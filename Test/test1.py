import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/bye":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            resp = {"message": "Good byyyyyyye"}
            self.wfile.write(json.dumps(resp).encode())
    
server = HTTPServer(("localhost", 8000), SimpleAPI)
print("🚀 Server running on http://localhost:8000")

server.serve_forever()

