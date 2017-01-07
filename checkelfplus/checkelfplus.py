#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import re


def build(arg):


    pcpath = glob.glob( "/var/pisi/%s/install/usr/lib/pkgconfig/*.pc" % arg[1][0].split("-lm-x86_64")[0])
    cmakepath = glob.glob( "/var/pisi/%s/work/%s/CMakeLists.txt" % (arg[1][0].split("-lm-x86_64")[0],re.search("[a-z]*\-[0-9]*\.[0-9]*\.[0-9]*",arg[1][0].split("-lm-x86_64")[0]).group()))
    print pcpath
    print cmakepath
    if len(pcpath) > 0:
        print "pkgparse çalıştırıldı"
        if os.path.exists(pcpath[0]):
            os.system("sudo python pkgpars.py %s" % pcpath[0])
    if len(cmakepath) > 0:
        print "deneme çalıştırıldı"
        if os.path.exists(cmakepath[0]):
            os.system("sudo python deneme.py %s" % cmakepath[0])
