#
# File        : Webpage_Parser.py  
# Created     : 29/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Python script to connect to a remote webpage and retrieve useful information from it
#
import re
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
    # print(soup.prettify())

    print("\nThe Web Page you have just parsed contains the following sections:")
    # Retrieve page headings, print just the heading text, stripping whitespace
    for header in soup.find_all(class_='section_header'):
        print(header.text.strip())

    # Count the number of times the string Apache2 appears on the page
    # Note - It doesn't search for a string in the content by default, it needs to be passed as a regular expression
    apache2_count = soup.find_all(string=re.compile("Apache2"))
    print("\nThe page contains the string Apache2 {} times.".format(len(apache2_count)))

    print("\nThe Web Page you have just parsed links to the following addresses:")
    # Retrieve the target URLs from the webpage
    # For each URL found, just print the href attribute rather than the full detail
    for link in soup.find_all("a"):
        print(link['href'])

