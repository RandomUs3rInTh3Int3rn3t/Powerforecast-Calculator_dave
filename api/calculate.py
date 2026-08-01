import json
from urllib.parse import parse_qs, urlparse
from http.server import BaseHTTPRequestHandler

DEFAULT_RATES = {
    "transmission": 1.4074,
    "systemLoss": 0.7994,
    "distTier1": 0.9803,
    "distTier2": 1.2908,
    "distTier3": 1.5837,
    "distTier4": 2.0941,
    "meteringFixed": 5.0,
    "meteringPerKwh": 0.3350,
    "supplyFixed": 16.3800,
    "supplyPerKwh": 0.4979,
    "awatRefund": -0.4278,
    "regReset": -0.0023,
    "vatGen": 0.0941,
    "vatTrans": 0.1126,
    "vatSysLoss": 0.0966,
    "vatOthers": 0.1200,
    "rptRate": 0.0062,
    "lftRate": 0.0050,
    "universalRate": 0.3216,
    "fitAll": 0.2011,
    "lifelineRate": 0.0100,
    "seniorRate": 0.0001
}

def perform_calculation(kwh: float, gen_rate: float, other_charges: float):
    gen_cost = round(kwh * gen_rate * 100) / 100
    trans_cost = round(kwh * DEFAULT_RATES["transmission"] * 100) / 100
    sys_loss_cost = round(kwh * DEFAULT_RATES["systemLoss"] * 100) / 100

    if kwh <= 200:
        dist_rate = DEFAULT_RATES["distTier1"]
    elif kwh <= 300:
        dist_rate = DEFAULT_RATES["distTier2"]
    elif kwh <= 400:
        dist_rate = DEFAULT_RATES["distTier3"]
    else:
        dist_rate = DEFAULT_RATES["distTier4"]

    dist_cost = round(kwh * dist_rate * 100) / 100
    metering_cost = 0 if kwh == 0 else round(kwh * DEFAULT_RATES["meteringPerKwh"] * 100) / 100 + DEFAULT_RATES["meteringFixed"]
    supply_cost = 0 if kwh == 0 else round(kwh * DEFAULT_RATES["supplyPerKwh"] * 100) / 100 + DEFAULT_RATES["supplyFixed"]
    awat_refund = round(kwh * DEFAULT_RATES["awatRefund"] * 100) / 100
    reg_reset = round(kwh * DEFAULT_RATES["regReset"] * 100) / 100
    senior_cost = round(kwh * DEFAULT_RATES["seniorRate"] * 100) / 100

    gen_vat = round(gen_cost * DEFAULT_RATES["vatGen"] * 100) / 100
    trans_vat = round(trans_cost * DEFAULT_RATES["vatTrans"] * 100) / 100
    sys_loss_vat = round(sys_loss_cost * DEFAULT_RATES["vatSysLoss"] * 100) / 100

    dist_total = dist_cost + metering_cost + supply_cost + awat_refund + reg_reset
    dist_vat = round(dist_total * DEFAULT_RATES["vatOthers"] * 100) / 100
    senior_vat = round(senior_cost * DEFAULT_RATES["vatOthers"] * 100) / 100
    total_vat = gen_vat + trans_vat + sys_loss_vat + dist_vat + senior_vat

    rpt_cost = round(kwh * DEFAULT_RATES["rptRate"] * 100) / 100
    lft_base = gen_cost + trans_cost + sys_loss_cost + dist_total + senior_cost + rpt_cost
    lft_cost = round(lft_base * DEFAULT_RATES["lftRate"] * 100) / 100
    gov_taxes_total = rpt_cost + lft_cost + total_vat

    universal_charges_total = round(kwh * DEFAULT_RATES["universalRate"] * 100) / 100
    fit_all_cost = round(kwh * DEFAULT_RATES["fitAll"] * 100) / 100
    lifeline_cost = round(kwh * DEFAULT_RATES["lifelineRate"] * 100) / 100
    non_vat_subsidies_total = universal_charges_total + fit_all_cost + lifeline_cost

    energy_amount = gen_cost + trans_cost + sys_loss_cost + dist_total + senior_cost + gov_taxes_total + non_vat_subsidies_total
    total_bill = energy_amount + other_charges

    return {
        "success": True,
        "input": {
            "kwh": kwh,
            "generation_rate": gen_rate,
            "other_charges": other_charges
        },
        "summary": {
            "total_bill": round(total_bill, 2),
            "energy_cost": round(energy_amount, 2),
            "other_charges": round(other_charges, 2)
        },
        "itemized": {
            "generation_charge": gen_cost,
            "transmission_charge": trans_cost,
            "system_loss_charge": sys_loss_cost,
            "distribution_charge": dist_cost,
            "metering_supply_charge": round(metering_cost + supply_cost, 2),
            "subsidies_and_refunds": round(awat_refund + reg_reset + senior_cost, 2),
            "government_taxes_and_vat": gov_taxes_total,
            "universal_charges_and_fitall": non_vat_subsidies_total
        }
    }

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        kwh = float(params.get('kwh', [0])[0])
        gen_rate = float(params.get('gen_rate', [9.2504])[0])
        other_charges = float(params.get('other', [0])[0])

        res = perform_calculation(kwh, gen_rate, other_charges)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception:
            payload = {}

        kwh = float(payload.get('kwh', 0))
        gen_rate = float(payload.get('generation_rate', payload.get('gen_rate', 9.2504)))
        other_charges = float(payload.get('other_charges', payload.get('other', 0)))

        res = perform_calculation(kwh, gen_rate, other_charges)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))
