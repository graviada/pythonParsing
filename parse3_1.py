import requests
import csv
from bs4 import BeautifulSoup

LINK = "https://premierliga.ru/tournaments/championship/tournament-table/"


def write_csv(data):
    with open('ligaPremier.csv', 'a') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['positions'],
                           data['clubs'],
                           data['goals_plus'],
                           data['goals_minus'],
                           data['points']))


def get_html(link):
    response = requests.get(link)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    trs = soup.find('div', class_='stats-tournament-table').find('table').find_all('tr')
    # print(trs)

    for tr in trs:

        # позиция команды
        position = tr.find_all('td', class_='place')
        # print(position, '\n')
        for i in position:
            positions = i.text.replace('\n', '')
            # print(positions)

        club = tr.find_all('td', class_='club')
        for i in club:
            clubs = i.text.replace('\n', '')
            # print(clubs)

        goal = tr.find_all('td', class_='dark-blue goals')
        for i in goal:
            goals_plus = i.find('span', class_='green').get_text()
            goals_minus = i.find('span', class_='red').get_text()
            # print(goals_plus,'-',goals_minus)

        point = tr.find_all("p", {"class": "points"})
        for i in point:
            points = i.text.replace('\n', '')
            # print(points)

            print(positions, clubs, goals_plus, 'Голов Забито', '-', goals_minus, 'Голов Пропущено', points, 'Очков')

            data = {'positions': positions,
                    'clubs': clubs,
                    'goals_plus': goals_plus,
                    'goals_minus': goals_minus,
                    'points': points}
            write_csv(data)


def main():
    link = LINK
    print(get_data(get_html(link)))


if __name__ == '__main__':
    main()
