import requests
from bs4 import BeautifulSoup
import json


def get_page(count_page: int, link: str)->str:
    for page in range(1, count_page + 1):
        response = requests.get(f"{link}/interesting?page={page}")
        return response.text


def get_data_from_page(page:str)-> list[dict]:
    data = []
    bs = BeautifulSoup(page, "html.parser")
    titles_h5 = bs.find_all('h5', class_="title")
    for title in titles_h5:
        data.append({
            "href": title.find("a")["href"],
            "title": title.find("a")["title"]
        })
    return data


def write_data_to_file(data:[dict]):
    with open("data.json", 'w', encoding="utf-8", ) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    link = input("Enter link: ")
    count_page = int(input("Enter count pages: "))
    page = get_page(count_page, link)
    write_data_to_file(get_data_from_page(page))


if __name__ == "__main__":
    main()







