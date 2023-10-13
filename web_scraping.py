import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')

        for i, quote in enumerate(quotes, start=1):
            print(f"{i}. {quote.get_text()}\n")
    else:
        print(f"Error {response.status_code}: Unable to retrieve the content.")

if __name__ == "__main__":
    scrape_quotes()
