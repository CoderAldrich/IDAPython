# -*- coding: cp936 -*-
# ��ģ����ĳһ���ļ������ݸ���R2ָ����ڴ�����ݣ����ݴ�С���ļ���С

import idc
import os

backupfile = AskFile(0, '*.*', 'select the file to load')

size = os.path.getsize(backupfile)

ea = GetRegValue('R2')

loadfile(backupfile, 0, ea, size)
