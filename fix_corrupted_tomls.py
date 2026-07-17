import os
import re

def fix_toml_file(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # We need to find double quoted strings like key = "value"
    # where value contains literal newlines, and replace literal newlines with \n.
    # TOML string pattern (simple regex for key = "value" where value can span multiple lines if it was corrupted)
    # The pattern matches: key = " ... "
    # But since it contains literal newlines, we can find all matches of double quotes.
    
    # Let's parse line by line to detect unfinished strings, or write a state machine.
    # A state machine is much safer for this!
    
    new_chars = []
    in_quotes = False
    escape = False
    
    i = 0
    while i < len(content):
        c = content[i]
        
        if in_quotes:
            if escape:
                new_chars.append(c)
                escape = False
            elif c == '\\':
                new_chars.append(c)
                escape = True
            elif c == '"':
                new_chars.append(c)
                in_quotes = False
            elif c == '\n':
                # Literal newline inside double quotes! Escape it!
                new_chars.append('\\')
                new_chars.append('n')
            elif c == '\r':
                # Literal carriage return inside double quotes! Escape it!
                new_chars.append('\\')
                new_chars.append('r')
            else:
                new_chars.append(c)
        else:
            new_chars.append(c)
            # We only enter quotes if we see double quotes, but we should make sure it's part of a value
            # Actually, just tracking double quotes is enough since comments don't have unclosed double quotes with newlines.
            if c == '"':
                # Check if it is a triple quote (TOML multiline string). We don't want to escape those.
                # But this VN TOML doesn't use triple quotes for translation values.
                in_quotes = True
                
        i += 1
        
    fixed_content = "".join(new_chars)
    if fixed_content != content:
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write(fixed_content)
        print(f"Fixed literal newlines in: {file_path}")

def main():
    target_dir = r"E:\MaitetsuProject\translation_toml"
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".toml"):
                fix_toml_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
