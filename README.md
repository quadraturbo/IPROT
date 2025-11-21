# 🔄 IPROT

<div align="center">

```
██╗██████╗ ██████╗  ██████╗ ████████╗
██║██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║██████╔╝██████╔╝██║   ██║   ██║   
██║██╔═══╝ ██╔══██╗██║   ██║   ██║   
██║██║     ██║  ██║╚██████╔╝   ██║   
╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   
```

**Automated Public IP Rotation Tool via TOR**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)]()
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)]()
[![TOR](https://img.shields.io/badge/Powered%20by-TOR-7D4698.svg)](https://www.torproject.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Requirements](#-requirements) • [Disclaimer](#-disclaimer)

</div>

---

##   Overview

**IPROT** is a lightweight, cross-platform Python script that automatically rotates your public IP address at configurable intervals using the TOR network. Designed with operational security (OPSEC) in mind, it provides a simple yet effective solution for maintaining anonymity online.

## Features

-  **Automatic IP Rotation** - Change your public IP at custom intervals
-  **Cross-Platform** - Works seamlessly on Windows and Linux
-  **Simple Interface** - Minimal configuration required
-  **OPSEC Focused** - Routes traffic through TOR network
-  **Real-time Monitoring** - Displays current IP before and after rotation
-  **Lightweight** - No heavy dependencies or complex setup
-  **Privacy First** - No data collection or logging

##  Quick Start

```bash
git clone https://github.com/quadraturbo/iprot.git
cd iprot
python iprot.py
```

##   Requirements

### Core Dependencies
- Python 3.7+
- TOR
- curl
- netcat (nc)

### Installation by Platform

<details>
<summary><b>🐧 Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt update
sudo apt install tor curl netcat
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b>🐧 Linux (Fedora)</b></summary>

```bash
sudo dnf install tor curl nc
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b>🐧 Linux (Arch)</b></summary>

```bash
sudo pacman -S tor curl gnu-netcat
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b> Windows</b></summary>

**Option 1: TOR Expert Bundle**
1. Download from [torproject.org](https://www.torproject.org/download/tor/)
2. Extract and add to PATH
3. Install curl and netcat

**Option 2: Package Managers**
```powershell
# Chocolatey
choco install tor curl netcat

# Scoop
scoop install tor curl netcat
```
</details>

##   Usage

1. **Run the script:**
   ```bash
   python iprot.py
   ```

2. **Select your OS:**
   ```
   1. Windows
   2. Linux
   ```

3. **Set rotation interval:**
   ```
   Enter interval in seconds: 30
   ```

4. **Monitor rotations:**
   ```
   [0] IP actual: 185.220.101.45
   [*] Rotando IP...
   [✓] Nueva IP: 198.98.57.207
   ```

5. **Stop the script:**
   - Press `Ctrl+C` to gracefully exit

##  Use Cases

- **Privacy Research** - Test anonymity tools and techniques
- **Web Scraping** - Avoid IP-based rate limiting
- **Security Testing** - Test geo-blocking and IP restrictions
- **Development** - Test multi-region functionality
- **OSINT Operations** - Maintain anonymity during investigations

##  Configuration

The script is configured through interactive prompts:

| Parameter | Description | Default |
|-----------|-------------|---------|
| OS Type | Windows or Linux | Interactive |
| Rotation Interval | Seconds between IP changes | User defined |
| TOR Port | SOCKS5 proxy port | 9050 |
| Control Port | TOR control port | 9051 |

##  Screenshots

```
[0] IP actual: 185.220.101.45
[*] Rotando IP...
[✓] Nueva IP: 198.98.57.207

[1] IP actual: 198.98.57.207
[*] Rotando IP...
[✓] Nueva IP: 91.216.79.178
```

##  Security Considerations

- All traffic is routed through TOR SOCKS5 proxy (127.0.0.1:9050)
- No logs are stored locally or remotely
- Script requires TOR control port (9051) for rotation
- Ensure TOR is properly configured before use
- Consider additional OPSEC measures for sensitive operations

##  Troubleshooting

<details>
<summary><b>TOR not detected</b></summary>

Ensure TOR is installed and in your system PATH. Follow the installation guide for your platform.
</details>

<details>
<summary><b>IP not rotating</b></summary>

Check that:
- TOR service is running
- Port 9051 is accessible
- Firewall allows connections to 127.0.0.1:9051
</details>

<details>
<summary><b>Connection errors</b></summary>

Verify:
- TOR is running: `ps aux | grep tor` (Linux) or Task Manager (Windows)
- curl is installed and working
- netcat is available
</details>

##  Disclaimer

This tool is provided for **educational and research purposes only**. Users are responsible for complying with all applicable laws and regulations in their jurisdiction. The authors assume no liability for misuse or damage caused by this software.

**Use responsibly and ethically.**

##  Contributing

Contributions are welcome! Feel free to:

-  Report bugs
-  Suggest features
-  Submit pull requests
-  Improve documentation


##  Acknowledgments

- [The TOR Project](https://www.torproject.org/) for providing the anonymity network
- The open-source community for inspiration and tools

---

<div align="center">

**[⬆ Back to Top](#-iprot)**

Made with ❤️ for privacy enthusiasts (and for practice!!) 

</div>
