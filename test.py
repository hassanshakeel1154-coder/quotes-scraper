import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes = []
authors = []

for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)


    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract quotes and authors
    for quote in soup.find_all("span", class_="text"):
        quotes.append(quote.text)

    for author in soup.find_all("small", class_="author"):
        authors.append(author.text)

    print(f"✅ Page {page} scraped successfully!")

# Save data into CSV
df = pd.DataFrame({"Quote": quotes, "Author": authors})
df.to_csv("all_quotes.csv", index=False, encoding="utf-8")

print("🎉 Scraping complete! Data saved in all_quotes.csv")
