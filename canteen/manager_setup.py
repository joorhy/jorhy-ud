#_*_ encoding=utf-8 _*_

import sys
from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]

'''options = {"py2exe":
           {"compressed": 1,
            "optimize": 2,
            #"ascii": 1,
            "includes": includes,
            "bundle_files": 1}}
setup(
    version="0.1.0",
    description=u"管理系统",
    name=u"管理系统",
    options=options,
    zipfile=None,
    windows=[{"script": './app/manager/manager_main.py', "icon_resources": [(1, "manager.ico")]}])'''

SCRIPT = "{'script'='./app/manager/manager_main.py', 'icon_resources': [(1, 'manager.ico')]}"
sys.argv.append('py2exe')
setup(options={"py2exe": {"includes": includes}}, windows=[{"script": './app/manager/manager_main.py',
                                                            "icon_resources": [(1, "manager.ico")]}])


# python manager_setup.py py2exe -p MySQLdb