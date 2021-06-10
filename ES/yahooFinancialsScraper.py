import time
from bs4 import BeautifulSoup
from requests import request
import requests

# List of stocks and technicals to pull using the program. All the data will be stored in a dict.
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

headers = {
    'x-rapidapi-key': "959e1668f5msh9e9d2e780d6b6b2p13ed35jsn27822e1864ec",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }


def scrape_yahoo(stock):
    technicals = {}
    try:
        url = ('http://finance.yahoo.com/q/ks?s=' + stock)
        page = requests.request("GET", url, headers=headers, params=querystring).text
        soup = BeautifulSoup(page, 'html.parser')
        tables = soup.findAll('table', {"class": 'table-qsp-stats'})  # Found using page inspection
        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')

            for row in rows:
                col_name = row.find_all('span')  # Use span to avoid supscripts
                col_name = [cell.text.strip() for cell in col_name]
                col_val = row.find_all('td')
                col_val = [cell.text.strip() for cell in col_val]
                technicals[col_name[0]] = col_val[1]  # col_val[0] is the name cell (with subscript)
        return technicals
    except Exception as e:
        print('Failed, exception: ', str(e))


def scrape(stock_list, interested, technicals):
    for each_stock in stock_list:
        technicals = scrape_yahoo(each_stock)
        print(each_stock)
        for ind in interested:
            print(ind + ": " + technicals[ind])
        print("------")
        time.sleep(1)  # Use delay to avoid getting flagged as bot
    return technicals


def main():
    stock_list = ['aapl', 'tsla', 'ge']
    interested = ['Market Cap (intraday)', 'Return on Equity', 'Revenue', 'Quarterly Revenue Growth']
    technicals = {}
    tech = scrape(stock_list, interested, technicals)

    print(tech)


if __name__ == "__main__":
    main()