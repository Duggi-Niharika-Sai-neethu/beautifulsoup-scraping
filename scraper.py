import requests
from bs4 import BeautifulSoup

# Wikipedia page URL for Albert Einstein
url = "https://en.wikipedia.org/wiki/Albert_Einstein"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"Page Title: {soup.find('h1').text}\n")
    print("Section Titles:")

    for header in soup.find_all(['h2', 'h3']):
        span = header.find('span', class_='mw-headline')
        if span:
            print(" -", span.text)
        else:
            header_text = header.get_text(strip=True)
            if header_text and 'edit' not in header_text.lower():
                print(" -", header_text)
else:
    print("Failed to fetch page:", response.status_code)