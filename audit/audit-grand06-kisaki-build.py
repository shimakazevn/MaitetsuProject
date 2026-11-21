# -*- coding: utf-8 -*-
# Hand-written fix values for グランドリライト06_稀咲.txt.toml (audit-grand06-kisaki).
# Each fix was decided by reading that row's JP (+TW + neighbours).
# "\\n" below is a literal backslash-n (CSV3/TOML convention); "\\x" is literal backslash-x.
import csv, json

FIX = {
"1378": ("pronoun", "稀咲", "「Thời gian gặp được, sao——ufufu, hay đấy.\\nNghe cậu nói vậy, em vui lắm.」"),
"1426": ("pronoun", "稀咲", "「……Bố em ấy mà. Cậu thấy đấy, ông ấy cưng chiều con gái quá mức mà.」"),
"1852": ("pronoun", "稀咲", "「Với người bình thường thì có lẽ không đâu. Nhưng cậu biết không?\\nEm thì biết. Soutetsu đã trở nên dễ đoán hơn rất nhiều rồi.」"),
"1863": ("pronoun", "稀咲", "「Đâu có――\\nĐâu phải chuyện đáng để cậu phải cảm ơn đâu.」"),
"1867": ("pronoun", "双鉄", "「Không, tôi đủ rồi. Trà ngon lắm.」"),
"1877": ("pronoun", "双鉄", "「Không, lần này người có công lớn nhất không phải là cháu――\\nmà là Akai-guji mới đúng.」"),
"1885": ("pronoun", "稀咲", "「Để cậu đợi lâu rồi, Soutetsu.」"),
"1898": ("pronoun", "稀咲", "「Hửm? À――cậu nói em mới để ý,\\ntrông có vẻ khác với những chỗ còn lại nhỉ?」"),
"1907": ("pronoun", "稀咲", "「Từ giờ cậu sẽ còn phải giúp em nhiều hơn nữa đấy nhé?\\nĐổi lại, tất nhiên em cũng sẽ giúp đỡ cậu.」"),
"1923": ("pronoun", "双鉄", "「Nhưng……chuyển từ một công ty lớn ở Teito sang Đường sắt Ohito,\\ndù nói ra từ lập trường của tôi thì cũng hơi...」"),
"1932": ("pronoun", "双鉄", "「Nhưng nói chính xác hơn thì thế này.\\n『Tôi đang đợi đến giờ hẹn với Kisaki』.」"),
"1943": ("pronoun", "双鉄", "「Nếu được thì cho tôi nghe thử đi.\\nNếu là ý tưởng của Kisaki, thì tất nhiên tôi sẽ cân nhắc nghiêm túc.」"),
"1945": ("pronoun", "双鉄", "「Chính cô đã nói mà. Việc của thợ làm bánh thì để thợ làm bánh lo. Việc của thợ làm tàu thì để thợ làm tàu lo.\\n——Mỗi người chỉ cần hoàn thành tốt nhất vai trò của mình là được.」"),
"1947": ("pronoun", "双鉄", "「Nếu cô nghĩ vậy thì tốt quá.」"),
"1951": ("pronoun", "稀咲", "「Cậu vào trước nghỉ ngơi đi nhé?\\nEm có chút việc cần làm.」"),
"1957": ("pronoun", "双鉄", "「Nếu cô thích cách nói đó, thì có thể coi là vậy.」"),
"1959": ("pronoun", "稀咲", "「Cậu đang làm gì ở đây vậy?」"),
"1961": ("pronoun", "双鉄", "「Sao cô lại nhận ra?」"),
"1965": ("pronoun", "双鉄", "「Được cô nói vậy, tôi rất vinh hạnh.」"),
"1972": ("pronoun", "稀咲", "「Cậu thích đến vậy thì\\ncông em giới thiệu cũng bõ. Vui quá đi.」"),
"1973": ("pronoun", "双鉄", "「Cô cất công làm đến mức đó sao.」"),
"2006": ("pronoun", "稀咲", "「Đừng ngại, ăn đi Soutetsu.\\nEm chuẩn bị riêng cho cậu đấy.」"),
"2014": ("pronoun", "双鉄", "「Như tôi đã nói, hiện nay đường ray thay thế rất hiếm.\\nVì vậy ở Đường sắt Ohito, trừ khi có chuyện bất đắc dĩ, nếu không thì không thể thay được.」"),
"2024": ("pronoun", "双鉄", "「Ra là vậy. Nghe cô nói mới thấy đúng thật.\\nHóa ra trong sự im lặng đó――đã có vô số những thỏa thuận ngầm sao.」"),
"2054": ("pronoun", "双鉄", "「Có lẽ là có, nhưng tôi không biết.\\nỞ Đường sắt Ohito, công việc này do các tình nguyện viên làm thủ công.」"),
"2066": ("pronoun", "双鉄", "「Ừm——. À, không. Ừm.\\nChết thật, mặt tôi dễ đoán thế sao?」"),
"2077": ("sfx", "後東", "「Ha!」"),
"2078": ("pronoun", "稀咲", "「Aha, cậu tò mò rồi.」"),
"2093": ("pronoun", "双鉄", "「À, cô pha ấm mới cho tôi sao.」"),
"2106": ("gasp", "双鉄", "「Ư!?」"),
"2111": ("sfx", "双鉄", "「Ừ, ừm.」"),
"2116": ("pronoun", "双鉄", "「Ừm. Hôm nay trông cậy vào cô đấy.」"),
"2124": ("pronoun", "稀咲", "「Ừ. Đúng vậy. Chính vì thế mà cậu mới dẫn em đến đây――\\nđể tận mắt xem xét đường ray thực tế mà.」"),
"2127": ("pronoun", "稀咲", "「Ừ, đúng vậy.\\nViệc đó――ừ. Em cũng biết rõ mà.」"),
"2129": ("pronoun", "双鉄", "「Không, tôi thực sự rất thích.\\nKhông ngờ trà nhài và nhân đậu đỏ lại hợp nhau đến thế.」"),
"2134": ("pronoun", "双鉄", "「Được chứ. Cô đứng giữa hai thanh ray cũng không sao.\\nTuy nhiên, cố gắng đừng giẫm lên thanh ray nhé.」"),
"2136": ("pronoun", "双鉄", "「Hừm? ……Xin lỗi, cô có thể cho một ví dụ cụ thể được không?」"),
"2149": ("pronoun", "稀咲", "「Đó là vì, Soutetsu à? Em có hứng thú với cậu,\\nnên mới thường xuyên quan sát cậu đấy.」"),
"2169": ("pronoun", "双鉄", "「Tôi nghĩ đó là một cái tên tuyệt vời. ――Một cái tên thật tuyệt vời.\\nKisaki, thực sự cảm ơn cô.」"),
"2198": ("pronoun", "双鉄", "「Dù với Kisaki là vậy――\\nNhưng cảm ơn cô.」"),
"2288": ("pronoun", "双鉄", "「Tôi nghĩ là được. Vì thời Teitetsu,\\nnhững người tham gia vào công việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#; rất nhiều.」"),
"2300": ("pronoun", "稀咲", "「Vừa hay, em cũng chuẩn bị xong để đón tiếp cậu rồi.」"),
"2311": ("pronoun", "双鉄", "「Tôi nghe nói là do tàu hỏa chạy qua lại vô số lần,\\ndẫn đến hiện tượng mỏi kim loại trên đường ray.」"),
"2316": ("terminology", "ニイロク", "「Tôi là một món hàng lỗi, một kẻ hỏng hóc.\\nĐã đánh mất \\x%l整備体;#00ffc040;thân bảo trì%l;#;, và cũng mất luôn cả biểu cảm trên khuôn mặt.」"),
"2327": ("pronoun", "双鉄", "「Vì vậy, tôi không muốn giẫm lên nó bằng giày bẩn mà không có lý do chính đáng.\\nCho dù trọng lượng của tôi hay Kisaki có không gây ra ảnh hưởng hay thay đổi gì đi chăng nữa.」"),
"2339": ("pronoun", "双鉄", "「Bẩn tay cô thì tiếc lắm.\\nNếu không phiền, cô dùng cái này đi.」"),
"2341": ("pronoun", "双鉄", "「Xin lỗi. Tôi uống cạn mất rồi.」"),
"2351": ("terminology", "双鉄", "「Đường sắt――Hinomoto.」"),
"2353": ("terminology", "双鉄", "「Đường sắt――Hinomoto.」"),
"2354": ("terminology", "稀咲", "「Đường sắt Hinomoto.」"),
"2361": ("pronoun", "稀咲", "「Người hỗ trợ em, lại chính là cậu đấy? Soutetsu.」"),
"2408": ("pronoun", "双鉄", "「Vậy sao, trông tôi hạnh phúc lắm à.」"),
"2436": ("pronoun", "双鉄", "「Đó chính xác là điều tôi mong muốn.」"),
"2443": ("pronoun", "双鉄", "「Tôi không rõ tình hình ở các địa phương khác――\\nNhưng ít nhất ở Kyushu thì có vẻ là không còn nơi nào sản xuất nữa.」"),
"2453": ("pronoun", "稀咲", "「Không sao đâu. Trà vẫn còn nhiều mà.\\nNếu cậu thích, em pha ấm mới nhé?」"),
"2537": ("pronoun", "稀咲", "「Đúng là hơi sớm thật. Thật tốt khi gặp cậu ở đây.\\nChúng ta có thể tận dụng năm phút này một cách có ý nghĩa.」"),
"2548": ("pronoun", "双鉄", "「Nếu chỉ ở mức độ đó thì không sao cả――nhưng,\\nvì liên quan đến an toàn nên cô cẩn thận như vậy cũng tốt.」"),
"2573": ("pronoun", "双鉄", "「Tôi rất vui vì đã giúp được cô.」"),
"2581": ("pronoun", "双鉄", "「Sự thay đổi hành động——của tôi á?」"),
"2599": ("pronoun", "双鉄", "「Có khi thứ đó đã tồn tại rồi cũng nên.\\nChỉ là tôi không biết, và Đường sắt Ohito cũng không có thôi.」"),
"2604": ("pronoun", "双鉄", "「Cảm ơn cô.」"),
"2605": ("pronoun", "稀咲", "「Thật tốt khi cậu đã dẫn em đến đây và cho em thấy thực tế.\\nNếu không có điều đó, em đã không thể nảy ra ý tưởng này.」"),
"2623": ("pronoun", "稀咲", "「Nói chuyện với cậu, cảm giác như các bánh răng khớp vào nhau vậy, rất dễ chịu.」"),
"2660": ("pronoun", "稀咲", "「Và nó hợp với nhân đậu đỏ đến mức kỳ diệu.\\nUống cùng sữa hay uống không đều ngon, cậu chọn gì?」"),
"2678": ("pronoun", "稀咲", "「Cả cái này nữa. Cậu cứ tự nhiên nhé?」"),
"2681": ("pronoun", "稀咲", "「Vậy, cho đến tối nay. Cậu có thể ở lại với em thêm chút nữa được không?\\nEm muốn hoàn thành luôn bản tóm tắt kế hoạch kinh doanh này.」"),
"2704": ("pronoun", "双鉄", "「Vậy, tôi không khách sáo nhé.」"),
"2708": ("pronoun", "双鉄", "「Nếu vậy thì tôi không khách sáo nhé.」"),
"2709": ("pronoun", "双鉄", "「Vậy cho tôi uống không đi.」"),
"2714": ("pronoun", "双鉄", "「Đằng kia, cô có thấy đường ray trông như bị lún xuống không?」"),
}

rows = {}
with open('sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        if row['File'].split(chr(92))[-1] == 'グランドリライト06_稀咲.txt.toml':
            rows[row['Key']] = row

assert set(FIX) <= set(rows), set(FIX) - set(rows)
out = []
for k in sorted(FIX, key=int):
    kind, ch, fix = FIX[k]
    r = rows[k]
    assert ch == r['Character'], (k, ch, r['Character'])
    out.append({"key": k, "jp": r['JP Original'], "tw": r['TW Original/Current'],
                "old_vn": r['Vietnamese'], "fix": fix, "kind": kind, "character": ch})
json.dump(out, open('audit-grand06-kisaki-wrong.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print("JSON entries:", len(out))

# TOML block (raw text): escape backslash and double-quote; values are single-line.
def toml_esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')
lines = ['[script]']
for e in out:
    lines.append(f'"{e["key"]}" = "{toml_esc(e["fix"])}"')
block = '\n'.join(lines)
open('work-grand06-tomlblock.txt', 'w', encoding='utf-8').write(block)
print("TOML block lines:", len(lines))

# Verification
import tomllib
parsed = tomllib.loads(block)
assert len(parsed['script']) == len(out), (len(parsed['script']), len(out))
mism = [(e['key']) for e in out if parsed['script'][e['key']] != e['fix']]
print("TOML value mismatches:", mism)

# Diff-sanity: fix differs from old_vn only in targeted words
import difflib
for e in out:
    a, b = e['old_vn'], e['fix']
    sm = difflib.SequenceMatcher(None, a, b)
    ratio = sm.ratio()
    if ratio < 0.80:
        print("LOW-RATIO", e['key'], round(ratio, 2))
print("diff-sanity done")
# jp/tw/old_vn vs CSV3: trivially true by construction; re-verify from file
recheck = json.load(open('audit-grand06-kisaki-wrong.json', encoding='utf-8'))
bad = [e['key'] for e in recheck if rows[e['key']]['JP Original'] != e['jp'] or rows[e['key']]['TW Original/Current'] != e['tw'] or rows[e['key']]['Vietnamese'] != e['old_vn']]
print("CSV3 mismatches:", bad)
from collections import Counter
print(Counter(e['kind'] for e in out))
print("keys as strings:", all(isinstance(e['key'], str) for e in out))
