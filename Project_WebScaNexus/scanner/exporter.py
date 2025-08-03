import csv
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

REPORT_DIR = "reports"

def export_to_csv(findings, filename=None):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    if not filename:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{now}.csv"

    path = os.path.join(REPORT_DIR, filename)

    with open(path, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Vulnerability", "Payload", "Method", "Param(s)", "URL", "Evidence"])

        for item in findings:
            writer.writerow([
                item["vulnerability"],
                item["payload"],
                item["method"].upper(),
                ", ".join(item["param_names"]),
                item["url"],
                item["evidence"][:200] + "..."
            ])
    return filename

def export_to_pdf(findings, filename=None):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    if not filename:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{now}.pdf"

    path = os.path.join(REPORT_DIR, filename)
    c = canvas.Canvas(path, pagesize=A4)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "WebScaNexus Vulnerability Report")
    c.setFont("Helvetica", 10)
    c.drawString(50, 785, f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 770, f"Findings: {len(findings)} vulnerabilities")

    data = [["Vuln", "Severity", "Payload", "Param(s)", "Method", "URL"]]
    for f in findings:
        data.append([
            f["vulnerability"],
            f["severity"],
            f["payload"],
            ", ".join(f["param_names"]),
            f["method"].upper(),
            f["url"]
        ])

    table = Table(data, colWidths=[70, 60, 100, 80, 50, 140])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.gray),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke)
    ]))

    table.wrapOn(c, 50, 700)
    table.drawOn(c, 50, 500 - (len(findings) * 12))

    c.save()
    return filename