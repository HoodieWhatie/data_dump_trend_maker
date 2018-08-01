import paramiko
import sys
import re

def open_term(ip_add, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip_add,username=user,password=pwd)
    
    stdin, stdout, stderr=ssh.exec_command("show full-config")

    result = stdout.readlines()
    query = input('What are you looking for?:')

    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        for line in result:
            split_ln = line.split('\W')
            for bit in split_ln:
                    if query in bit:
                        print(bit)
