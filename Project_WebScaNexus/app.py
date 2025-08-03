from flask import Flask, render_template, request, send_from_directory
from scanner.scanner_engine import run_scan
from scanner.exporter import export_to_csv, export_to_pdf
import os

app = Flask(__name__)
last_report_file = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global last_report_file
    if request.method == 'POST':
        url = request.form['url']
        selected_vulns = request.form.getlist('vulns')
        findings = run_scan(url, selected_vulns)
        last_report_file = export_to_csv(findings)
        pdf_file = export_to_pdf(findings)
        return render_template('scan_results.html', url=url, findings=findings, report_file=last_report_file, pdf_file=pdf_file)
    return render_template('index.html')

@app.route('/download/<filename>')
def download_report(filename):
    return send_from_directory('reports', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
