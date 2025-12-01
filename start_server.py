import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

try:
    port = get_free_port()
    print(f"Starting server on port {port}")
    sys.stdout.flush()
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
except Exception as e:
    print(f"Error: {e}")
