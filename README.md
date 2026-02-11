# 🔎 Python Port Scanner

A simple TCP port scanner written in Python for educational purposes.

---

## 📚 Educational Purpose

This project was created strictly for learning and educational use.

Its goal is to better understand:

- TCP socket communication
- Port states (open / closed)
- Network enumeration fundamentals
- Error handling in network programming
- Basic reconnaissance concepts

This tool is part of my cybersecurity learning journey as an IT student.

---

## ⚙️ Features

- Scan custom port ranges
- Timeout handling
- Detection of open TCP ports
- Clean and modular structure for further development

---

## 🚀 Usage

```bash
python scanner.py
```

---


You will be prompted to enter:

- Target IP address or hostname  
- Start port  
- End port  

Example:

```
Enter target IP or hostname: 127.0.0.1
Start port: 20
End port: 100
```

The scanner will attempt to connect to each port in the given range
and display open ports in the terminal.

---

## 🧠 How It Works

The scanner:

- Creates a TCP socket connection  
- Attempts to connect to each port in a specified range  
- Uses a timeout to avoid hanging on unresponsive ports  
- Reports ports that respond successfully  

This approach simulates basic network enumeration techniques used in security testing.

---

## 🚧 Future Improvements

Planned improvements:

- Multithreaded scanning for better performance  
- CLI argument support  
- Basic service detection (banner grabbing)  
- Improved error handling  
- Logging results to a file  

---

## ⚠️ Disclaimer

This software is provided for educational purposes only.

Do not use this tool against systems, networks, or devices without explicit permission from the owner.

The author is not responsible for any misuse or damage caused by this program.

Always follow applicable laws and ethical guidelines.
