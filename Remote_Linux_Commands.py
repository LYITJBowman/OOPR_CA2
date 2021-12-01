#
# File        : Remote_Linux_Commands.py  
# Created     : 01/12/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

import paramiko


def create_ssh_connection(destination, port, user, password):
    # Configure the Paramiko Session
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Attempt to make an SSH Connection, attempt to gracefully handle the error if not
    try:
        session.connect(hostname=destination.rstrip("\n"),
                        port=port,
                        username=user.rstrip("\n"),
                        password=password.rstrip("\n"))
        return session
    except paramiko.ssh_exception.SSHException as err:
        print("\nSSH Connection failed!")
        print(err)
        exit(99)


def print_remote_output(executed_command, standard_output):
    print("-" * 60)
    print("Output from command: {}\n".format(executed_command))
    for line in standard_output.read().splitlines():
        print(line)  # end of line formatting required to prevent output being displayed vertically
    print("\n")


def execute_remote_command(connection, command, print_output):
    remote_stdin, remote_stdout, remote_stderr = connection.exec_command(command, get_pty=True)
    if print_output:
        print_remote_output(command, remote_stdout)


if __name__ == '__main__':
    # Prompt for connection parameters
    destination_ip = input("Please enter a target IP address: ")
    destination_port = input("Please enter the port to SSH to: ")
    user_name = input("Please enter your user name: ")
    user_password = input("Please enter your password: ")

    ssh_session = create_ssh_connection(destination_ip, destination_port, user_name, user_password)

    execute_remote_command(ssh_session, 'sudo apt install curl', False)
    execute_remote_command(ssh_session, 'mkdir ~/Labs', True )
    execute_remote_command(ssh_session, 'mkdir ~/Labs/Lab1', True)
    execute_remote_command(ssh_session, 'mkdir ~/Labs/Lab2', True)
    execute_remote_command(ssh_session, 'ls -l --time=atime', True)
