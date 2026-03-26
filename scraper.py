# import requests
# from bs4 import BeautifulSoup

# urls = [
#     "https://bankofmaharashtra.bank.in/personal-banking/loans/home-loan",
#     "https://bankofmaharashtra.bank.in/personal-banking/loans/personal-loan",
#     "https://bankofmaharashtra.bank.in/personal-loan-for-salaried-customers"
# ]

# def scrape_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     for script in soup(["script", "style"]):
#         script.extract()

#     text = soup.get_text(separator=" ")
#     return text

# all_text = ""

# for url in urls:
#     print(f"Scraping: {url}")
#     all_text += scrape_page(url) + "\n\n"

# with open("data/raw/loans.txt", "w", encoding="utf-8") as f:
#     f.write(all_text)

# print("✅ Scraping completed")

import requests
from bs4 import BeautifulSoup
import time
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

urls = [
    "https://bankofmaharashtra.bank.in/personal-banking/loans/home-loan",
    "https://bankofmaharashtra.bank.in/personal-banking/loans/personal-loan",
    "https://bankofmaharashtra.bank.in/personal-loan-for-salaried-customers"
]

def scrape_page(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ")
        return text

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return ""

# ✅ create folder automatically
os.makedirs("data", exist_ok=True)

all_text = ""

# ✅ THIS is where your loop + time.sleep goes
for url in urls:
    print(f"Scraping: {url}")
    
    page_text = scrape_page(url)
    all_text += page_text + "\n\n"
    
    time.sleep(2)   # 👈 important

# ✅ save file
with open("data/loans.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("✅ Scraping completed")