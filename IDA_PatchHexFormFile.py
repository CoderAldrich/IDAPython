# -*- coding: cp936 -*-
# 本模块用某一个文件的数据覆盖R2指向的内存的数据，数据大小是文件大小

import idc
import os

backupfile = AskFile(0, '*.*', 'select the file to load')

size = os.path.getsize(backupfile)

ea = GetRegValue('R2')

loadfile(backupfile, 0, ea, size)
