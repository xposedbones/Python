import os,urllib
import time
from zipfile import ZipFile
import shutil
import webbrowser

cwd = os.getcwd()
wampPath = 'C:\\wamp\\www\\'

if(os.path.exists(cwd + '/temp/wp.zip') and os.path.exists(cwd + '/temp/wordpress')):
    os.remove(cwd + '/temp/wp.zip')
    shutil.rmtree(cwd + '/temp/wordpress')

projectName = raw_input('Enter a the name of the project..: ')


def getWP():

    print 'downloading wordpress........'
    open(cwd + '/temp/wp.zip', 'wb').write(urllib.urlopen('http://fr.wordpress.org/wordpress-3.5-fr_FR.zip').read())

    zip = ZipFile(cwd + '/temp/wp.zip')
    print 'done'
    print 'Extracting wordpress...'

    zip.extractall(cwd + '/temp/')
    print 'done'

    print 'Moving the wordpress installation to C:/wamp/www/' + projectName
    # - Copy the WP installation
    
    shutil.copytree(cwd+ '/temp/wordpress/', wampPath + projectName)
    # - remove the junk
    #copytree(cwd + '/temp/wordpress/', wampPath + projectName)
   
    print 'done'
    print 'Getting ready for the first run.. Opening your web browser...'
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    url = "localhost/" + projectName + "/wp-admin/setup-config.php"
    webbrowser.open(url,new=new)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def main():
   
    #projectName = 'test'
    #if(os.path.exists(wampPath + projectName)):
     #   print 'Project already exists.. Please try again..'
      #  main()
    #else:
        getWP();

if __name__=="__main__":
    main()

