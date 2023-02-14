from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello World</h1></body></html>')

if __name__ == '__main__':
    server_address1 = ('', 8080)
    httpd1 = HTTPServer(server_address1, HelloHandler)
    print(f'Server running at http://{server_address1[0]}:{server_address1[1]}')
    httpd1.serve_forever()
