#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg
import scapy

import re, os

route_n_result = os.popen('netstat -rn').read()

gwliststr = re.findall('192\.168\.1\.\d{1,4}\s*\w+\s*en0',route_n_result)[0]

print(gwliststr)




l1 = [4,5,6,1,2,9,12,7]

l2 = sorted(l1.copy())

for i in range (len(l1)):
    print(l1[i],l2[i])




if __name__ == '__main__':
    pass
