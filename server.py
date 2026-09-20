import http.server
import socketserver
import json
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                "status": "online",
                "message": "Hello from Python HTTP Server!",
                "server_time": os.popen("date /t").read().strip() if os.name == 'nt' else "Server Active"
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"🚀 Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()
