#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer 
from sys import argv

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.s_print(b'')
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length)
        
        self.s_print(body)
        self.s_echo(body)

    def s_echo(self, data):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data)

    def s_print(self, data):
        print(self.headers)
        print(data.decode('utf-8'))

def is_IP(IP):
    if IP == "localhost":
        return True
    check = IP.split('.') 
    
    if len(check) != 4:
        return False

    for tmp in check:
        try:
            tmp = int(tmp)
        except ValueError:
            return False
        if tmp < 0 or tmp > 255:
            return False
    return True 

def is_port(port):
    try:
        port = int(port)
    except ValueError:
        return False

    if 0 < port and port < 65535:
        return True
    return False

if len(argv) > 1:
    if is_IP(argv[1]) and is_port(argv[2]):
        httpd = HTTPServer((argv[1], int(argv[2])), HTTPRequestHandler)
        print("Server started: ", argv[1], ':', argv[2])
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    else:
        print("Easy Server Logger v0.1")
        print("Usage: easyserverlogger.py [IP] [PORT]")
        print("IP: 0.0.0.0")
        print("For Local use 127.0.0.1")
        print("For LAN use 0.0.0.0")
        exit()
else:
    print("for usage type -help")
    exit()

