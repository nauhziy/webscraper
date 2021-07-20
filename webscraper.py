"""
-- BeautifulSoup Script Desc --
This script scapes google for a given search result 
and returns the possible links
"""

import os
import json
import urllib
import requests
import pandas as pd
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



def scrape_google(query):

    query = '+'.join(query.split())

    req = Request("https://www.google.com/search?q=" + query, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(req)

    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    print(soup.find("div"))

    return


def main():
    scrape_google('gmail')


if __name__ == '__main__':
    main()
