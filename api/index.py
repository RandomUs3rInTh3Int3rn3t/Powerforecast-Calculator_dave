import os
import sys
import json
from urllib.parse import parse_qs, urlparse
from http.server import BaseHTTPRequestHandler

# Ensure project root is in python path for imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from api.calculate import perform_calculation

class handler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        if path in ['/api/rates', '/api/rates.py']:
            self.handle_rates()
        elif path in ['/api/appliances', '/api/appliances.py']:
            self.handle_appliances()
        elif path in ['/api/calculate', '/api/calculate.py']:
            params = parse_qs(parsed.query)
            kwh = float(params.get('kwh', [0])[0])
            gen_rate = float(params.get('gen_rate', [9.2504])[0])
            other = float(params.get('other', [0])[0])
            self.handle_calculate(kwh, gen_rate, other)
        else:
            # Default fallback for /api or unknown route
            self.handle_rates()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        if path in ['/api/calculate', '/api/calculate.py']:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                payload = json.loads(body)
            except Exception:
                payload = {}

            kwh = float(payload.get('kwh', 0))
            gen_rate = float(payload.get('generation_rate', payload.get('gen_rate', 9.2504)))
            other = float(payload.get('other_charges', payload.get('other', 0)))
            self.handle_calculate(kwh, gen_rate, other)
        else:
            self.send_response(404)
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))

    def handle_rates(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self._send_cors_headers()
        self.end_headers()

        rates_path = os.path.join(base_dir, 'rates.json')
        if os.path.exists(rates_path):
            with open(rates_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            fallback = {"success": False, "error": "rates.json file not found", "data": []}
            self.wfile.write(json.dumps(fallback).encode('utf-8'))

    def handle_appliances(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self._send_cors_headers()
        self.end_headers()

        db_path = os.path.join(base_dir, 'appliance_db.json')
        if os.path.exists(db_path):
            with open(db_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            fallback = {"success": False, "error": "appliance_db.json file not found", "appliances": []}
            self.wfile.write(json.dumps(fallback).encode('utf-8'))

    def handle_calculate(self, kwh, gen_rate, other_charges):
        res = perform_calculation(kwh, gen_rate, other_charges)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))
