import csv

p = r"E:\まいてつ Last Run!!\tools\sample_translation.tsv"
with open(p, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        line_id = row.get('line_id')
        jp = row.get('jp_text', '')
        vn = row.get('vn_text', '')
        if vn:
            safe_jp = jp.encode('ascii', errors='replace').decode('ascii')
            safe_vn = vn.encode('ascii', errors='replace').decode('ascii')
            print(f"Line {line_id}: JP='{safe_jp}' -> VN='{safe_vn}'")
