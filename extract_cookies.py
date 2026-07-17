import json
import re
import os

def extract_cookies():
    log_path = r'C:\Users\Shimakaze\.gemini\antigravity-ide\brain\41b99b02-9a8a-4976-8cde-4ad8aea6a3e2\.system_generated\logs\transcript_full.jsonl'
    
    psid = None
    psidts = None
    
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'USER_INPUT' in line:
                try:
                    data = json.loads(line)
                    content = data.get('content', '')
                    matches = re.finditer(r'\[\s*\{.*?\}\s*\]', content, re.DOTALL)
                    for match in matches:
                        try:
                            cookies = json.loads(match.group(0))
                            for cookie in cookies:
                                if cookie.get('name') == '__Secure-1PSID':
                                    psid = cookie.get('value')
                                elif cookie.get('name') == '__Secure-1PSIDTS':
                                    psidts = cookie.get('value')
                        except json.JSONDecodeError:
                            pass
                except json.JSONDecodeError:
                    pass

    print(f"Found __Secure-1PSID: {'Yes' if psid else 'No'}")
    print(f"Found __Secure-1PSIDTS: {'Yes' if psidts else 'No'}")
    
    if psid:
        settings_path = r'E:\まいてつ Last Run!!\gemini_desktop_client\data\settings.json'
        settings = {}
        if os.path.exists(settings_path):
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                pass
                
        settings['__Secure-1PSID'] = psid
        if psidts:
            settings['__Secure-1PSIDTS'] = psidts
            
        os.makedirs(os.path.dirname(settings_path), exist_ok=True)
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4)
        print("Settings saved successfully!")
    else:
        print("Cookies not found.")

if __name__ == '__main__':
    extract_cookies()
