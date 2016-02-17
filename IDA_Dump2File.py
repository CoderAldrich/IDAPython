# -*- coding: cp936 -*-
# 本程序作为IDA条件断点的expression使用，用于执行到某一句代码时dump下R0指向的R1*R2大小的内存，写文件方式为追加到文件末尾

import idc
import os

R0 = GetRegValue("R0");
R1 = GetRegValue("R1");
R2 = GetRegValue("R2");

if os.path.isfile("E:\\AutoRap\\CODE\\processed.bin"):
	size = os.path.getsize("E:\\AutoRap\\CODE\\processed.bin");
else:
	size = 0;

savefile("E:\\AutoRap\\CODE\\processed.bin", size, R0, R1*R2);
