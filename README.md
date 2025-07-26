# 🛡️ WebScanner - Web Vulnerability Scanner

A lightweight Python-based tool for scanning websites for common security vulnerabilities such as-
**SQL Injection (SQLi)**
**Cross-Site Scripting (XSS)*
**insecure HTTP headers**.
This tool helps identify potential entry points in web applications and supports ethical hacking and penetration testing workflows.

---

## 🚀 Features

- 🔍 **Automatic Vulnerability Detection**
  - Detects **XSS**, **SQL Injection**, and **CSRF** vulnerabilities using crafted payloads
- 🌐 **URL Crawler**
  - Recursively crawls target websites to extract all links and form endpoints
- 🧠 **Intelligent Scanning**
  - Analyzes and injects payloads into `GET`, `POST`, and form input fields
- 🛡️ **CSRF Detection**
  - Flags potential CSRF risks by checking for anti-CSRF token mechanisms
- 🔒 **HTTP Header Analysis**
  - Identifies missing or misconfigured security headers (e.g., CSP, X-Frame-Options)
- 📝 **Detailed Reporting**
  - Saves raw scan data in `JSON` format and generates clean **HTML** reports
- ⚙️ **Custom Scan Modes**
  - Supports `non-intrusive` mode (safe XSS/CSRF-only scanning) and full `intrusive` mode (includes SQLi)
- 📁 **Organized Output**
  - Stores structured results under `output_reports/` and `generated_reports/`
- 🎯 **Command-line Flexibility**
  - Modular CLI with optional flags for choosing specific vulnerability scans
- 💡 **Future Extensibility**
  - Designed to be extended with more payloads and scan types in the future

---

## 🧰 Technologies Used

- Python 3
- `requests`
- `BeautifulSoup4`
- `re` (Regex)

---

## 🧭 Flag Summary

| Script                          | Flag                        | Description                                   |
| ------------------------------- | --------------------------- | --------------------------------------------- |
| `vulnerability.py`              | `--non-intrusive`           | Only XSS & CSRF scan                          |
|                                 | `--sqli`, `--xss`, `--csrf` | Individually enable scanning modules          |
| `report_generator.py`           | `--html`                    | Generate HTML report                          |
|                                 | `--nonintrusive`            | Include only reports from non-intrusive scans |
|                                 | `--intrusive`               | Include only reports from intrusive scans     |


## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshlad07/WebScanner.git
   cd WebScanner

## ⚠️ Disclaimer
    Use this tool only on web applications for which you have explicit authorization. Misuse may be illegal and unethical.

## 🧠 Credits & License
    Created by Harsh Lad
    License: MIT
    Supported Python modules: requests, beautifulsoup4, argparse, html
