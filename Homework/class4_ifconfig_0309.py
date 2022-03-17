#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

import re
import os
#第一题
ifconfig_result=os.popen('ifconfig ' + 'en0').read()
print('第一题:\n' + ifconfig_result)

#第二题：
ipaddr = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
netmask_hex = re.findall('[0a-z]{10}', ifconfig_result)[0]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[1]
mac_addr = re.findall('\w{0,2}\:\w{0,2}\:\w{0,2}\:\w{0,2}\:\w{0,2}\:\w{0,2}', ifconfig_result)[0]

format_str='{:20} : {:30}'

print(format_str.format('ipv4_add',ipaddr))
print(format_str.format('netmask',netmask_hex))
print(format_str.format('broadcast',broadcast))
print(format_str.format('macadd',mac_addr))


#第三题：
ipv4_front = ipaddr[0:11]
gw = ipv4_front + '254' #本机网关为1

print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为：'+gw+'\n')

ping_result = os.popen('ping ' + gw + ' -c 1').read()

re_ping_result=re.findall('\d{1,3}\.\d{1}\%',ping_result)[0]

if re_ping_result:
    print('网关不可达！')
else:
    print('网关可达！')





if __name__ == '__main__':
    pass
