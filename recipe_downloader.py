import requests
from lxml import html
from sys import argv


def main():
    url = argv[1]
    r = requests.get(url)
    t = html.fromstring(r.content)

    print('Ingredientes:')
    ing = t.xpath(
        '//*[@id="recipe-detail"]/div[2]/div[2]/div/div/div/div/div[1]/ul/li')

    for i in ing:
        print(' -' + i.text_content())

    print('Valor Nutricional:')
    nut = t.xpath(
        '//*[@id="recipe-detail"]/div[2]/div[2]/div/div/div/div/div[2]/div/div/ul/li')
    for n in nut:
        print(' -  ' + n.text_content())


if __name__ == '__main__':
    main()
