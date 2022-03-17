#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()


if __name__ == '__main__':
    pass
