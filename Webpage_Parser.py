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
    """
    Procedure to take a URL, retrieve it's content, parse with the Beautiful Soup API and return the results
    :param target_url: The URL to parse
    :return: The webpage, parsed as a Beautiful Soup object
    """
    # Retrieve the Webpage
    webpage = urllib.request.urlopen(target_url)
    webpage_data = webpage.read()

    # Pass the retrieved webpage content through to be parsed by Beautiful Soup
    soup = BeautifulSoup(webpage_data, 'html.parser')

    # Return the parsed information
    return soup


def print_webpage_classes(webpage, class_name):
    """
    Function to search a webpage, parsed by Beautiful Soup, and return the labels of a specified html class
    :param webpage: The Beautiful Soup parsed webpage
    :param class_name: The html class to search for
    :return: None
    """
    # Print some initial formatting output
    print("\n" + ("-" * 60))
    print("\nThe Web Page you have just parsed contains the following sections:\n")

    # Retrieve page headings, print just the heading text, stripping whitespace
    for header in webpage.find_all(class_=class_name):
        print("> " + header.text.strip())


def webpage_string_search(webpage, search_string):
    """
    Function to count the number of times a string appears on a webpage
    :param webpage: The Beautiful Soup parsed webpage
    :param search_string: The string to search for
    :return: None
    """
    # Print some initial formatting output
    print("\n" + ("-" * 60))

    # Count the number of times the string appears on the
    # Note - It doesn't search for a string in the content by default, it needs to be passed as a regular expression
    apache2_count = webpage.find_all(string=re.compile(search_string))

    # Print the results
    print("\nThe page contains the string {} {} times.".format(search_string, len(apache2_count)))


def webpage_link_finder(webpage):
    """
    Function to search a webpage and print any links found
    :param webpage: The Beautiful Soup parsed webpage
    :return: None
    """
    # Print some initial formatting output
    print("\n" + ("-" * 60))
    print("\nThe Web Page you have just parsed links to the following addresses:\n")
    # Retrieve the target URLs from the webpage
    # For each URL found, just print the href attribute rather than the full detail
    for link in webpage.find_all("a"):
        print("> " + link['href'])


if __name__ == '__main__':
    # Prompt the user a URL to check
    url = input("Please enter the web address you wish to connect to: ")

    # First we parse the specified URL
    parsed_url = soupify_a_url(url)

    # Next we call a method to print out anything matching the specified class
    print_webpage_classes(parsed_url,'section_header')

    # Next we call a method to search for a specific string
    webpage_string_search(parsed_url,'Apache2')

    # Finally we call a method to scan the page for links to other sites
    webpage_link_finder(parsed_url)
