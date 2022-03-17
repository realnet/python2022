#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

word2 = 'Python'
list1=list(word2)
list1.append("-")
sub_list1=list1[0:1]
print(sub_list1)
list1.append(sub_list1[0])
list1.append('y')
list2=map(str,list1)
print("".join(list2))


department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = '456789.123456'
COURSE_FEES_Python = '1234.3456'

line1 = 'Department1 name:%s\tManager:%s\tCourse FEES:%s\tThe END!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%s\tManager:%s\tCourse FEES:%s\tThe END!' % (department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)





import re
str='port-channel1.189      192.168.189.254   YES    CONFIG    up'

interfaceinfo = re.match(r'([a-z]+-[a-z]+\d?\.\d*)\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\S.*(\w{2})$', str).groups()

print('-'*150)
print('接口\t\t:',interfaceinfo[0])
print('IP地址\t:',interfaceinfo[1])
print('状态\t\t:',interfaceinfo[2])






