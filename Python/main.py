from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

class TR143Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request for {self.path}")
        self.send_response(200)
        self.send_header('Content-Type', 'application/octet-stream')
        self.send_header('Content-Length', '1024000')  # 1MB test file
        self.end_headers()
        self.wfile.write(b'0' * 1024000)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST request, {content_length} bytes received")
        self.send_response(200)
        self.end_headers()

def run_server(port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = HTTPServer(server_address, TR143Handler)
    print(f'Starting TR-143 test server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()