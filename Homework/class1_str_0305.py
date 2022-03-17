#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

import random
section1 = random.randint(1,255)
section2 = random.randint(0,255)
section3 = random.randint(0,255)
section4 = random.randint(0,255)

IPv4 = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)

print(IPv4)