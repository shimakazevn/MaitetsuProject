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

def make_clean_custom():
    p_steam = r'E:\MaitetsuProject\steam_version_patch_vn\Data_Decompile\data\main\custom.tjs'
    steam_custom = descramble(p_steam)
    
    # 1. Enable CustomMsgwinRender class by replacing '@if (0)' before CustomMsgwinRender with '@if (1)'
    target_pattern = '@if (0)\r\n//==============\r\n// 英語等で文字がはみ出た時の特殊処理'
    if target_pattern in steam_custom:
        steam_custom = steam_custom.replace(target_pattern, '@if (1)\r\n//==============\r\n// 英語等で文字がはみ出た時の特殊処理')
        print("[OK] Enabled CustomMsgwinRender class (@if (1))")
    else:
        lines = steam_custom.splitlines()
        for i, l in enumerate(lines):
            if '@if (0)' in l and i + 2 < len(lines) and 'はみ出た' in lines[i+2]:
                lines[i] = '@if (1)'
                print(f"[OK] Enabled CustomMsgwinRender at line {i+1}")
                break
        steam_custom = '\r\n'.join(lines)
    
    # 2. Patch font aliases in custom.tjs (replace default fallback from "源ノ角ゴシックB" to "Signika Negative")
    steam_custom = steam_custom.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "源ノ角ゴシックB", "MessageDefaultFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "Signika Negative", "MessageDefaultFontFace");'
    )
    steam_custom = steam_custom.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "源ノ角ゴシックH", "MessageRubyFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "Signika Negative Bold", "MessageRubyFontFace");'
    )
    
    # 3. Insert PreRenderFontEx.AddTrueTypeFont right after alias definitions
    font_init_block = """
// Register Signika Negative TrueType fonts with PreRenderFontEx
if (typeof global.PreRenderFontEx != "undefined" && typeof global.PreRenderFontEx.AddTrueTypeFont != "undefined") {
	try {
		PreRenderFontEx.AddTrueTypeFont("Signika Negative", "Signika Negative", "SignikaNegative-Regular.ttf", void, %[ comment: "Phông chữ Signika Negative (Thường)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Bold", "Signika Negative Bold", "SignikaNegative-Bold.ttf", void, %[ comment: "Phông chữ Signika Negative (Đậm)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative SemiBold", "Signika Negative SemiBold", "SignikaNegative-SemiBold.ttf", void, %[ comment: "Phông chữ Signika Negative (Bán Đậm)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Medium", "Signika Negative Medium", "SignikaNegative-Medium.ttf", void, %[ comment: "Phông chữ Signika Negative (Vừa)" ]);
		PreRenderFontEx.AddTrueTypeFont("Signika Negative Light", "Signika Negative Light", "SignikaNegative-Light.ttf", void, %[ comment: "Phông chữ Signika Negative (Nhẹ)" ]);
	} catch(e) {
		dm("PreRenderFontEx register notice: " + e.message);
	}
}
"""
    alias_pos = steam_custom.find('PreRenderFontEx.AddAlias("*RubyFont*"')
    if alias_pos != -1:
        end_brace = steam_custom.find('}', alias_pos)
        if end_brace != -1:
            end_block = steam_custom.find('}', end_brace + 1)
            if end_block != -1:
                steam_custom = steam_custom[:end_block+1] + '\r\n' + font_init_block + steam_custom[end_block+1:]
                print("[OK] Inserted PreRenderFontEx.AddTrueTypeFont block into custom.tjs")

    # 4. Vietnamese font & text enhancement block
    vn_block = """

// =========================================================================
// [VIETNAMESE LOCALIZATION - FONT & TEXT ENHANCEMENT HOOKS]
// =========================================================================

// Register TrueType Fonts for Vietnamese
try {
	Font.addFont("SignikaNegative-Regular.ttf");
	Font.addFont("SignikaNegative-Bold.ttf");
	Font.addFont("SignikaNegative-SemiBold.ttf");
	Font.addFont("SignikaNegative-Medium.ttf");
	Font.addFont("SignikaNegative-Light.ttf");
} catch (e) {
	dm("Font register notice: " + e.message);
}

// Hook PreRenderFontEx & FontDialogFilterFaceList to insert Signika Negative into the System Font Dialog
function _registerVietnameseFontList() {
	var fontNames = [
		"Signika Negative",
		"Signika Negative Bold",
		"Signika Negative SemiBold",
		"Signika Negative Medium",
		"Signika Negative Light"
	];
	
	// Add to PreRenderFontEx if available
	if (typeof global.PreRenderFontEx != "undefined" && typeof global.PreRenderFontEx.PreRenderFontNames != "undefined") {
		for (var i = fontNames.count - 1; i >= 0; i--) {
			var fn = fontNames[i];
			if (global.PreRenderFontEx.PreRenderFontNames.find(fn) < 0) {
				global.PreRenderFontEx.PreRenderFontNames.insert(0, fn);
			}
		}
	}
	
	// Hook SystemConfig.FontDialogFilterFaceList to ensure Signika fonts are always present in the selection dialog
	if (typeof SystemConfig.FontDialogFilterFaceList == "Function") {
		if (typeof global._orig_FontDialogFilterFaceList == "undefined") {
			global._orig_FontDialogFilterFaceList = SystemConfig.FontDialogFilterFaceList;
			SystemConfig.FontDialogFilterFaceList = function(list) {
				if (global._orig_FontDialogFilterFaceList) (global._orig_FontDialogFilterFaceList incontextof global)(list);
				var vfonts = [
					"Signika Negative",
					"Signika Negative Bold",
					"Signika Negative SemiBold",
					"Signika Negative Medium",
					"Signika Negative Light"
				];
				for (var i = vfonts.count - 1; i >= 0; i--) {
					var vf = vfonts[i];
					if (list.find(vf) < 0) {
						list.insert(0, vf);
					}
				}
			};
		}
	} else {
		SystemConfig.FontDialogFilterFaceList = function(list) {
			var vfonts = [
				"Signika Negative",
				"Signika Negative Bold",
				"Signika Negative SemiBold",
				"Signika Negative Medium",
				"Signika Negative Light"
			];
			for (var i = vfonts.count - 1; i >= 0; i--) {
				var vf = vfonts[i];
				if (list.find(vf) < 0) {
					list.insert(0, vf);
				}
			}
		};
	}
}

// Enable 3-line layout and dynamic auto-shrink font scaling
with (SystemConfig) {
	.multiLangRenderMsgwinAutoScale = 1;
	.multiLangRenderMsgwinExpandRect = ["meswin_normal", "base.textmax"];
	.multiLangRenderMsgwinCutLF = 0;
	.multiLangRenderMsgwinClass = "CustomMsgwinRender";
}

// Backlog dynamic font scaling for Vietnamese text
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
		dm("CustomBacklog dynamic font hook applied!");
	}
}

// Scene selection compact font
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

// Hook KAGLoadScript to attach hooks on script load
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

// After init font mapping to Signika Negative
addAfterInitCallback(function() {
	_registerVietnameseFontList();
	if (typeof global.MessageDefaultFontFaceMap == "Object") {
		global.MessageDefaultFontFaceMap.tw = "Signika Negative";
	}
	if (typeof global.SystemDefaultFontFaceMap == "Object") {
		global.SystemDefaultFontFaceMap.tw = "Signika Negative";
	}
	if (typeof global.SystemSettingFontFaceMap == "Object") {
		global.SystemSettingFontFaceMap.tw = "Signika Negative";
	}
	if (typeof global.MessageRubyFontFaceMap == "Object") {
		global.MessageRubyFontFaceMap.tw = "Signika Negative Bold";
	}
	if (typeof kag.setLanguageFont != "undefined" && typeof global.LanguageTags == "Object") {
		for (var i = 0; i < global.LanguageTags.count; i++) {
			if (global.LanguageTags[i] == "tw") {
				try { kag.setLanguageFont("Signika Negative", i); } catch(e){}
			}
		}
	}
	try {
		kag.chDefaultFace = "Signika Negative";
		kag.setMessageLayerUserFont();
	} catch(e){}
	_applyBacklogHook();
	_applyExChViewHook();
}, 50);
"""
    
    final_content = steam_custom + vn_block
    target = r'E:\MaitetsuProject\steam_version_patch_vn\patch_assets\custom.tjs'
    with open(target, 'wb') as f:
        f.write(b'\xff\xfe')
        f.write(final_content.encode('utf-16le'))
    print(f"Successfully generated Steam custom.tjs at {target} ({os.path.getsize(target)} bytes)")

if __name__ == '__main__':
    make_clean_custom()
