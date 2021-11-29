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

if __name__ == '__main__':
    # Define connection parameters
    destination_ip = "192.168.0.207".rstrip("\n")
    destination_port = 3022
    user_name = "l00170244".rstrip("\n")
    user_password = "ass1gnm3nt".rstrip("\n")
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Create a Boolean to store the connection status
    session_active = False

    # Attempt to make an SSH Connection, attempt to gracefully handle the error if not
    try:
        session.connect(hostname=destination_ip, port=destination_port, username=user_name, password=user_password)
        session_active = True  # Set the Boolean to True if the connection succeeds
    except paramiko.ssh_exception.SSHException as err:
        print("SSH Connection failed!")
        print(err)

    # Execute a command against the target server if the session_active parameter has been set to true
    if session_active:
        # Capture the command output enabled through get_pty in three variables for review
        stdin, stdout, stderr = session.exec_command('whoami', get_pty=True)
        for line in stdout.readline():
            print(line, end="")  # end of line formatting required to prevent output being displayed vertically
