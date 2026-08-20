import os
import struct

def descramble(p):
    with open(p, 'rb') as f:
        raw = f.read()
    if raw[:2] == b'\xfe\xfe':
        mode = raw[2]
        body = raw[5:]
        if mode == 1:
            out = bytearray()
            for i in range(0, len(body), 2):
                if i + 1 < len(body):
                    d = struct.unpack_from('<H', body, i)[0]
                    d = ((d & 0xAAAA) >> 1) | ((d & 0x5555) << 1)
                    out.extend(struct.pack('<H', d))
            return out.decode('utf-16le', errors='ignore')
        else:
            return raw[5:].decode('utf-16le', errors='ignore')
    elif raw[:2] == b'\xff\xfe':
        return raw[2:].decode('utf-16le', errors='ignore')
    else:
        return raw.decode('utf-8', errors='ignore')

def make_clean_steam_config():
    p_orig = r'E:\MaitetsuProject\steam_version_patch_vn\Data_Decompile\data\main\Config.tjs'
    text = descramble(p_orig)
    
    # Replace the 4 font mapping lines exactly like DMM version
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'global.SystemDefaultFontFaceMap' in line:
            lines[i] = ';global.SystemDefaultFontFaceMap  = %[ jp:"源ノ角ゴシックB", en:"源ノ角ゴシックB", cn:"思源宋体B", tw:"Signika Negative" ]; // 言語別システムフォントマップ'
            print(f"[OK] Patched SystemDefaultFontFaceMap at line {i+1}")
        elif 'global.SystemSettingFontFaceMap' in line:
            lines[i] = ';global.SystemSettingFontFaceMap  = %[ jp:"源ノ明朝B",       en:"源ノ明朝B",       cn:"思源宋体B", tw:"Signika Negative" ]; // 言語別コンフィグ画面用テキストフォント'
            print(f"[OK] Patched SystemSettingFontFaceMap at line {i+1}")
        elif 'global.MessageDefaultFontFaceMap' in line:
            lines[i] = ';global.MessageDefaultFontFaceMap = %[ jp:"ニューシネマA",   en:"源ノ明朝B",       cn:"思源宋体B", tw:"Signika Negative" ];'
            print(f"[OK] Patched MessageDefaultFontFaceMap at line {i+1}")
        elif 'global.MessageRubyFontFaceMap' in line:
            lines[i] = ';global.MessageRubyFontFaceMap    = %[ jp:"源ノ角ゴシックH", en:"源ノ角ゴシックH", cn:"思源黑体H", tw:"Signika Negative Bold" ]; // 言語別ルビフォントマップ'
            print(f"[OK] Patched MessageRubyFontFaceMap at line {i+1}")
            
    out_text = '\r\n'.join(lines)
    target = r'E:\MaitetsuProject\steam_version_patch_vn\patch_assets\Config.tjs'
    with open(target, 'wb') as f:
        f.write(b'\xff\xfe')
        f.write(out_text.encode('utf-16le'))
    print(f"[OK] Generated clean Steam Config.tjs at {target} ({os.path.getsize(target)} bytes)")

def apply_dmm_logic_to_steam_custom():
    p_orig = r'E:\MaitetsuProject\steam_version_patch_vn\Data_Decompile\data\main\custom.tjs'
    text = descramble(p_orig)
    
    # 1. Patch font aliases around lines 210-220 (exact DMM behavior)
    text = text.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "源ノ角ゴシックB", "MessageDefaultFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "Signika Negative", "MessageDefaultFontFace");'
    )
    text = text.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "源ノ角ゴシックH", "MessageRubyFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "Signika Negative Bold", "MessageRubyFontFace");'
    )
    
    # 2. Insert PreRenderFontEx & TTF registration block right after alias block (exact DMM behavior)
    dmm_font_block = """with (SystemConfig) {
	.PreRenderFontSelectOnly = true;
	.multiLangRenderMsgwinAutoScale = 1;
	.multiLangRenderMsgwinExpandRect = ["meswin_normal", "base.textmax"];
	.multiLangRenderMsgwinClass = "CustomMsgwinRender";
}

// Register Signika Negative TrueType fonts (DMM Architecture)
try {
	if (typeof global.PreRenderFontEx != "undefined" && typeof global.PreRenderFontEx.AddTrueTypeFont != "undefined") {
		PreRenderFontEx.AddTrueTypeFont("Signika Negative", "Signika Negative", "SignikaNegative-Regular.ttf", void, %[ comment: "Phông chữ Signika Negative" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Bold", "Signika Negative Bold", "SignikaNegative-Bold.ttf", void, %[ comment: "Phông chữ Signika Negative (Đậm)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative SemiBold", "Signika Negative SemiBold", "SignikaNegative-SemiBold.ttf", void, %[ comment: "Phông chữ Signika Negative (Bán Đậm)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Medium", "Signika Negative Medium", "SignikaNegative-Medium.ttf", void, %[ comment: "Phông chữ Signika Negative (Vừa)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Light", "Signika Negative Light", "SignikaNegative-Light.ttf", void, %[ comment: "Phông chữ Signika Negative (Nhẹ)" ]);
	}
} catch (e) {
	dm("Font register notice: " + e.message);
}
"""
    alias_search = 'PreRenderFontEx.AddAlias("*RubyFont*"'
    pos = text.find(alias_search)
    if pos != -1:
        end_brace = text.find('}', pos)
        if end_brace != -1:
            end_block = text.find('}', end_brace + 1)
            if end_block != -1:
                text = text[:end_block+1] + '\r\n' + dmm_font_block + text[end_block+1:]
                print("[OK] Inserted PreRenderFontEx TTF registration block")

    # 3. Adjust Message Layer spacing in onInitMessageLayerProps (exact DMM behavior)
    layer_search = 'addKagHookCallback("onInitMessageLayerProps", function (mes) {'
    pos_layer = text.find(layer_search)
    if pos_layer != -1:
        with_pos = text.find('with (mes) {', pos_layer)
        if with_pos != -1:
            spacing_code = '\r\n\t\tif (typeof global.CurrentLanguageTag != "undefined" && global.CurrentLanguageTag != "jp") {\r\n\t\t\t.marginT = 2;\r\n\t\t\t.marginB = 0;\r\n\t\t\t.defaultLineSpacing = 7;\r\n\t\t}'
            text = text[:with_pos + len('with (mes) {')] + spacing_code + text[with_pos + len('with (mes) {'):]
            print("[OK] Inserted message layer line-spacing and margin hook")

    # 4. Enable CustomMsgwinRender class (change @if (0) -> @if (1))
    target_pattern = '@if (0)\r\n//==============\r\n// 英語等で文字がはみ出た時の特殊処理'
    if target_pattern in text:
        text = text.replace(target_pattern, '@if (1)\r\n//==============\r\n// 英語等で文字がはみ出た時の特殊処理')
        print("[OK] Enabled CustomMsgwinRender class (@if (1))")
    else:
        lines = text.splitlines()
        for i, l in enumerate(lines):
            if '@if (0)' in l and i + 2 < len(lines) and 'はみ出た' in lines[i+2]:
                lines[i] = '@if (1)'
                print(f"[OK] Enabled CustomMsgwinRender at line {i+1}")
                break
        text = '\r\n'.join(lines)

    # 5. Append DMM hooks at end of custom.tjs (Backlog, Scene Selection, AfterInitCallback)
    dmm_tail_block = """

// =========================================================================
// [DMM ARCHITECTURE - BACKLOG & SCENE SELECTION & AFTER INIT FONT HOOKS]
// =========================================================================

function _applyBacklogHook() {
	if (typeof global.CustomBacklog != "undefined" && typeof global._orig_CustomBacklog_drawTextBlock == "undefined") {
		global._orig_CustomBacklog_drawTextBlock = CustomBacklog.drawTextBlock;
		CustomBacklog.drawTextBlock = function(arg0, arg1) {
			var rawText = (typeof kag.getLangInfo != "undefined") ? string(kag.getLangInfo(arg1, "text")) : string(arg1.text);
			var cleanText = rawText.replace(/(\\r|\\n|\\[.*?\\])/g, "");
			var charCount = cleanText.length;
			var lines = rawText.split("\\n");
			var hasName = (arg1.name != "" || arg1.disp != "");
			var max2LineChars = hasName ? 80 : 98;
			var isThreeLines = (lines.count >= 3) || (charCount > max2LineChars);
			var isMedium2Lines = !isThreeLines && (charCount > (hasName ? 50 : 65));

			var orig_fontSize = _render.defaultFontSize;
			var orig_lineSpacing = _render.defaultLineSpacing;

			if (isThreeLines) {
				_render.defaultFontSize = 19;
				_render.defaultLineSpacing = 2;
			} else if (isMedium2Lines) {
				_render.defaultFontSize = 22;
				_render.defaultLineSpacing = 3;
			} else {
				_render.defaultFontSize = 24;
				_render.defaultLineSpacing = 5;
			}
			_render.resetStyle();

			var r = (global._orig_CustomBacklog_drawTextBlock incontextof this)(...);

			_render.defaultFontSize = orig_fontSize;
			_render.defaultLineSpacing = orig_lineSpacing;
			_render.resetStyle();
			return r;
		};
		dm("CustomBacklog 3-state dynamic font hook applied!");
	}
}

function _applyExChViewHook() {
	if (typeof global.ExCVTextEdit != "undefined" && typeof global._orig_ExCVTextEdit_drawText == "undefined") {
		global._orig_ExCVTextEdit_drawText = ExCVTextEdit.drawText;
		ExCVTextEdit.drawText = function(arg0, arg1) {
			if (arg0 !== void) {
				if (typeof arg0.font != "Object" || arg0.font === void) {
					arg0.font = %[];
				}
				arg0.font.size = 21;
			}
			var local0 = getMessageLayer(arg1);
			if (local0) {
				local0.defaultFontSize = 21;
				local0.defaultLineSpacing = 5;
			}
			return (global._orig_ExCVTextEdit_drawText incontextof this)(...);
		};
		dm("ExCVTextEdit (SceneSel) compact font size 21 hook applied!");
	}
}

// Hook KAGLoadScript to guarantee hooks are attached as soon as scripts load
if (typeof global._orig_KAGLoadScript_Custom == "undefined") {
	global._orig_KAGLoadScript_Custom = global.KAGLoadScript;
	global.KAGLoadScript = function(storage) {
		var r = (global._orig_KAGLoadScript_Custom incontextof global)(...);
		if (storage == "backlog.tjs") {
			_applyBacklogHook();
		} else if (storage == "exchview.tjs") {
			_applyExChViewHook();
		}
		return r;
	};
}

// Hook default font to Signika Negative, CustomMsgwinRender, Backlog and SceneSel
addAfterInitCallback(function() {
	if (typeof global.MessageDefaultFontFaceMap == "Object") {
		global.MessageDefaultFontFaceMap.tw = "Signika Negative";
	}
	if (typeof global.SystemDefaultFontFaceMap == "Object") {
		global.SystemDefaultFontFaceMap.tw = "Signika Negative";
	}
	if (typeof global.SystemSettingFontFaceMap == "Object") {
		global.SystemSettingFontFaceMap.tw = "Signika Negative";
	}
	if (typeof kag.setLanguageFont != "undefined") {
		try { kag.setLanguageFont("Signika Negative", "tw"); } catch(e){}
	}
	try {
		kag.chDefaultFace = "Signika Negative";
	} catch(e){}
	if (typeof global.CustomMsgwinRender != "undefined") {
		&RenderMsgwinPlugin.MsgwinRender = global.CustomMsgwinRender;
		if (typeof kag.renderMsgwinPlugin == "Object") {
			&kag.renderMsgwinPlugin.MsgwinRender = global.CustomMsgwinRender;
		}
	}
	_applyBacklogHook();
	_applyExChViewHook();
}, 50);
"""
    
    final_custom = text + dmm_tail_block
    target = r'E:\MaitetsuProject\steam_version_patch_vn\patch_assets\custom.tjs'
    with open(target, 'wb') as f:
        f.write(b'\xff\xfe')
        f.write(final_custom.encode('utf-16le'))
    print(f"[OK] Generated clean Steam custom.tjs at {target} ({os.path.getsize(target)} bytes)")

if __name__ == '__main__':
    make_clean_steam_config()
    apply_dmm_logic_to_steam_custom()
