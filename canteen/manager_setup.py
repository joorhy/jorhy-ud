#_*_ encoding=utf-8 _*_
#!/usr/bin/env python

import sys
from distutils.core import setup
import py2exe

SCRIPT = './app/manager/manager_main.py'

sys.argv.append('py2exe')

setup(windows=[SCRIPT])

# python manager_setup.py py2exe -p MySQLdb