import requests
from bs4 import BeautifulSoup

# URL of the news website (example: BBC)
url = "https://www.bbc.com/news"

# Fetch HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines (adjust tags if needed)
headlines = soup.find_all(["h2", "h3"])

# Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headlines:
        title = h.get_text(strip=True)
        if title:
            file.write(title + "\n")

print("✅ Headlines saved to 'headlines.txt'")