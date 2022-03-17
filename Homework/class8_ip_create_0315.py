#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

import logging
# from kamene.all import *
from scapy.all import *
logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 关闭不必要的报错


def testping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    # ping_result.show()
    if ping_result:
        print(ip + ' can reachable')
    else:
        print(ip + ' unreachable')



if __name__ == '__main__':
    testping('192.168.1.254')

