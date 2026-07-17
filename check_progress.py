import os
import glob
import sys

def main():
    # Set console encoding to UTF-8
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
        
    # 1. Count completed files
    completed_file = r"E:\まいてつ Last Run!!\gemini_desktop_client\data\completed_files.txt"
    completed_count = 0
    if os.path.exists(completed_file):
        try:
            with open(completed_file, "r", encoding="utf-8") as f:
                completed_count = len([line for line in f if line.strip()])
        except Exception:
            pass
            
    print("="*60)
    print("             MAITETSU TRANSLATION PROGRESS")
    print("="*60)
    print(f" Completed Files : {completed_count} / 216 ({completed_count/216*100:.1f}%)")
    print("="*60)
    
    # 2. Find the latest translation task log
    tasks_dir = r"C:\Users\Shimakaze\.gemini\antigravity-ide\brain\41b99b02-9a8a-4976-8cde-4ad8aea6a3e2\.system_generated\tasks"
    log_files = glob.glob(os.path.join(tasks_dir, "task-*.log"))
    
    translation_logs = []
    for lf in log_files:
        try:
            # Quick check if it is a translation log by checking the first line
            with open(lf, "r", encoding="utf-8") as f:
                first_line = f.readline()
                if "Found" in first_line and "TOML" in first_line:
                    translation_logs.append((os.path.getmtime(lf), lf))
        except Exception:
            pass
            
    if not translation_logs:
        print("No active translation logs found.")
        print("="*60)
        return
        
    translation_logs.sort(reverse=True)
    latest_log = translation_logs[0][1]
    
    print(f" Live Activity Log (Last 15 lines):")
    print("="*60)
    
    try:
        with open(latest_log, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Get the last 15 lines
            last_lines = lines[-15:]
            for line in last_lines:
                print(line.rstrip())
    except Exception as e:
        print(f"Error reading log file: {e}")
        
    print("="*60)

if __name__ == "__main__":
    main()
