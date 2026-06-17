from http.server import BaseHTTPRequestHandler, HTTPServer
import socket


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Python Backend</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <h1>Python Webserver läuft</h1>
            <p>Diese Seite wird vom Python-Backend ausgeliefert.</p>
            <p>Der Zugriff erfolgt über Nginx als Reverse Proxy.</p>
            <p>Container-Hostname: {hostname}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Python Webserver läuft auf Port 5000")
server.serve_forever()