from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)

        try:
            a = float(params.get("a", [0])[0])
            b = float(params.get("b", [0])[0])
            resultado = a - b
            response = {"resultado": resultado}
        except Exception as e:
            response = {"error": str(e)}

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
