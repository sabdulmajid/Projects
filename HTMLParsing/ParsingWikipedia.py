# Parsing the Wikipedia homepage for links to other pages
import os
import requests
import bs4


def get_html(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, 'html.parser')


def get_urls(html):
    return [a.attrs.get('href') for a in html.select('a[href^="/wiki/"]')]


def get_urls_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def save_urls(filename, urls):
    with open(filename, 'w') as f:
        f.write('\n'.join(urls))


def main():
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    urls = get_urls(get_html(url))
    save_urls('urls.txt', urls)


if __name__ == '__main__':
    main()