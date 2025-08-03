import requests
from .crawler import get_forms, get_form_details
from .payloads import PAYLOADS
from .detector import detect_vulnerability

def run_scan(url, selected_vulns):
    forms = get_forms(url)
    findings = []

    severity_map = {
        "SQLi": "High",
        "XSS": "Medium",
        "CSRF": "High",
        "Command Injection": "Critical"
    }

    for form in forms:
        form_details = get_form_details(form, url)

        for vuln_type in selected_vulns:
            for payload in PAYLOADS.get(vuln_type, []):
                data = {input_field["name"]: payload for input_field in form_details["inputs"]}
                try:
                    if form_details["method"] == "post":
                        response = requests.post(form_details["action"], data=data)
                    else:
                        response = requests.get(form_details["action"], params=data)

                    if detect_vulnerability(response, vuln_type, payload):
                        findings.append({
                            "vulnerability": vuln_type,
                            "payload": payload,
                            "url": form_details["action"],
                            "param_names": [i["name"] for i in form_details["inputs"]],
                            "method": form_details["method"],
                            "evidence": response.text[:300],
                            "severity": severity_map.get(vuln_type, "Low")
                        })
                except Exception as e:
                    print(f"[!] Request failed: {e}")
                    print("Scanning:", form_details)
                    print("Submitting payload:", payload)
                    print("Response:", response.status_code, response.text[:300])

    return findings
