# -*- coding: cp936 -*-
# 本程序用于在Android动态调试时定位并跳转到特定的so模块

import idc
import os

somodule = AskStr('input the name of so module', 'locat the module')

modulebase = GetFirstModule()

while (modulebase != None) and (GetModuleName(modulebase).find(somodule) == -1):

	modulebase = GetNextModule(modulebase)

if modulebase == None:

	print 'failed to find module:' , somodule

else:

	if AskYN(1, 'successed to find the module , jump to the base ?') == 1:
	
		Jump(modulebase)

	else:

		print 'module of' , somodule , 'base address is :' , hex(modulebase)
