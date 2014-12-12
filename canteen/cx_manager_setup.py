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

setup(name='manager_main',
      version='0.1',
      description='Sample cx_Freeze wxPython script',
      options={'build_exe': {'includes': 'MySQLdb'}},
      executables=[Executable("./app/manager/manager_main.py", base=base, icon="manager.ico", targetDir="manager")]
      )

# cx_manager_setup.py build