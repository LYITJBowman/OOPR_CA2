#
# File        : Webpage_Parser.py  
# Created     : 29/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Python script to connect to a remote webpage and retrieve useful information from it
#
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    #url = input("Please enter the web address you wish to connect to: ")
    url = 'http://192.168.0.207'

    # Retrieve the Webpage
    webpage = requests.get(url)

    # Pass the retrieved webpage content through to be parsed by Beautiful Soup
    soup = BeautifulSoup(webpage.content, 'html.parser')

    # Test print of the results
    print(soup.prettify())