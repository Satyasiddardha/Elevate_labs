import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Error fetching forms: {e}")
        return []

def get_form_details(form, base_url):
    details = {}
    action = form.attrs.get("action", "").strip()
    method = form.attrs.get("method", "get").lower()
    form_url = urljoin(base_url, action)

    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})

    details['action'] = form_url
    details['method'] = method
    details['inputs'] = inputs
    return details
