import requests
from bs4 import BeautifulSoup
import lxml

user = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()

for j in range(1, 26):
    print(f"Page = {j}")
    url = f"https://hard.rozetka.com.ua/videocards/c80087/#search_text=%D0%B2%D1%96%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0={j}"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all("div", class_="catalog-grid ng-star-inserted")

        for product in all_products:
            if product.find("div", class_="catalog-grid ng-star-inserted"):
                cond = product.find("span", class_="catalog-grid ng-star-inserted")
                title = product.find("h6", class_="catalog-grid ng-star-inserted")
                print(cond.text, title.text)
                cond = cond.text.replace(" ", " ")
                with open("text.txt", "a", encoding="utf-8") as file:
                    file.write(f"{cond} {title.text}\n")