import json

import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

BASE_URL = "https://demowebshop.tricentis.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}


def post(path, data=None, cookies=None):
    url = BASE_URL + path
    with step(f"POST {url}"):
        response = requests.post(url, data=data, headers=HEADERS, cookies=cookies)

        try:
            body = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except:
            body = response.text

        allure.attach(body, "Response", AttachmentType.JSON)
        return response
