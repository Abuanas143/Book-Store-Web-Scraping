import requests
from bs4 import BeautifulSoup
import re

URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_books():
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()  # 🔥 HTTP errors handle

    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    articles = soup.find_all("article", class_="product_pod")

    for book in articles:
        # 🔹 Title
        title = book.h3.a.get("title", "No title")

        # 🔹 Price (safe)
        price_tag = book.find("p", class_="price_color")
        if price_tag:
            price_text = price_tag.text
            price = float(re.sub(r"[^\d.]", "", price_text))
        else:
            price = None

        # 🔹 Rating (safe)
        rating = "Not rated"
        rating_tag = book.find("p", class_="star-rating")
        if rating_tag:
            classes = rating_tag.get("class", [])
            if len(classes) > 1:
                rating = classes[1]

        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return books


if __name__ == "__main__":
    data = scrape_books()
    for book in data:
        print(book)
