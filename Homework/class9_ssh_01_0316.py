#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg
import paramiko
import re

private_key = paramiko.RSAKey.from_private_key_file('/Users/zhangxionggang/.ssh/id_rsa')


def test_ssh(ip, username, key, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, pkey=private_key, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()


def get_gw(ip, username, pkey, port=22):
    get_route = test_ssh(ip, username, pkey, cmd='route -n')
    # print(get_route.split('\n')[2:-1])
    # return get_route
    for c in get_route.split('\n')[2:-1]:
        re_result = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                             r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                             r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                             r'(\w+)\s+\d+\s+\d+\s+\d+\s+\w+', c.strip())
        if re_result:
            if re_result.groups()[1] == 'UG':
                return re_result.groups()[0]


if __name__ == '__main__':
    # print(test_ssh('172.20.2.195', 'root', key=private_key))
    # print(test_ssh('172.20.2.195', 'root', key=private_key, cmd='pwd'))
    print('Network Gateway is:')
    print(get_gw('172.20.2.195', 'root', pkey=private_key))





