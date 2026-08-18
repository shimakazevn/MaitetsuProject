import csv

p = r"E:\まいてつ Last Run!!\tools\sample_translation.tsv"
with open(p, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        if row.get('line_id') == '1':
            print("Row 1 keys and values:")
            for k, v in row.items():
                print(f"  {k}: {v.encode('ascii', errors='replace').decode('ascii')}")
        elif row.get('line_id') == '0':
            print("Row 0 keys and values:")
            for k, v in row.items():
                v_str = v.encode('ascii', errors='replace').decode('ascii') if v is not None else 'None'
                print(f"  {k}: {v_str}")
