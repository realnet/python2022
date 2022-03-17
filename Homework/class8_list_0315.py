#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

list1 = ['aaa', 111, (4, 5), 2.02]
list2 = ['bbb', 333, 3.14, (4, 5)]

for x in list1:
    print(f'{x} in list1 and list2') if x in list2 else print(f'{x} only in list1')


def find_name(l1, l2):
    for c in l1:
        if c in l2:
            print(f'{c} in list1 and list2')
        else:
            print(f'{c} only in list1')


if __name__ == '__main__':
    find_name(list1, list2)
    pass

