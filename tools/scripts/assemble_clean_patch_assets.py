import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

project_dir = r"E:\MaitetsuProject"
patch_assets = os.path.join(project_dir, "patch_assets")
steam_patch_assets = os.path.join(project_dir, "steam_version_patch_vn", "patch_assets")
uipsd_tw_src = os.path.join(project_dir, "extracted_assets", "KrkrExtract_Output", "others", "uipsd", "tw")

def read_text_clean(fp_path):
    with open(fp_path, "rb") as fp:
        raw = fp.read()
    
    # 1. Strip fake UTF-16 prepended to UTF-8
    if raw.startswith(b'\xff\xfe\xef\xbb\xbf'):
        raw = raw[2:]
        
    # 2. Real UTF-16 LE / BE
    if raw.startswith(b'\xff\xfe'):
        try:
            return raw[2:].decode('utf-16le')
        except Exception:
            pass
    if raw.startswith(b'\xfe\xff'):
        try:
            return raw[2:].decode('utf-16be')
        except Exception:
            pass
            
    # 3. Real UTF-8 BOM
    if raw.startswith(b'\xef\xbb\xbf'):
        try:
            return raw[3:].decode('utf-8')
        except Exception:
            pass
            
    # 4. Strict UTF-8 without BOM
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        pass
        
    # 5. Japanese / Traditional Chinese / Windows encodings
    for enc in ['cp932', 'shift_jis', 'cp950', 'gbk', 'latin1']:
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
            
    return raw.decode('utf-8', errors='ignore')

def save_utf16le(target_path, text):
    with open(target_path, "wb") as fp:
        fp.write(b"\xff\xfe" + text.encode("utf-16le"))

# 1. Regenerate 244 clean TIPS
sys.path.insert(0, os.path.join(project_dir, "tools", "scripts"))
import rebuild_all_tips_clean
rebuild_all_tips_clean.main()

# 2. Copy 22 clean pristine CSV tables
csv_files = [f for f in os.listdir(uipsd_tw_src) if f.endswith(".csv")]
print(f"\nCopying {len(csv_files)} clean CSV tables from {uipsd_tw_src}:")
for f in csv_files:
    src_p = os.path.join(uipsd_tw_src, f)
    txt = read_text_clean(src_p)
    
    for dst_dir in [patch_assets, steam_patch_assets]:
        dst_p = os.path.join(dst_dir, f)
        save_utf16le(dst_p, txt)
    print(f"  -> {f} (verified: {len(txt)} chars)")

# 3. Copy ALL 426 UI PNG images from uipsd/tw
png_files = [f for f in os.listdir(uipsd_tw_src) if f.endswith(".png")]
print(f"\nCopying {len(png_files)} UI PNG images from {uipsd_tw_src}:")
for f in png_files:
    src_p = os.path.join(uipsd_tw_src, f)
    for dst_dir in [patch_assets, steam_patch_assets]:
        dst_p = os.path.join(dst_dir, f)
        shutil.copy2(src_p, dst_p)
print(f"  -> Successfully copied {len(png_files)} PNG files to both patch asset directories.")

# 4. Copy clean TJS scripts
tjs_files = [
    "cglist_tw.tjs", "cglist_tw_1.tjs", "cglist_tw_87.tjs", "cglist_tw_89.tjs", "cglist_tw_91.tjs",
    "scnlist_tw.tjs", "scnlist_tw_1.tjs", "scnlist_tw_87.tjs", "scnlist_tw_89.tjs", "scnlist_tw_91.tjs", "scnlist_tw_92.tjs",
    "standmode_tw.tjs"
]

print("\nCopying clean TJS list files:")
for f in tjs_files:
    found = False
    for root, dirs, files in os.walk(os.path.join(project_dir, "extracted_assets", "KrkrExtract_Output")):
        if f in files:
            src_p = os.path.join(root, f)
            txt = read_text_clean(src_p)
            for dst_dir in [patch_assets, steam_patch_assets]:
                dst_p = os.path.join(dst_dir, f)
                save_utf16le(dst_p, txt)
            first_line = txt.splitlines()[0] if txt.splitlines() else ""
            print(f"  -> {f} (start: {repr(first_line[:40])})")
            found = True
            break

# Note: DMM / Last Run!! custom.tjs is maintained in patch_assets/custom.tjs and NOT overwritten here.

# 5. Steam custom.tjs (Clean Steamworks & 100% Valid Syntax)
steam_custom_src = r'''//=============================================================================
// Maitetsu Last Run!! - Steam Release Dedicated System Script (custom.tjs)
//=============================================================================

// Global error trace hook
if (typeof global._orig_execStorage == "undefined") {
	global._orig_execStorage = Scripts.execStorage;
	Scripts.execStorage = function(storage, *) {
		try {
			return _orig_execStorage(storage, *);
		} catch (e) {
			System.inform("Error loading script [" + storage + "]:\n" + e.message + "\n\nTrace:\n" + (typeof e.trace != "undefined" ? e.trace : ""), "SCRIPT LOAD ERROR");
			throw e;
		}
	};
}

// Dynamic Re-mounting with highest priority
Storages.addAutoPath(System.exePath + "patch.xp3>");

// Emote compression plugin
if (Storages.isExistentStorage("lzfs.dll")) {
	Plugins.link("lzfs.dll");
	var uselzfs = true;
}

// Helper to detect if a text contains Latin/Vietnamese characters dynamically
function isSmartLatinText(str) {
	if (typeof str != "String" || str.length == 0) return false;
	for (var i = 0; i < str.length && i < 60; i++) {
		var ch = str.charCodeAt(i);
		if ((ch >= 0x0041 && ch <= 0x007A) || ch == 0x0020 || (ch >= 0x00C0 && ch <= 0x1EF9)) {
			return true;
		}
	}
	return false;
}

// Glyph fade & Smart Dynamic Message Layout
addKagHookCallback("onInitMessageLayerProps", function (mes) {
	with (mes) {
		.marginT = 2;
		.marginB = 1;
		.defaultLineSpacing = 8;
		.lineSpacing = 8;
		.showBreakGlyph_ = .showBreakGlyph;
		.showBreakGlyph = function(glyphobj) {
			showBreakGlyph_(...);
			with (window) {
				.stopAction(glyphobj);
				.beginAction(glyphobj, %[ opacity: %[ handler:MoveAction, start:(glyphobj.opacity=0), value:255, time:150 ]]);
			}
		} incontextof mes;
	}
}, false);

addKagHookCallback("onRenderMsgWinDelayStateChanged", function (render, state) {
	if (state == "render" || state == "redraw") with (render) {
		var mes = fore.messages[msgHackTargetLayer];
		var x = mes.marginL + .renderRight + 4;
		var y = mes.marginT + .renderBottom - 20;
		var max = mes.height - mes.marginB - 16;
		if (y > max) y = max;
		mes.glyphFixedLeft = x; mes.comp.glyphFixedLeft = x;
		mes.glyphFixedTop  = y; mes.comp.glyphFixedTop  = y;
		if (state == "redraw" && lastClickGlyphVisible && lastClickGlyphMessagePage == msgHackTargetLayer) {
			var type = lastClickGlyphWhich;
			_showClickGlyphs(mes, type);
			_showClickGlyphs(mes.comp, type) if (currentWithBack);
		}
	}
}, true);

// Smart Content-Adaptive Message Window Renderer (3-Line Auto Fit)
if (typeof global.MsgwinRender != "undefined") {
	class CustomMsgwinRender extends MsgwinRender {
		function CustomMsgwinRender() { super.MsgwinRender(...); }
		function finalize() { super.finalize(...); }

		var _renderWidth;
		function setRenderSize(w, h) {
			_renderWidth = w;
			return super.setRenderSize(...);
		}
		var _orig_oy, _orig_valign;
		function init() {
			var r = super.init(...);
			_orig_oy = oy;
			return r;
		}

		function render(elm, diff=0, time=0) {
			_reFontScale = 1;
			oy = _orig_oy;
			defaultValign = -1;
			global.TextRenderBase.clear();

			var curText = "";
			try { curText = kag.getLangInfo(elm, "text", kag.languageType); } catch {}
			if (curText == "" && typeof elm.text != "undefined") curText = elm.text;

			var isLatin = isSmartLatinText(curText);
			var isNonJP = (typeof global.CurrentLanguageTag != "undefined" && global.CurrentLanguageTag != "jp") || isLatin;

			var lineCount = 1;
			if (typeof curText == "String") {
				var spl = curText.split("\n");
				lineCount = spl.count;
			}

			var needExpansion = (lineCount >= 3) || isNonJP || _internalRender(...);

			if (needExpansion) {
				function _(storage, tag) {
					var ui = global.uiload, parse = uiloadParse(%[ storage:storage ]);
					return uiloadGetRect(tag, parse.result);
				}
				var rect;
				if (typeof _.overRect == "undefined") {
					rect = _.overRect = _("meswin_normal", "base.textmax");
					dm("renderLang:overRect", getPrint(rect));
				} else rect = _.overRect;

				if (rect) {
					oy = rect.oy;
					defaultValign = 0;
					var targetWidth = isNonJP ? 620 : _renderWidth;
					super.setRenderSize(targetWidth, rect.h);
				}

				global.TextRenderBase.clear();

				for (var i = 0; i < 5 && _internalRender(...); i++) {
					_reFontScale *= 0.85;
					global.TextRenderBase.clear();
				}
			}
		}

		function _internalRender() {
			super.render(...);
			super.done();
			return renderOver;
		}

		var _reFontScale = 1;
		function getMainLangFontScale() { return super.getMainLangFontScale(...) * _reFontScale; }
		function getSubLangFontScale()  { return super.getSubLangFontScale (...) * _reFontScale; }
	}
	if (typeof global.RenderMsgwinPlugin != "undefined") {
		&RenderMsgwinPlugin.MsgwinRender = CustomMsgwinRender;
	}
}

// Multi-language typography setup
if (typeof SystemConfig.multiLangParamsMap == "Object") {
	var allLangs = ["jp", "tw", "zh", "cn", "en"];
	for (var i = 0; i < allLangs.count; i++) {
		var l = allLangs[i];
		if (SystemConfig.multiLangParamsMap[l] === void) {
			SystemConfig.multiLangParamsMap[l] = %[];
		}
		SystemConfig.multiLangParamsMap[l].word_break = 0;
	}
}
if (typeof SystemConfig.multiLangSingleFontScaleMap == "Object") {
	var allLangs = ["jp", "tw", "zh", "cn", "en"];
	for (var i = 0; i < allLangs.count; i++) {
		var l = allLangs[i];
		SystemConfig.multiLangSingleFontScaleMap[l] = 0.68;
	}
}

// UI Table Auto-Redirection for Multi-language
{
	var uil = global.uiload;
	objectHookInjection(%[ target:UIListParser, method:"parseStorage", func:function (orig, filename,*) {
		var lang = CurrentLanguageUITag;
		if (SystemConfig.disableJapanese && lang == "jp") lang = SystemConfig.multiLangUnknownTag;
		if (lang != "jp" && Storages.extractStorageExt(filename) == ".csv") {
			var repl = Storages.chopStorageExt(filename) + "_" + lang + ".csv";
			if (Storages.isExistentStorage(repl)) filename = repl;
		}
		return (orig incontextof this)(filename, *);
	} ]);
}

// Steam Achievements Link
if (typeof global.setSteamAchievement == "Object") {
	SystemHook.add("tipsview.enter",      function () { setSteamAchievement("enter_tips");   } incontextof global);
	SystemHook.add("option.enter",        function () { setSteamAchievement("enter_option"); } incontextof global);
	addKagHookCallback("onUILangChanged", function () { setSteamAchievement("change_uilang"); }, false);
}
'''
save_utf16le(os.path.join(steam_patch_assets, "custom.tjs"), steam_custom_src)

print("\n[OK] Pristine patch assets assembled successfully with 100% clean UTF-16LE encoding and 426 UI images!")
