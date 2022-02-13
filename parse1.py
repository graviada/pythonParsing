import requests
from bs4 import BeautifulSoup


# функция main - внутри вызываем функцию get_html
def main():
    link = 'https://wordpress.org'
    print(get_data(get_html(link)))


# функция get_html отсылает запрос на нужный нам сайт
def get_html(link):
    response = requests.get(link)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('header', id="masthead").find('div').find('p').text
    return name


# точка входа
if __name__ == '__main__':
    main()
