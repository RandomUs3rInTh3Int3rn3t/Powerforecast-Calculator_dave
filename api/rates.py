import json
import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Path to rates.json relative to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        rates_path = os.path.join(base_dir, 'rates.json')

        if os.path.exists(rates_path):
            with open(rates_path, 'r', encoding='utf-8') as f:
                data = f.read()
            self.wfile.write(data.encode('utf-8'))
        else:
            fallback = {
                "success": False,
                "error": "rates.json cache file not found",
                "data": []
            }
            self.wfile.write(json.dumps(fallback).encode('utf-8'))
