#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

import os
import re
import time

while True:
    try:
        netstat_result = os.popen('netstat -nat').read()
        # print(netstat_result)
        finded_tcp80 = False
        for netstat in netstat_result.split('\n')[2:-1]:
            re_result = re.match(r'tcp4\s+\d+\s+\d+\s+\*\.80\s+.*', netstat)
            if re_result:
                print('http (tcp/80) service open')
                finded_tcp80 = True
                break
        if finded_tcp80:
            break
        print('Waiting for 1 minite to monitor ')
        time.sleep(1)
    except KeyboardInterrupt:
        print("recieved AD command Ctrl+C")
        print('EXIT')
        break


if __name__ == '__main__':
    pass
