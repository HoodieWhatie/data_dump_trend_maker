#build SSH2 session
def open_term(ip_add, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip_add,username=user,password=pwd)
    
    #invoke shell and build channels (sockets) for IO features
    channel = ssh.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    #execute code
    stdin.write('''
    config router setting
    set hostname JLsLabRouter
    get system status
    ''')
    
    #read output
    result = stdout.readlines()

    #check for error, print output if clean
    if result == []:
        error = ssh.stderr.readlines()
        print('something went wrong...')
    else:
        for line in result:
            split_ln = line.split('\W')
            for bit in split_ln:
                print(bit)

#executes code without requiring manual entry, testing purposes only
for i in range(0,1):
    print('executing open_term...')
    open_term('10.0.0.220', 'admin', 'password')
    print('program complete...')
