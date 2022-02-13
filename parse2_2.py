import requests
import csv
from bs4 import BeautifulSoup
import requests

# получить ссылку на тему оформления и его название
LINK = 'https://wordpress.org/themes'


def get_html(link):
    response = requests.get(link)
    return response.text


def write_csv(data):
    with open('themesList.csv', 'a') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['name'],
                           data['link']))


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # данный метод возвращает все найденные элементы в виде списка
    blocks = soup.find('main', id='themes').find('div', class_='themes').find_all('a', class_='url')
    # print(blocks)
    # return len(blocks)
    for a in blocks:
        link = a.get('href')
        name = a.find('h3', class_='theme-name entry-title').text

        # print(link, name)
        data = {'name': name,
                'link': link}
        write_csv(data)


def main():
    # print(get_html(LINK))
    # pass
    link = LINK
    print(get_data(get_html(link)))


if __name__ == "__main__":
    main()
