# -*- coding: utf-8 -*-
import http.server
import os
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.send_response(302)
            self.send_header('Location', '/dashboard/index.html')
            self.end_headers()
            return
        return super().do_GET()

def start_server():
    port = 8080
    server_address = ('127.0.0.1', port)
    try:
        httpd = http.server.ThreadingHTTPServer(server_address, CustomHandler)
    except OSError:
        server_address = ('127.0.0.1', 0)
        httpd = http.server.ThreadingHTTPServer(server_address, CustomHandler)

    actual_port = httpd.server_address[1]
    print(f"Threading HTTP Server running at: http://localhost:{actual_port}/dashboard/index.html")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    start_server()
