# -*- coding: cp936 -*-
# ���������ڶ�̬����SO�ļ�ʱ�鿴log����puts�Լ�printf���¶ϵ㣬Ȼ��edit breakpoint����log��Ϣ���浽�ļ����Թ��鿴�����ݲ���׼ȷ����Ҫ����ӡ������������Ϣ���Ƚϼ�ª

import idc
import os

logfile = open('%path%\\logfile.log', 'a+');

r0 = GetRegValue('R0');

r1 = GetRegValue('R1');

r2 = GetRegValue('R2');

r3 = GetRegValue('R3');

sp = GetRegValue('SP');

logplatform = GetString(r0);

loginfo = logplatform;

count = logplatform.count('%');

if count == 1:
	loginfo = logplatform % r1;
elif count == 2:
	loginfo = logplatform % (r1,r2);
elif count == 3:
	loginfo = logplatform % (r1,r2,r3);
elif count == 4:
	spone = Dword(sp);
	loginfo = logplatform % (r1,r2,r3,spone);
elif count == 5:
	spone = Dword(sp);
	sptwo = Dword(sp+4);
	loginfo = logplatform % (r1,r2,r3,spone,sptwo);
elif count == 6:
	spone = Dword(sp);
	sptwo = Dword(sp+4);
	spthree = Dword(sp+8);
	loginfo = logplatform % (r1,r2,r3,spone,sptwo,spthree);

loginfo += '\n';

logfile.write(loginfo);
