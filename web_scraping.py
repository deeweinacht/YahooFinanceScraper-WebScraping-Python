import time
import requests
import html_table_parser
import constants


def generate_nasdaq_url():
    """
    Generates a url pointing to the yahoo finance page summarizing daily
    data for the nasdaq composite for the previous 90-day period
    :return: <str> generated url
    """
    time2 = int(time.time())
    time1 = time2 - constants.SECONDS_IN_90_DAYS
    url = f'https://finance.yahoo.com/quote/%5EIXIC/history?period1={time1}&' \
          f'period2={time2}&' \
          'interval=1d&' \
          'filter=history&' \
          'frequency=1d&' \
          'includeAdjustedClose=true'
    return url


def scrape(url: str):
    """
    Scrapes webpage html source code from a given URL.
    :param url: address of the webpage
    :return: <str> source code of the webpage
    """
    response = requests.get(url=url, headers=constants.HEADERS)
    source = response.text
    return source


def extract_table_data(source: str):
    """
    Extracts tables from html source code and returns the first table.
    :param source: source file of the webpage
    :return: <list> rows of data from the table
    """
    parser = html_table_parser.HTMLTableParser()
    parser.feed(source)
    return parser.tables[0][1:-1]
