import requests



def get_urls(pages: int, path: str):
    for page in range(1, pages + 1):
        response = requests.get(f"{path}/interesting?page={page}")
        print(type(response))





def main():
    link = input("Enter link: ")
    count_pages = int(input("Enter count pages: "))
    get_urls(count_pages, link)




if __name__ == "__main__":
    main()







