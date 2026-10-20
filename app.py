from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os, socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status = "unavailable"
        try:
            with socket.create_connection((os.getenv("REDIS_HOST", "redis"), 6379), timeout=2) as s:
                s.sendall(b"*1\r\n$4\r\nPING\r\n")
                status = s.recv(128).decode("utf-8", "replace").strip()
        except OSError as exc:
            status = f"error: {exc.__class__.__name__}"
        body = json.dumps({"service": "compose-demo", "redis": status}).encode()
        self.send_response(200 if status == "+PONG" else 503)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers(); self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
