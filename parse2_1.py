import requests
import csv
from bs4 import BeautifulSoup

LINK = 'https://wordpress.org/plugins/'


# получаем результат выполнения запроса кода html с нужного сайта
def get_html(link):
    response = requests.get(link)
    return response.text


def refinde(str):
    s = str.split(' ')[0]
    return s.replace(',', '')


def write_csv(data):
    with open('listplugins2.csv', 'a') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['h3'],
                           data['link'],
                           data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # данный метод возвращает все найденные элементы в виде списка
    articles = soup.find_all('article')
    # return len(articles)
    for article in articles:
        h3 = article.find('h3', class_='entry-title').text
        link = article.find('h3', class_='entry-title').find('a').get('href')
        rating = article.find('div', class_="plugin-rating").find('span', class_="rating-count").find('a').text
        # print(h3, link, refinde(rating))
        rating = refinde(rating)

        data = {'h3': h3,
                'link': link,
                'rating': rating}
        write_csv(data)


def main():
    link = LINK
    print(get_data(get_html(link)))


if __name__ == "__main__":
    main()
