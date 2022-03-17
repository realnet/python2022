#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

import re

MAC = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

remac = re.match(r'(\d{1,3})\s*([a-zA-Z0-9]{1,5}\.[a-zA-Z0-9]{1,5}\.[a-zA-Z0-9]{1,5})\s*([A-Z]{1,8})\s*(\w\w\d\/\d\/\d)', MAC).groups()

print('='*40)
print('VLAN ID\t\t:', remac[0])
print('MAC\t\t\t:',remac[1])
print('TYPE\t\t:',remac[2])
print('INTERFACE\t:',remac[3])
print('='*40)




show = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

reshow = re.match(r'([A-Z]{1,3})\s*([a-z]{1,6})\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,3})\s*([a-z]{1,12})\s*'
                  r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\,\s*([a-z]{1,5})\s*(\d:\d{1,2}\:\d{1,2})\,\s*([a-z]{1,5})'
                  r'\s*(\d{1,9})\,\s*([a-z]{1,5})\s*([A-Z]{1,3})', show).groups()

idle = re.split(':', reshow[6])
nidle = idle[0] + ' Hours ' + idle[1] + ' Minutes ' + idle[2] + ' Seconds '

print('{:20}: {:30}'.format('Protocol', reshow[0]))
print('{:20}: {:30}'.format('Server', reshow[2]))
print('{:20}: {:30}'.format('Localserver', reshow[4]))
print('{:20}: {:30}'.format('Idle', nidle))
print('{:20}: {:30}'.format('Bytes', reshow[8]))
print('{:20}: {:30}'.format('Bytes', reshow[10]))



