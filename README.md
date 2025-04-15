# 🛡️ WebScanner - Web Vulnerability Scanner

A lightweight Python-based tool for scanning websites for common security vulnerabilities such as-
**SQL Injection (SQLi)**
**Cross-Site Scripting (XSS)*
**insecure HTTP headers**.
This tool helps identify potential entry points in web applications and supports ethical hacking and penetration testing workflows.

---

## 🚀 Features

- 🔍 **Automatic Vulnerability Detection**
  - Detects XSS and SQLi by injecting crafted payloads
- 🌐 **URL Crawler**
  - Parses and crawls target web pages to extract links and input parameters
- 🧠 **Intelligent Scanning**
  - Scans GET/POST parameters and HTML forms
- 🔒 **HTTP Header Analysis**
  - Identifies missing or misconfigured security headers
- 📝 **Clean Logging**
  - Provides a clear, color-coded summary of results

---

## 🧰 Technologies Used

- Python 3
- `requests`
- `BeautifulSoup4`
- `re` (Regex)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshlad07/WebScanner.git
   cd WebScanner
