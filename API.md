# PowerForecast API Documentation ⚡

This document provides technical documentation for the data endpoints, JSON schemas, Python parser modules, and Discord bot commands available in the **PowerForecast** project.

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Data Endpoints (JSON APIs)](#data-endpoints-json-apis)
   - [`GET /rates.json`](#get-ratesjson)
   - [`GET /appliance_db.json`](#get-appliance_dbjson)
3. [Python Parser API (`meralco_parser.py`)](#python-parser-api-meralco_parserpy)
   - [`get_meralco_rates()`](#get_meralco_rates)
   - [`get_rates_for_specific_month(year, month)`](#get_rates_for_specific_monthyear-month)
4. [Discord Bot Commands API (`bot.py`)](#discord-bot-commands-api-botpy)
5. [Usage Examples](#usage-examples)

---

## 🌐 Overview

PowerForecast exposes rate data and appliance consumption parameters via static JSON endpoints (consumed directly by the Web UI front-end), a Python PDF parser library for programmatic access, and a Discord slash command interface.

---

## 📊 Data Endpoints (JSON APIs)

### `GET /rates.json`

Returns the latest parsed Meralco residential electricity rates categorized by consumption bracket (kWh).

#### Response Schema

```json
{
  "success": true,
  "error": null,
  "warning": null,
  "date": "2026-07-01",
  "data": [
    {
      "kwh": 200,
      "rate": 14.8261,
      "generation_rate": 9.2504,
      "rate_change": 0.3428,
      "rate_change_percent": 2.37,
      "trend": "up"
    }
  ],
  "meta": {
    "timestamp": "2026-07-28T15:17:58.430118",
    "source": "https://meralcomain.s3.ap-southeast-1.amazonaws.com/2026-07/07-2026_residential_bills.pdf"
  }
}
```

#### Field Descriptions

| Field | Type | Description |
| :--- | :--- | :--- |
| `success` | `boolean` | `true` if PDF parsing succeeded |
| `error` | `string \| null` | Error details if retrieval failed |
| `date` | `string \| null` | Effective billing date |
| `data[].kwh` | `integer` | Consumption threshold (e.g. 50, 100, 200, 500) |
| `data[].rate` | `float` | Total Effective Rate per kWh (PHP/kWh) |
| `data[].generation_rate` | `float` | Base Generation Charge per kWh (PHP/kWh) |
| `data[].rate_change` | `float` | Month-over-month rate change (PHP/kWh) |
| `data[].rate_change_percent` | `float` | Percentage change (% relative to previous month) |
| `data[].trend` | `string` | Trend direction: `"up"`, `"down"`, or `"stable"` |
| `meta.timestamp` | `string` | ISO 8601 timestamp when the rate was generated |
| `meta.source` | `string` | Direct Amazon S3 URL of the parsed Meralco PDF bulletin |

---

### `GET /appliance_db.json`

Provides average wattages and operational ranges for common Philippine household appliances.

#### Response Schema

```json
{
  "appliances": [
    {
      "id": "aircon_1hp",
      "name": "1.0 HP Air Conditioner (Inverter)",
      "category": "Cooling",
      "wattage_avg": 750,
      "wattage_min": 500,
      "wattage_max": 1100,
      "default_hours_per_day": 8
    }
  ]
}
```

---

## 🐍 Python Parser API (`meralco_parser.py`)

You can import `meralco_parser.py` into any Python project to programmatically extract and calculate Meralco rate components.

```python
from meralco_parser import get_meralco_rates, get_rates_for_specific_month

# Fetch latest rate bulletin
rates_data = get_meralco_rates()

if rates_data["success"]:
    for entry in rates_data["data"]:
        print(f"Consumption: {entry['kwh']} kWh | Total Rate: ₱{entry['rate']}/kWh | Gen Rate: ₱{entry['generation_rate']}/kWh")
```

### Key Functions

- `get_meralco_rates() -> MeralcoRatesResult`: Automatically attempts to download and parse the PDF for the current month. Fallback logic automatically checks previous months if the current month's PDF is not yet published.
- `get_rates_for_specific_month(year: int, month: int) -> MeralcoRatesResult`: Downloads and parses the rate schedule for a specific target month and year.

---

## 🤖 Discord Bot Commands API (`bot.py`)

The Discord Bot exposes interactive slash commands:

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `/ask` | `<question>` | Chat with **BillShock AI** regarding rates, power-saving tips, or appliance queries |
| `/rates` | None | View current Meralco rate breakdown across brackets |
| `/bracket` | `<kwh>` | Save user's typical monthly consumption bracket |
| `/calculate` | `<appliance>` `<hours>` `[days]` | Estimate running cost for a specific appliance |
| `/appliances` | None | Browse typical household appliance wattage database |
| `/wattage` | `<query>` | Search wattage ranges for a specific device |
| `/total_bill` | `<kwh>` `[gen_rate]` `[other]` | Calculate itemized total monthly electricity bill |
| `/generation_charge` | `<kwh>` | Calculate base generation charge component |
| `/update_rates` | None | Force re-check and parse latest Meralco rate PDF |

---

## 💡 Frontend API Integration Example

In JavaScript (Web UI):

```javascript
async function loadMeralcoRates() {
    const res = await fetch('rates.json');
    const result = await res.json();
    if (result.success && result.data) {
        console.log("Current Generation Rate:", result.data[0].generation_rate);
    }
}
loadMeralcoRates();
```
