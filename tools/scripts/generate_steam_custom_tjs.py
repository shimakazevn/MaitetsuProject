import os
import struct
import re

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
    
    # 0. Add AutoPath re-mounting at top
    autopath_header = 'Storages.addAutoPath(System.exePath + "unencrypted.xp3>");\r\n'
    if not steam_custom.startswith('Storages.addAutoPath'):
        steam_custom = autopath_header + steam_custom

    # 1. Fix GetFontFaceMap cleanly with try/catch
    new_getfontfacemap = '''function GetFontFaceMap(tag, table, defval, log) {
	if (table !== void && typeof table == "Object" && tag !== void && tag != "") {
		try {
			var face = table[tag];
			if (face !== void && face != "") return face;
		} catch (e) {
		}
	}
	return defval;
}'''
    steam_custom = re.sub(
        r'function\s+GetFontFaceMap\s*\([^)]*\)\s*\{[^}]*\}',
        new_getfontfacemap,
        steam_custom,
        count=1
    )
    print("[OK] Replaced GetFontFaceMap with clean safe try/catch implementation")

    # 2. Replace prototype CustomMsgwinRender with our perfected 3-State Dynamic Engine
    three_state_render_block = """//==============
// 英語等で文字がはみ出た時の特殊処理

&RenderMsgwinPlugin.MsgwinRender =
/**/          CustomMsgwinRender ;
class         CustomMsgwinRender extends MsgwinRender {
	function  CustomMsgwinRender { super.MsgwinRender(...); }
	function finalize { super.finalize(...); }

	var _renderWidth;
	var _renderHeight;
	function setRenderSize(w, h) {
		_renderWidth = w;
		_renderHeight = h;
		return super.setRenderSize(...);
	}
	var _orig_ox, _orig_oy;
	function init() {
		var r = super.init(...);
		_orig_ox = ox;
		_orig_oy = oy;
		return r;
	}

	// Reset render area with dynamic oy for vertical balance
	function _resetRenderArea(customOy) {
		ox = _orig_ox;
		oy = (customOy !== void) ? customOy : _orig_oy;
		_TextRenderBase.clear();
	}

	function render(elm, diff=0, time=0) {
		var standardH = (_renderHeight !== void && _renderHeight > 0) ? _renderHeight : 60;
		var standardW = (_renderWidth  !== void && _renderWidth  > 0) ? _renderWidth  : 1000;

		// =============================================================
		// [STATE 1: 1-2 DÒNG CHUẨN]
		// - Cỡ chữ: 100% (26px) to rõ
		// - Line spacing: 7px thoáng đãng
		// - oy: _orig_oy - 3 (~60px) -> Lề trên 35px / Lề dưới 36px (Cân giữa)
		// =============================================================
		_reFontScale = 1.0;
		defaultLineSpacing = 7;
		resetStyle();
		_resetRenderArea(_orig_oy - 3);
		super.setRenderSize(standardW, standardH);
		if (!_internalRender(...)) {
			return; // Khớp chuẩn State 1!
		}

		// =============================================================
		// [STATE 2: 2-3 DÒNG TRUNG GIAN]
		// - Cỡ chữ: 91% (~23.5px) vừa vặn cho câu 2 dòng hơi dài
		// - Line spacing: 5px thanh thoát
		// - oy: _orig_oy + 1 (~64px) -> Lề trên 39px / Lề dưới 39px (Cân giữa tuyệt đối)
		// =============================================================
		_reFontScale = 0.91;
		defaultLineSpacing = 5;
		resetStyle();
		_resetRenderArea(_orig_oy + 1);
		super.setRenderSize(standardW, standardH);
		if (!_internalRender(...)) {
			return; // Khớp chuẩn State 2!
		}

		// =============================================================
		// [STATE 3: 3 DÒNG MỞ RỘNG]
		// - Cỡ chữ: 82% (~21px)
		// - Line spacing: 4px gọn gàng
		// - oy: _orig_oy - 12 (~51px) -> Lề trên 26px / Lề dưới 29px (Cân giữa tuyệt đối)
		// - Khung mở rộng: 102px
		// =============================================================
		function _(storage, tag) {
			var parse = uiloadParse(%[ storage:storage ]);
			return uiloadGetRect(tag, parse.result);
		}
		var rect;
		if (typeof _.overRect == "undefined") {
			rect = _.overRect = _("meswin_normal", "base.textmax");
			dm("renderLang:overRect", getPrint(rect));
		} else rect = _.overRect;

		var maxH = rect ? rect.h : 102;
		var threeLineOy = _orig_oy - 12; // ~51px

		_reFontScale = 0.82;
		defaultLineSpacing = 4;
		resetStyle();
		_resetRenderArea(threeLineOy);
		super.setRenderSize(standardW, maxH);

		if (!_internalRender(...)) {
			return; // Khớp chuẩn State 3 với 3 dòng trải đều!
		}

		// =============================================================
		// [DỰ PHÒNG]: Câu cực dài (> 3 dòng ở 82%)
		// =============================================================
		var scale = 0.82;
		var retries = 0;
		while (true) {
			scale -= 0.04;
			if (scale < 0.60) break; // Minimum scale floor
			_reFontScale = scale;
			_resetRenderArea(threeLineOy);
			super.setRenderSize(standardW, maxH);
			if (!_internalRender(...)) {
				return; // Tìm được scale tối ưu nhất
			}
			++retries;
			if (retries > 8) break;
		}
	}

	function _internalRender {
		super.render(...);
		super.done();
		return renderOver;
	}

	var _reFontScale = 1.0;
	function getMainLangFontScale { return super.getMainLangFontScale(...) * _reFontScale; }
	function getSubLangFontScale  { return super.getSubLangFontScale (...) * _reFontScale; }
}
global.CustomMsgwinRender = CustomMsgwinRender;"""

    # Replace the old @if (0) ... @endif block
    steam_custom = re.sub(
        r'@if\s*\([01]\)\s*\r?\n//==============\r?\n//\s*英語等で文字がはみ出た時の特殊処理.*?\r?\n@endif',
        '@if (1)\r\n' + three_state_render_block + '\r\n@endif',
        steam_custom,
        flags=re.DOTALL
    )
    print("[OK] Replaced Steam CustomMsgwinRender with 3-State Engine")
    
    # 3. Patch font aliases in custom.tjs (replace default fallback to "Signika Negative")
    steam_custom = steam_custom.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "源ノ角ゴシックB", "MessageDefaultFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageDefaultFontFaceMap, "Signika Negative", "MessageDefaultFontFace");'
    )
    steam_custom = steam_custom.replace(
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "源ノ角ゴシックH", "MessageRubyFontFace");',
        'return GetFontFaceMap(CurrentLanguageTag,   MessageRubyFontFaceMap,    "Signika Negative Bold", "MessageRubyFontFace");'
    )

    # 4. Clean hooks for word-break, 3-line layout, Backlog & SceneSel
    vn_block = """

// =========================================================================
// [VIETNAMESE LOCALIZATION HOOKS]
// =========================================================================

// Configure word break for Vietnamese
if (typeof SystemConfig.multiLangParamsMap != "undefined") {
	SystemConfig.multiLangParamsMap["tw"] = %[word_break: 0, width_time_scale: 1];
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

// Apply hooks after init and attach CustomMsgwinRender plugin
addAfterInitCallback(function() {
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
    
    final_content = steam_custom + vn_block
    target = r'E:\MaitetsuProject\steam_version_patch_vn\patch_assets\custom.tjs'
    with open(target, 'wb') as f:
        f.write(b'\xff\xfe')
        f.write(final_content.encode('utf-16le'))
    print(f"Successfully generated Steam custom.tjs at {target} ({os.path.getsize(target)} bytes)")

if __name__ == '__main__':
    make_clean_custom()
