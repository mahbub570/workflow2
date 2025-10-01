import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Send HTTP request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
