# OPRecon Pro 🔍  
**Advanced Network Reconnaissance Suite by `RkineX`⚡**  
*Uncover Hidden Network Insights with Military-Grade Scanning*


---

## 🚀 Features  
### **Core Capabilities**  
| Module | Description | Speed |  
|--------|-------------|-------|  
| **Port Scanner** | Scan all 65,535 ports with threaded optimization | 1,000 ports/sec |  
| **Service Detector** | Identify services/versions via Nmap integration | Auto-paced |  
| **DNS Recon** | Enumerate A, AAAA, MX, NS, TXT, SOA records | Instant |  
| **Web Fingerprint** | Detect web servers, frameworks, cookies | <1 sec |  

### **Advanced Tools**  
🛡️ **Smart Threat Detection**  
- Open vulnerable ports (21/FTP, 22/SSH, 3389/RDP)  
- Outdated service versions (Apache <2.4, Nginx <1.18)  

📊 **Analytics Dashboard**  
- Export results to JSON/CSV  
- Live scanning progress visualization  

🔐 **Safety Protocols**  
- Rate limiting to avoid detection  
- Randomized user-agent rotation  

---

## 🛠 Installation  
**Requirements:**  
- Python 3.8+  
- Root access (for SYN scans)  

```bash
# Clone & Setup  
git clone https://github.com/YourOrg/OPRecon-Pro.git  
cd OPRecon-Pro  

# Install Dependencies  
pip install -r requirements.txt  

# Verify Installation  
python src/cli.py --version
```

## 💡 Usage 

```bash
# Basic Scan
oprecon scan example.com -p 1-1000 -t 500
```
```bash
# Options:
  -p, --ports     Port range (default: 1-1000)
  -t, --threads   Concurrent threads (default: 200)
  -o, --output    Export format (txt/json/csv)
  --stealth       Enable SYN scan (requires root)
  --tor           Route through Tor network
  --api           Enable API integration mode
```
# 📋 Sample Report

```bash
[+] Target: example.com (93.184.216.34)
[+] Scan commenced: 2023-08-20 14:30:00 UTC

PORT     SERVICE    VERSION           CPE
80/tcp   http      nginx 1.18.0     cpe:/a:nginx:nginx:1.18.0
443/tcp  https     nginx 1.18.0     cpe:/a:nginx:nginx:1.18.0 
22/tcp   ssh       OpenSSH 8.2p1    cpe:/a:openbsd:openssh:8.2p1

DNS RECORDS:
A        93.184.216.34
AAAA     2606:2800:220:1:248:1893:25c8:1946
MX       mail.example.com
TXT      "v=spf1 include:_spf.example.com ~all"

WEB TECHNOLOGIES:
Server: nginx/1.18.0
X-Powered-By: PHP/7.4.3
Security-Policy: HSTS=enabled, CSP=strict
```

### **Features Comparison**  
| Feature | Original OPRecon | OPRecon Pro⚡ |  
|--------|-------------|-------|  
| **Scanning Speed** | 5 ports/sec | 1k ports/sec |  
| **Service Detection** | ❌ | ✅ |  
| **DNS Enumeration** | ❌ | ✅ |  
| **Web Fingerprinting** | ❌ | ✅ |  
| **Output Formatting** | Basic Text | Tabular | 

## 🐛 Troubleshooting
```bash
# Resolve dependency conflicts
pip install --force-reinstall -r requirements.txt

# Fix Nmap path issues
export PATH=$PATH:/usr/local/nmap/bin  # Linux/Mac
```

