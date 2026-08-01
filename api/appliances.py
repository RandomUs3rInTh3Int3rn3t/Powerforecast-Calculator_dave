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

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, 'appliance_db.json')

        if os.path.exists(db_path):
            with open(db_path, 'r', encoding='utf-8') as f:
                data = f.read()
            self.wfile.write(data.encode('utf-8'))
        else:
            fallback = {
                "success": False,
                "error": "appliance_db.json file not found",
                "appliances": []
            }
            self.wfile.write(json.dumps(fallback).encode('utf-8'))
