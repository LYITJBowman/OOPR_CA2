#
# File        : SSH_Test.py  
# Created     : 29/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Python script to test SSH connectivity to a Ubuntu machine
#
import paramiko


def test_ssh_connection(destination, port, user, password):
    """
    Function to attempt an SSH connection and print results to screen
    :param destination: The IP address of the destination system
    :param port: The port to connect to.  Normally SSH would be port 22.
    :param user: The remote username to use
    :param password: The associated password for the remote user
    :return: None
    """
    # Configure the Paramiko Session
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Attempt to make an SSH Connection, attempt to gracefully handle the error if not
    try:
        session.connect(hostname=destination.rstrip("\n"),
                        port=port,
                        username=user.rstrip("\n"),
                        password=password.rstrip("\n"))
        print("\nSSH Connection Successful!")
    except paramiko.ssh_exception.SSHException as err:
        print("\nSSH Connection failed!")
        print(err)
        exit(99)


if __name__ == '__main__':
    # Prompt for connection parameters
    destination_ip = input("Please enter a target IP address: ")
    destination_port = input("Please enter the port to SSH to: ")
    user_name = input("Please enter your user name: ")
    user_password = input("Please enter your password: ")

    # Attempt the connection
    test_ssh_connection(destination_ip
                        , destination_port, user_name, user_password)
