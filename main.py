import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time


def make_header():
    header = Headers().generate()

    return header


def make_response(url):
    header = make_header()
    response = requests.get(url=url, headers=header)
    html_text = response.text

    return html_text


def make_soup(url):
    html_text = make_response(url)
    soup = BeautifulSoup(html_text, "html.parser")

    return soup


def get_catalog(url):
    num = 1
    soup = make_soup(url)
    catalog_data = soup.find_all("div", class_="col col-9 text-truncate")
    for topic in catalog_data:
        topic_name = topic.text.strip()
        topic_url = f'{url}{topic.find("a").get("href")}'
        print(num, topic_name, topic_url)
        num += 1


def main():
    pass


if __name__ == "__main__":
    get_catalog("https://tgstat.ru/")
    # make_soup("https://tgstat.ru/")
    # main()
