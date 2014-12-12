#!/usr/bin/env python
#coding=utf-8

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

#print sys.getdefaultencoding()
#reload(sys)
#sys.setdefaultencoding("utf-8")

setup(name='front_main',
      version='0.1',
      description='Sample cx_Freeze wxPython script',
      executables=[Executable("./app/front/front_main.py", base=base, icon="front.ico", targetDir="front")]
      )

# cx_front_setup.py build