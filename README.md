# Linux System Monitor (Root Dashboard) 🚀

A lightweight, real-time web dashboard for Linux VPS/VDS monitoring. Built with **FastAPI** and **psutil**, featuring a mobile-responsive Cyberpunk-style UI.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100%2B-05998b)

## ✨ Features
- **Real-time Metrics:** CPU load, RAM usage, and Network I/O (MB/s).
- **Root Access Insights:** Hardware temperatures and system logs (`dmesg`).
- **Process Management:** Built-in Process Manager with the ability to `KILL` tasks directly from the UI.
- **Mobile First:** Fully responsive design works perfectly on both Desktop and Mobile devices.
- **Lightweight:** No heavy databases or complex setups required.

## 🛠 Tech Stack
- **Backend:** Python, FastAPI, Uvicorn.
- **System Layer:** Psutil (Process and System Utilities).
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API).

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/lixynhay/system-monitor.git](https://github.com/lixynhay/system-monitor.git)
cd system-monitor

### 2. Install dependencies
```bash
pip install -r requirements.txt

### 3. Run the server
```bash
sudo python3 main.py
