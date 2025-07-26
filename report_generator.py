import os
import json
import argparse
from datetime import datetime
from pathlib import Path
import html

REPORT_DIR = "output_reports"
OUTPUT_DIR = "generated_reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_all_json():
    combined = []
    for file in os.listdir(REPORT_DIR):
        if file.endswith(".json"):
            path = os.path.join(REPORT_DIR, file)
            with open(path, 'r') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        combined.extend(data)
                    else:
                        combined.append(data)
                except Exception as e:
                    print(f"Error loading {file}: {e}")
    return combined

def generate_html(data, scan_mode_filter=None):
    html_content = """
    <html>
    <head>
        <title>Web Vulnerability Scan Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            h1 {
                color: #d9534f;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 40px;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            .report-block {
                margin-bottom: 60px;
            }
        </style>
    </head>
    <body>
        <h1>Combined Web Vulnerability Scan Report</h1>
    """

    for report in data:
        if scan_mode_filter and report.get("Scan Mode") != scan_mode_filter:
            continue

        html_content += "<div class='report-block'>"
        html_content += f"<h2>Report</h2>"
        html_content += f"<p><strong>Test Type:</strong> {report.get('Test Type', 'N/A')}</p>"
        html_content += f"<p><strong>Scan Mode:</strong> {report.get('Scan Mode', 'N/A')}</p>"
        html_content += f"<p><strong>Forms Found:</strong> {report.get('Forms Found', 'N/A')}</p>"
        html_content += f"<p><strong>Crawled URLs:</strong> {', '.join(report.get('Crawled URLs', []))}</p>"

        vulnerabilities = report.get("Vulnerabilities", [])
        html_content += f"<h3>Detected Vulnerabilities ({len(vulnerabilities)})</h3>"

        if report.get("Test Type") == "XSS":
            html_content += "<table><tr><th>#</th><th>URL</th><th>Payload</th></tr>"
            for idx, vuln in enumerate(vulnerabilities, 1):
                url = html.escape(vuln.get("url", "N/A"))
                payload = html.escape(str(vuln.get("payload", "N/A")))
                html_content += f"<tr><td>{idx}</td><td>{url}</td><td><code>{payload}</code></td></tr>"
            html_content += "</table>"

        elif report.get("Test Type") == "CSRF":
            html_content += "<table><tr><th>#</th><th>URL</th></tr>"
            for idx, vuln in enumerate(vulnerabilities, 1):
                url = html.escape(vuln.get("url", "N/A"))
                html_content += f"<tr><td>{idx}</td><td>{url}</td></tr>"
            html_content += "</table>"

        else:
            html_content += "<p>No known Test Type handler.</p>"

        html_content += "</div>"

    html_content += "</body></html>"
    return html_content, url

def save_file(content, url, ext):
    final_url = (url.split("https://")[1].split(".org")[0])
    filename = f"scan_report_{final_url}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Report saved: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Generate readable reports from scan results.")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")
    parser.add_argument("--nonintrusive", action="store_true", help="Only include non-intrusive scan results")
    parser.add_argument("--intrusive", action="store_true", help="Only include intrusive scan results")
    args = parser.parse_args()

    data = load_all_json()

    scan_mode_filter = None
    if args.nonintrusive:
        scan_mode_filter = "non-intrusive"
    elif args.intrusive:
        scan_mode_filter = "intrusive"

    if args.html:
        html_content,url = generate_html(data, scan_mode_filter=scan_mode_filter)
        save_file(html_content, url, "html")

if __name__ == "__main__":
    main()
