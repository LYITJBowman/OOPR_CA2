#
# File        : remote_exec_test.py  
# Created     : 01/12/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

import paramiko
l_password = "ass1gnm3nt"
l_host = "192.168.0.207"
l_user = "l00170244"
l_port = 3022
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(l_host, port=l_port, username=l_user, password=l_password)
transport = ssh.get_transport()
session = transport.open_session()
session.set_combine_stderr(True)
session.get_pty()
#for testing purposes we want to force sudo to always to ask for password. because of that we use "-k" key
session.exec_command("ls -l --time=atime")
stdin = session.makefile('wb', -1)
stdout = session.makefile('rb', -1)
#you have to check if you really need to send password here
stdin.write(l_password +'\n')
stdin.flush()
for line in stdout.read().splitlines():
    print('host: %s: %s' % (l_host, line))
