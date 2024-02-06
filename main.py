import requests
from bs4 import BeautifulSoup
import re

def extract_phone_numbers(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    phone_numbers = re.findall(r'\b8\d{10}\b', text)

    return phone_numbers

url_1 = "https://hands.ru/company/about"
url_2 = "https://repetitors.info"
print("Phone numbers found on", url_1, ":", extract_phone_numbers(url_1))
print("Phone numbers found on", url_2, ":", extract_phone_numbers(url_2))