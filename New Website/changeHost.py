import os
import shutil
import ConfigParser
import time

config = ConfigParser.ConfigParser()
config.read("config.ini")
ip = config.get("config", "ip")
mail = config.get("config", "mail")


projectName = raw_input('the URL that you want (without .local, or 192.168.0.111.xip.io): ') 
hostPrefix = '127.0.0.1    '
projectUrl = [hostPrefix + projectName + '.local\n', hostPrefix + projectName + '.' + ip + '.xip.io\n']

print 'Adding the correct info in the hosts file and creating a backup'

hostDir = 'C:\Windows\System32\drivers\etc\hosts'

shutil.copy2(hostDir, hostDir + '_bkp')

with open(hostDir, 'a') as hosts:
          hosts.write(projectUrl[0] + projectUrl[1])

print 'Done'

projectRoot = raw_input('What is the project Root? ')
print 'Modifying vhost..'

vhostDir = 'C:/wamp/bin/apache/Apache2.2.21/conf/extra/httpd-vhosts.conf'
vhostText = '\n\n<VirtualHost *:80>\n   ServerName '+projectName+'.local\n   ServerAlias '+projectName+'.'+ip+'.xip.io\n   DocumentRoot C:/wamp/www/'+projectRoot+'\n   ServerAdmin '+ mail +'\n   ErrorLog "C:/wamp/logs/'+projectRoot+'.log"\n  <Directory "C:/wamp/www/'+projectRoot+'">\n    Options Indexes FollowSymLinks MultiViews\n    AllowOverride all\n    Order Deny,Allow\n    Allow from localhost\n    Allow from ::1\n    Allow from fe80::/10\n    Allow from 127.0.0.1\n  </Directory>\n</VirtualHost>\n'

shutil.copy2(vhostDir, vhostDir + '_bkp')

with open(vhostDir, 'a') as vhosts:
          vhosts.write(vhostText)

print "Everything is donw, YOU NEED TO RESTART WAMP"



os.system('pause')



