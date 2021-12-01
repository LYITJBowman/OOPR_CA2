#
# File        : Port_Checker.py  
# Created     : 01/12/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : Initial Port Scan functionality (C) Ruth Lennon
#               Port to service translation method (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Utility to scan a host to determine what port are open and to translate ports to common services
#
import socket
import subprocess
import sys
from datetime import datetime
from Port_Service_Translator import port_service_translator

def port_scan():
    # Clear the screen
    subprocess.call("cls", shell=True)

    # Ask for a remote server to scan
    remote_server = input("Enter a remote host to scan: ")
    remote_server_ip = socket.gethostbyname(remote_server)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host...", remote_server_ip)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify a port range between 1 and 1024
    # Error handling also included

    try:
        for port in range(78, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                port_service, port_description = port_service_translator(port)
                print ("Port {}: Open \t Service Name: {} \t Service Description: {}".format(port, port_service, port_description))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    except socket.error:
        print("Could not connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculate the total runtime
    total_runtime = t2 - t1

    # Printing the runtime information to screen
    print("\n" + ("-" * 60))
    print("Scanning completed in: ", total_runtime)
    print("-" * 60)

if __name__ == '__main__':
    port_scan()
