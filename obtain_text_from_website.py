from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    with urlopen('https://finance.yahoo.com/quote/MSFT/options') as webpage:
        content = webpage.read().decode()

    print(content)


if __name__ == '__main__':
    main()
