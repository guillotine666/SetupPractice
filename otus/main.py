import sys
import argparse
import json
from requests_html import HTMLSession


def createParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', required=True)
    parser.add_argument('-s', '--site', default='google.com', required=True)
    parser.add_argument('-c', '--count', default=999, type=int)
    parser.add_argument('-r', '--recursion', default=False, action='store_const', const=True)
    parser.add_argument('-o', '--output', default='cmd', choices=['cmd', 'json', 'csv'])

    return parser


def save_in_json(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)
    print('Ссылки сохранены в json файл "data.json"')


def save_in_csv(data):
    with open('data.csv', 'w', encoding='utf-8') as csvfile:
        for key in data.keys():
            csvfile.write(f'{key}, {data[key]}\n')
    print('Ссылки сохранены в csv файл "data.csv"')


def search(text, site, output_format, count, recursion):
    session = HTMLSession()
    res = session.get(f'https://www.google.com/search?q={text}')

    if site in ['ya.ru', 'yandex.ru']:
        res = session.get(f'https://yandex.ru/search/?text={text}&lr=54')
    elif site == 'bing.com':
        res = session.get(f'https://www.bing.com/search?q={text}')
    else:
        res = session.get(f'https://www.google.com/search?q={text}')
    result = {}

    if count == 0:
        all_links = res.html.find('a')
    else:
        all_links = res.html.find('a')[:count]

    for link in all_links:
        result.update({link.text: link.absolute_links})

    if output_format == 'json':
        return save_in_json(result)

    if output_format == 'csv':
        return save_in_csv(result)

    for key, value in result.items():
        print(f'{key}:{value}')


def main():
    parser = createParse()
    namespace = parser.parse_args(sys.argv[1:])

    search(namespace.text, namespace.site, namespace.output, namespace.count, namespace.recursion)
