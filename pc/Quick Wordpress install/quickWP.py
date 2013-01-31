import os,urllib
import time
from zipfile import ZipFile
import shutil
import ConfigParser
import webbrowser

cwd = os.getcwd()
wampPath = 'C:\\wamp\\www\\'

if(os.path.exists( '/temp/')):
    shutil.rmtree( '/temp/')
    
    

projectName = raw_input('Enter a the name of the project..: ')


def getWP():

    print 'downloading wordpress........'
    open(cwd + '/temp/wp.zip', 'wb').write(urllib.urlopen('http://wordpress.org/latest.zip').read())

    zip = ZipFile(cwd + '/temp/wp.zip')
    print 'done'
    print 'Extracting wordpress...'

    zip.extractall(cwd + '/temp/')
    print 'done'

    print 'Moving the wordpress installation to C:/wamp/www/' + projectName
    # - Copy the WP installation
    
    copytree(cwd+ '/temp/wordpress', wampPath + projectName)
    # - remove the junk
   
    print 'done'
    #print 'Getting ready for the first run.. Opening your web browser...'
    #new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    #url = "localhost/" + projectName + "/wp-admin/setup-config.php"
    #webbrowser.open(url,new=new)

    bones = raw_input('Do you want to use the BONES Framework? Y/N: ')
    if(bones == 'y'):
        print 'downloading bones framework...'
        open(cwd + '/temp/bones.zip', 'wb').write(urllib.urlopen('https://github.com/eddiemachado/bones/zipball/master').read())
        zip = ZipFile(cwd + '/temp/bones.zip')
        print 'done'
        print 'Extracting bones to ' + wampPath + projectName + '/wp-content/themes/bones...'

        zip.extractall(wampPath + projectName + '/wp-content/themes/')
        os.rename(wampPath + projectName + '/wp-content/themes/eddiemachado-bones-b84b334', wampPath + projectName + '/wp-content/themes/bones')

        print 'done'
        # - Copy the WP installation
        #copytree(cwd+ '/temp/eddiemachado-bones-b84b334/', wampPath + projectName + '/wp-content/themes/bones/')

    setHost = raw_input('Do you want to configure the hosts file? Y/N: ')
    if(setHost == 'y'):
        changeHosts(projectName)
    else:
        os.system('pause')
        

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                shutil.copy2(s, d)


def changeHosts(projectName):
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    ip = config.get("config", "ip")
    mail = config.get("config", "mail")


    theURL = raw_input('the URL that you want (without .local, or 192.168.0.111.xip.io): ') 
    hostPrefix = '\n127.0.0.1    '
    projectUrl = [hostPrefix + theURL + '.local', hostPrefix + theURL + '.' + ip + '.xip.io']

    print 'Adding the correct info in the hosts file and creating a backup'

    hostDir = 'C:\Windows\System32\drivers\etc\hosts'

    shutil.copy2(hostDir, hostDir + '_bkp')

    with open(hostDir, 'a') as hosts:
              hosts.write(projectUrl[0] + projectUrl[1])

    print 'Done'

    projectRoot = projectName
    print 'Modifying vhost..'

    vhostDir = 'C:/wamp/bin/apache/Apache2.2.21/conf/extra/httpd-vhosts.conf'
    vhostText = '\n\n<VirtualHost *:80>\n   ServerName '+theURL+'.local\n   ServerAlias '+theURL+'.'+ip+'.xip.io\n   DocumentRoot C:/wamp/www/'+projectRoot+'\n   ServerAdmin '+ mail +'\n   ErrorLog "C:/wamp/logs/'+projectRoot+'.log"\n  <Directory "C:/wamp/www/'+projectRoot+'">\n    Options Indexes FollowSymLinks MultiViews\n    AllowOverride all\n    Order Deny,Allow\n    Allow from localhost\n    Allow from ::1\n    Allow from fe80::/10\n    Allow from 127.0.0.1\n  </Directory>\n</VirtualHost>\n'

    shutil.copy2(vhostDir, vhostDir + '_bkp')

    with open(vhostDir, 'a') as vhosts:
              vhosts.write(vhostText)

    print "Everything is done, YOU NEED TO RESTART WAMP"

    os.system('pause')

def main():
   
    #projectName = 'test'
    getWP()

if __name__=="__main__":
    main()

