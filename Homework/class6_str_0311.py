#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg


import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}
for conn in asa_conn.split('\n'):
    asa_result = re.match(r'\w+ \w+ '
                          r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) '
                          r'\w+ '
                          r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}), '
                          r'idle \d{1,2}:\d{1,2}:\d{1,2}, '
                          r'bytes (\d+), '
                          r'flags (\w+)',
                          conn.strip()).groups()
    asa_dict[asa_result[:4]] = asa_result[4:]
print('打印分析后的字典!')
print(asa_dict)

srcport = 'src'
src_ip = 'src_ip'
dstport = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'


print('\n格式化打印输出\n')
print('=' * 120)
for key, value in asa_dict.items():
    print(f'{src_ip:^10}:{key[0]:^20}|{srcport:^10}:{key[1]:^10}|{dst_ip:^10}:{key[2]:^20}|{dstport:^10}:{key[3]:^10}|')
    print(f'{bytes_name:^10}:{value[0]:^20}|{flags:^10}:{value[1]:^10}|')
    print('=' * 120)

if __name__ == '__main__':
    pass



port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
print('~' * 220)
print(sorted(port_list, key=lambda x:(int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d+)',x).groups()[2]),int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d+)',x).groups()[3]))))
print('~' * 220)