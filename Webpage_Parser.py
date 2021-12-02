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
import urllib.request
from bs4 import BeautifulSoup


def soupify_a_url(target_url):
    # Retrieve the Webpage
    webpage = urllib.request.urlopen(target_url)
    webpage_data = webpage.read()

    # Pass the retrieved webpage content through to be parsed by Beautiful Soup
    soup = BeautifulSoup(webpage_data, 'html.parser')

    # Return the parsed information
    return soup


def print_webpage_classes(webpage, class_name):
    print("\n" + ("-" * 60))
    print("\nThe Web Page you have just parsed contains the following sections:\n")
    # Retrieve page headings, print just the heading text, stripping whitespace
    for header in webpage.find_all(class_=class_name):
        print("> " + header.text.strip())

def webpage_string_search(webpage, search_string):
    # Count the number of times the string appears on the page
    # Note - It doesn't search for a string in the content by default, it needs to be passed as a regular expression
    apache2_count = webpage.find_all(string=re.compile(search_string))
    print("\n" + ("-" * 60))
    print("\nThe page contains the string {} {} times.".format(search_string, len(apache2_count)))

def webpage_link_finder(webpage):
    print("\n" + ("-" * 60))
    print("\nThe Web Page you have just parsed links to the following addresses:\n")
    # Retrieve the target URLs from the webpage
    # For each URL found, just print the href attribute rather than the full detail
    for link in webpage.find_all("a"):
        print("> " + link['href'])


if __name__ == '__main__':
    url = input("Please enter the web address you wish to connect to: ")

    # First we parse the specified URL
    parsed_url = soupify_a_url(url)

    # Next we call a method to print out anything matching the specified class
    print_webpage_classes(parsed_url,'section_header')

    # Next we call a method to search for a specific string
    webpage_string_search(parsed_url,'Apache2')

    # Finally we call a method to scan the page for links to other sites
    webpage_link_finder(parsed_url)


