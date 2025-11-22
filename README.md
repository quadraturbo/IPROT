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
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![TOR](https://img.shields.io/badge/Powered%20by-TOR-7D4698.svg)](https://www.torproject.org/)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Effective Usage](#effective-usage) • [Requirements](#requirements) • [Disclaimer](#disclaimer)

</div>

---

## Overview

**IPROT** is a lightweight, cross-platform Python script that automatically rotates your public IP address at configurable intervals using the TOR network. Designed with operational security (OPSEC) in mind, it provides a simple yet effective solution for maintaining anonymity online.

## Features

- **Automatic IP Rotation** - Change your public IP at custom intervals
- **Cross-Platform** - Works seamlessly on Windows and Linux
- **Simple Interface** - Minimal configuration required
- **OPSEC Focused** - Routes traffic through TOR network
- **Real-time Monitoring** - Displays current IP before and after rotation
- **Lightweight** - No heavy dependencies or complex setup
- **Privacy First** - No data collection or logging

## Quick Start

```bash
git clone https://github.com/quadraturbo/IPROT.git
cd IPROT
python iprot.py
```

## Requirements

### Core Dependencies
- Python 3.7+
- TOR
- curl
- netcat (nc)

### Installation by Platform

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt update
sudo apt install tor curl netcat
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b>Linux (Fedora)</b></summary>

```bash
sudo dnf install tor curl nc
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b>Linux (Arch)</b></summary>

```bash
sudo pacman -S tor curl gnu-netcat
sudo systemctl start tor
sudo systemctl enable tor
```
</details>

<details>
<summary><b>Windows</b></summary>

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

## Usage

### Running IPROT

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

## Effective Usage

**IMPORTANT:** IPROT rotates your IP within the TOR network, but your applications won't automatically use it. You need to configure them to route traffic through TOR's SOCKS5 proxy at `127.0.0.1:9050`.

### Web Browsing Setup

#### Option 1: Proxychains (Linux - Recommended)

```bash
# Install proxychains
sudo apt install proxychains4

# Configure it (one-time setup)
sudo nano /etc/proxychains4.conf
# Make sure this line exists at the end:
socks5 127.0.0.1 9050

# Launch your browser through TOR
proxychains4 firefox
proxychains4 chromium
```

#### Option 2: Browser Configuration (All Platforms)

**Firefox:**
1. Settings → Network Settings → Settings
2. Select "Manual proxy configuration"
3. SOCKS Host: `127.0.0.1` Port: `9050`
4. Select "SOCKS v5"
5. Enable "Proxy DNS when using SOCKS v5"

**Chrome/Chromium (Linux):**
```bash
chromium --proxy-server="socks5://127.0.0.1:9050"
```

**Chrome (Windows):**
```cmd
chrome.exe --proxy-server="socks5://127.0.0.1:9050"
```

### Running Commands Through TOR

#### Using Proxychains (Recommended)

```bash
# Web requests
proxychains4 curl https://example.com
proxychains4 wget https://file.zip

# Network scanning (use responsibly)
proxychains4 nmap -sT target.com
proxychains4 whatweb https://example.com

# Python scripts
proxychains4 python3 your_script.py

# Any command line tool
proxychains4 <your-command>
```

#### Using Torsocks (Alternative)

```bash
# Install torsocks
sudo apt install torsocks

# Use with any command
torsocks curl ifconfig.me
torsocks wget https://example.com
torsocks python3 script.py
torsocks ssh user@host
```

#### Manual SOCKS5 Configuration

**curl:**
```bash
curl --socks5-hostname 127.0.0.1:9050 https://ifconfig.me
curl -x socks5h://127.0.0.1:9050 https://api.example.com
```

**wget:**
```bash
wget -e use_proxy=yes -e http_proxy=socks5h://127.0.0.1:9050 https://file.zip
```

**Python requests:**
```python
import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

response = requests.get('https://ifconfig.me', proxies=proxies)
print(response.text)
```

**Git:**
```bash
git config --global http.proxy socks5h://127.0.0.1:9050
git clone https://github.com/user/repo.git
git config --global --unset http.proxy  # Remove when done
```

### Verify You're Using TOR

**Web verification:**
- Visit https://check.torproject.org - Should say "Congratulations. This browser is configured to use Tor"
- Visit https://ifconfig.me - Should show a TOR exit node IP (different from your real IP)

**Command line verification:**
```bash
# Your real IP
curl ifconfig.me

# TOR IP (should be different)
curl --socks5-hostname 127.0.0.1:9050 ifconfig.me

# Or with proxychains
proxychains4 curl ifconfig.me
```

### Complete Workflow Example

```bash
# Terminal 1: Start IPROT
python3 iprot.py
# Select OS, set rotation interval (e.g., 60 seconds)

# Terminal 2: Use TOR for your tasks
proxychains4 curl ifconfig.me
# Wait 60 seconds...
proxychains4 curl ifconfig.me  # Different IP!

# Or launch browser
proxychains4 firefox
```

## Use Cases

- **Privacy Research** - Test anonymity tools and techniques
- **Web Scraping** - Avoid IP-based rate limiting
- **Security Testing** - Test geo-blocking and IP restrictions
- **Development** - Test multi-region functionality
- **OSINT Operations** - Maintain anonymity during investigations

## Configuration

The script is configured through interactive prompts:

| Parameter | Description | Default |
|-----------|-------------|---------|
| OS Type | Windows or Linux | Interactive |
| Rotation Interval | Seconds between IP changes | User defined |
| TOR Port | SOCKS5 proxy port | 9050 |
| Control Port | TOR control port | 9051 |

## Security Considerations

- All traffic is routed through TOR SOCKS5 proxy (127.0.0.1:9050)
- No logs are stored locally or remotely
- Script requires TOR control port (9051) for rotation
- Ensure TOR is properly configured before use
- Always verify TOR is working before sensitive operations
- Use `proxychains4 -q` for quiet mode (less output)
- IPROT rotates circuits automatically - your IP changes at your chosen interval
- Disable WebRTC in browsers to prevent IP leaks
- Some applications may not work properly through SOCKS5 proxy
- For maximum anonymity, consider using TOR Browser or Tails OS

## Troubleshooting

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
<summary><b>My real IP is still showing</b></summary>

IPROT rotates IPs within TOR, but doesn't route your traffic automatically. You need to:
- Use `proxychains4` before your commands
- Use `torsocks` to wrap applications
- Configure applications to use SOCKS5 proxy (127.0.0.1:9050)

See the [Effective Usage](#effective-usage) section for detailed instructions.
</details>

<details>
<summary><b>Connection errors</b></summary>

Verify:
- TOR is running: `ps aux | grep tor` (Linux) or Task Manager (Windows)
- curl is installed and working
- netcat is available
</details>

## Disclaimer

This tool is provided for **educational and research purposes only**. Users are responsible for complying with all applicable laws and regulations in their jurisdiction. The authors assume no liability for misuse or damage caused by this software.

**Use responsibly and ethically.**

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [The TOR Project](https://www.torproject.org/) for providing the anonymity network
- The open-source community for inspiration and tools

---

<div align="center">

**[⬆ Back to Top](#-iprot)**

Made with ❤️ for privacy enthusiasts (and for practice!!) 

</div>
