***WebScaNexus***

WebScaNexus is a web vulnerability scanner built with Flask. It scans target URLs for common vulnerabilities such as SQL Injection (SQLi), Cross Site Scripting (XSS), and Cross Site Request Forgery (CSRF). Scan results are presented in a user-friendly web interface and can be exported as CSV or PDF reports.

## Features

- Scan for SQLi, XSS, and CSRF vulnerabilities
- Automatic form detection and payload injection
- Evidence and severity reporting for each finding
- Export scan results to CSV and PDF
- Simple web UI built with Bootstrap

### Prerequisites

- Python 3.7+
- pip

### Running the Application

Start the Flask server:
```sh
python app.py
```
Visit `http://localhost:5000` in your browser.

## Usage

1. Enter the target URL in the form.
2. Select vulnerabilities to scan.
3. Click "Start Scan" to begin.
4. View results and download reports.

## Project Structure

- `app.py` - Main Flask application
- `scanner/` - Scanning engine, payloads, crawler, detector, exporter
- `templates/` - HTML templates for UI
- `reports/` - Generated scan reports

## Results

<img width="1891" height="967" alt="image" src="https://github.com/user-attachments/assets/c61175e9-2ac3-4d56-bc3a-79a37ce2757a" />
<img width="1878" height="973" alt="image" src="https://github.com/user-attachments/assets/697a30b2-7d53-43b9-b6ae-9399fc32f3bb" />
<img width="1869" height="968" alt="image" src="https://github.com/user-attachments/assets/47bee353-a640-4f72-a948-7490cf83d2fb" />
