import requests
from bs4 import BeautifulSoup
import re

URL = "https://books.toscrape.com/"

def scrape_books():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    books = []
    articles = soup.find_all("article", class_="product_pod")

    for book in articles:
        price_text = book.find("p", class_="price_color").text

        # Remove everything except numbers and dot
        price = float(re.sub(r"[^\d.]", "", price_text))

        books.append({
            "title": book.h3.a["title"],
            "price": price,
            "rating": book.p["class"][1]
        })

    return books
