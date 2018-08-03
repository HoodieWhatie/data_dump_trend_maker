import pexpect
import time

SERVER = '<DHCP Address of PC>'							      #<localhost>
USERNAME = 'ftpadmin'							                  #FTP Username
PASSWORD = 'ftppassword'						                  #Password


#('172.16.30.254','username', 'password', 'host-description', 'System Name')

#Sonicwalls to Backup
SONICWALL = (
	('10.1.1.3','admin', 'password', 'TEST-FW', 'NSA 2400'),
	('10.1.1.4','admin', 'password', 'TEST-FW-2', 'NSA 2400'),
)

#Fortigate Test
FORTIGATE = ('10.0.0.220', 'admin', 'password')

def connection(host, username, password, desc, sysname):

	 sshc = pexpect.spawn('ssh ' + host) #pexpect.spawn uses pty's and can only be used on Unix. Windows will throw an error.
	 sshc.expect('User:')
	 sshc.sendline(username)
	 sshc.expect('Password:')
	 sshc.sendline(password)
	 sshc.expect(sysname + '>')
	 print 'Logged in...'
	 dts = time.strftime('%Y%m%d%H%M%S')	
	 sshc.sendline('export preferences ftp ' + FTP_SERVER + ' ' + FTP_USERNAME + ' ' + FTP_PASSWORD + ' prefs_'+ desc +'_'+ dts +'.exp')
	 print 'config dumped & copied...'
	 sshc.expect(sysname + '>')
	 sshc.sendline('exit')
	 print 'Exiting...'
	 sshc.close()
	 print 'Connection closed...'
	 time.sleep(2)

#For every Sonicwall in the tuple at the top of the script, run the backup method.
for i in range(0,len(SONICWALLS)):
	print 'backing up ' + SONICWALLS[i][3]
	connection(SONICWALLS[i][0], SONICWALLS[i][1],SONICWALLS[i][2],SONICWALLS[i][3],SONICWALLS[i][4])
	print 'done backing up ' + SONICWALLS[i][3]
