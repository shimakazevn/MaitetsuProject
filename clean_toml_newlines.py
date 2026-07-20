import os
import re

toml_dir = r"E:\MaitetsuProject\translation_toml"
modified_count = 0
total_replaced = 0
LENGTH_THRESHOLD = 55  # Only remove newlines if total length of the string is > 55 characters

log_lines = []

for root, dirs, files in os.walk(toml_dir):
    for file in files:
        if not file.endswith(".toml"):
            continue
        filepath = os.path.join(root, file)
        
        # Read the file
        content = ""
        encoding_used = 'utf-8'
        for encoding in ['utf-8', 'utf-16le', 'shift-jis']:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    content = f.read()
                encoding_used = encoding
                break
            except Exception:
                continue
        
        if not content:
            continue
            
        lines = content.splitlines()
        file_modified = False
        
        for idx, line in enumerate(lines):
            # Check if line matches a translation entry (e.g. 3319 = "...")
            match = re.match(r"^(\d+)\s*=\s*\"(.*)\"\s*$", line)
            if match:
                key = match.group(1)
                val = match.group(2)
                
                # Check if literal \n exists in the translation value
                if "\\n" in val:
                    # Check length of the text (after unescaping or basic count)
                    # We just count characters in the string value
                    total_len = len(val)
                    if total_len > LENGTH_THRESHOLD:
                        orig_val = val
                        # Replace \n with space
                        val = val.replace("\\n", " ")
                        # Clean up double spaces that might result
                        val = re.sub(r"\s+", " ", val)
                        # Reconstruct the line
                        lines[idx] = f'{key} = "{val}"'
                        
                        file_modified = True
                        total_replaced += 1
                        log_lines.append(f"[{file}] Line {key} (Len {total_len} > {LENGTH_THRESHOLD}):\n  OLD: {orig_val}\n  NEW: {val}\n")
        
        if file_modified:
            modified_count += 1
            # Write back
            with open(filepath, 'w', encoding=encoding_used) as f:
                f.write("\n".join(lines) + "\n")

# Write log results
log_path = r"C:\Users\Shimakaze\.gemini\antigravity-ide\scratch\clean_newlines_log.txt"
with open(log_path, 'w', encoding='utf-8') as f:
    f.write(f"Length Threshold: {LENGTH_THRESHOLD}\n")
    f.write(f"Total files modified: {modified_count}\n")
    f.write(f"Total entries cleaned: {total_replaced}\n\n")
    f.write("\n".join(log_lines))

print(f"Successfully cleaned newlines! Modified {modified_count} files, replaced {total_replaced} entries (Threshold: {LENGTH_THRESHOLD}).")
