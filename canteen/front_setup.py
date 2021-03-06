#_*_ encoding=utf-8 _*_
#!/usr/bin/env python

import sys
from distutils.core import setup
import py2exe

'''includes = ["encodings", "encodings.*"]

options = {"py2exe":
           {"compressed": 1,
            "optimize": 2,
            "includes": includes,
            "bundle_files": 1}}
setup(
    options=options,
    #zipfile=None,
    windows=[{"script": './app/front/front_main.py', "icon_resources": [(1, "front.ico")]}])'''

SCRIPT = "{'script'='./app/front/front_main.py', 'icon_resources': [(1, 'front.ico')]}"
sys.argv.append('py2exe')
setup(windows=[{"script": './app/front/front_main.py', "icon_resources": [(1, "front.ico")]}])

# python front_setup.py py2exe -p MySQLdb