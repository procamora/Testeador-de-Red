#!/usr/bin/env python3
# * coding: utf8 *

import glob
import os

fich = glob.glob("*.py")

for i in fich:
    comando = "2to3 -w {}".format(i)
    print(comando)
    os.system(comando)