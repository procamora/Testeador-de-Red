#!/bin/env python
# -*- coding: utf-8 -*-

import sys

from cx_Freeze import setup, Executable


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
'''
exe=Executable(
    script='index.py',
    base='Win32Gui',
    icon='Principal.ico'
    )
'''
exe=Executable(
    script='main.py',
    base=base,
    icon='images/Principal.ico',
    copyDependentFiles = True
    )

include_files=['admin.pyc', 'changeip.pyc', 'Compresion.pyc', 'funciones.pyc', 'gui.pyc', 'letter.txt', 'smtp.pyc', 'utils.pyc', './images/', './speedtest/']
includes = []
excludes=[]
packages=['re', 'time', 'sys', 'os', 'platform', 'Tkinter', 'tkFileDialog', 'mailer', 'zipfile', 'glob', 'tarfile', 'subprocess', 'wmi', 'traceback', 'types', 'ctypes', 'win32com', 'win32api', 'win32con', 'win32event', 'win32process']



setup(
    version = '1.0',
    description = 'Configurador Ubiquiti',
    author = 'Pablo Rocamora',
    name = 'Ubiquiti Configurator',
    author_email='pablojoserocamora@gmail.com',
    options = {'build_exe': {'includes':includes, 'excludes':excludes, 'packages':packages, 'include_files':include_files}},
    executables = [exe]
    )

# python.exe .\setup.py build
