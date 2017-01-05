#!/usr/bin/python



from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



def setup():
  
    shelltools.system("pwd")
    shelltools.system("ar xf slack-desktop-2.3.4-amd64.deb")
    shelltools.system("tar xf data.tar.xz")

  
  
  
def install():
  pisitools.insinto("/usr/", "./usr/*")
  pisitools.insinto("/etc/", "./etc/*") 
