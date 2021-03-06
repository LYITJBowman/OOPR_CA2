#
# File        : Port_Service_Translator.py  
# Created     : 01/12/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Utility to load and scan a listing of known ports for a given port, returning a service name and details
import csv


def port_service_translator(port):
    """
    Sample function for testing, using local list rather than external file
    :param port: The port to search for
    :return: The service name and description for that port
    """
    port_services = [[22, "ssh", "The Secure Shell (SSH) Protocol"],
                     [80, "http", "World Wide Web HTTP"]]

    # Loop through the list and return details if the port number matches
    for entry in port_services:
        if entry[0] == port:
            return entry[1], entry[2]


def port_service_translator_csv(port):
    """
    Function that searches an external csv listing from iana.org of ports and their underlying services
    :param port: The port to search for
    :return: The service name and description for that port
    """
    # Open the CSV File
    fh = open("service-names-port-numbers.csv")
    fr = csv.reader(fh)
    # Loop through the rows until a port match is found
    for row in fr:
        if row[0] == str(port):
            return row[1], row[2]


if __name__ == '__main__':
    # No main as not intended to be run directly
    pass
