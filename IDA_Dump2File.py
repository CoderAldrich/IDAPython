# -*- coding: cp936 -*-
# ��������ΪIDA�����ϵ��expressionʹ�ã�����ִ�е�ĳһ�����ʱdump��R0ָ���R1*R2��С���ڴ棬д�ļ���ʽΪ׷�ӵ��ļ�ĩβ

import idc
import os

R0 = GetRegValue("R0");
R1 = GetRegValue("R1");
R2 = GetRegValue("R2");

if os.path.isfile("%path%\\filename.bin"):
	size = os.path.getsize("%path%\\filename.bin");
else:
	size = 0;

savefile("%path%\\filename.bin", size, R0, R1*R2);
