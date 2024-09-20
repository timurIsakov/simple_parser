from bs4 import BeautifulSoup
import json
import requests


class Parser:
    base_url: str

    def __init__(self, keyword, count_page = 10):
        self._keyword = keyword
        self.count_page = count_page

    def parse_links(self)-> list[dict]:
        raise NotImplementedError

    @staticmethod
    def write_file(name:str, data: list[dict]):
        with open(name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii= False)


class ParserMover(Parser):
    base_url = "https://mover.uz"

    def parse_links(self) -> list[dict]:
        data = []
        for page in range(1, self.count_page + 1):
            response = requests.get(f"{self.__class__.base_url}/search?val={self._keyword}&page={page}")
            soup = BeautifulSoup(response.text, "html.parser")
            tags_h5 = soup.find_all("h5", class_="title")
            for tag in tags_h5:
                link = tag.find("a").get("href")
                title = tag.text.strip()
                data.append(
                    {
                        "title": title,
                        "link": link
                    }
                )
        return data






def main():
    mover = ParserMover("игры", 5)
    result = mover.parse_links()
    mover.write_file("result.json", result)


if __name__ == "__main__":
    main()