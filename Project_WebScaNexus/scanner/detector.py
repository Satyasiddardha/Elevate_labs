import re

SQL_ERRORS = [
    r"you have an error in your sql syntax",
    r"warning.*mysql",
    r"unclosed quotation mark",
    r"quoted string not properly terminated",
    r"ORA-01756",
    r"sql error",
    r"mysql_fetch",
    r"mysql_num_rows",
    r"sqlstate"
]
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe src='javascript:alert(\"XSS\")'>",
    "<input type='text' value='XSS' onfocus='alert(\"XSS\")'>"
]


def detect_vulnerability(response, vuln_type, payload):
    content = response.text.lower()

    if vuln_type == "SQLi":
        for error in SQL_ERRORS:
            if re.search(error, content):
                return True

    elif vuln_type == "XSS":
        return payload.lower() in content

    elif vuln_type == "CSRF":
        if response.request.method == "POST":
            has_token = any(token in response.text for token in ["csrf", "_token", "authenticity_token"])
            return not has_token

    return False