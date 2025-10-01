import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Send HTTP request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Example: extract all links
links = []
for a_tag in soup.find_all("a", href=True):
    links.append(a_tag["href"])

print("Found links:")
for link in links:
    print(link)
