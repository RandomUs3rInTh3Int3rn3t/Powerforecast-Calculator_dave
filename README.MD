# PowerForecast ⚡

PowerForecast is a consumer-focused utility designed to estimate, monitor, and forecast household electricity costs. It integrates dynamic **Meralco kWh rate parsing** and detailed component breakdowns to help consumers understand their electricity bills and make informed budgeting decisions.

The project consists of two main parts:
1. **Interactive Web Calculator**: A web-based application (ready for GitHub Pages) to estimate bill details in real-time.
2. **Discord Bot**: An interactive bot bringing rates, appliance cost estimation, and bill calculations directly to Discord.

---

## 🚀 Interactive Web Calculator

The calculator provides a real-time, dynamic breakdown of your Meralco electricity bill, including Generation, Transmission, System Loss, Distribution tiers, VAT, government taxes, and subsidies.

### Live Demo
👉 **[View the Web Calculator on GitHub Pages](https://RandomUs3rInTh3Int3rn3t.github.io/PowerForecast/)**

### Features
* **Dynamic Cost Share:** Stacked bar visualization of your bill component breakdown.
* **Tuning Controls:** Side panel to adjust component multipliers (Transmission, System Loss, VAT, etc.) in real-time.
* **Automatic Bracket Rate Retrieval:** Automatically fetches latest residential rates from `rates.json`.
* **Zero-based Baseline:** Displays `₱0.00` at default/zero consumption.

---

## 🤖 Discord Bot

The Discord bot provides slash commands for rates checking, appliance wattage database queries, and bill calculations.

### Commands
* `/ask <question>`: Chat with **PowerForecast AI** about Meralco rates, appliance power usage, or energy saving tips (or mention `@PowerForecast`).
* `/rates`: View the latest Meralco residential rates per consumption bracket.
* `/bracket <kwh>`: Save your typical monthly consumption bracket to personalize calculations.
* `/calculate <appliance_or_wattage> <hours_per_day> [days]`: Estimate the cost of running a specific appliance.
* `/appliances`: View average wattages for typical Philippine household appliances.
* `/wattage <query>`: Search average wattage and ranges for a specific appliance.
* `/total_bill <kwh> [generation_rate] [other_charges]`: Calculate a fully itemized monthly bill estimate.
* `/generation_charge <kwh>`: Estimate base generation charge.
* `/update_rates`: Force check and update the Meralco rate PDF cache.


### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RandomUs3rInTh3Int3rn3t/PowerForecast.git
   cd PowerForecast
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   ALLOWED_CHANNEL_ID=your_allowed_discord_channel_id_here
   ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

---

## 🚀 Deploying to Vercel

The project is structured to deploy seamlessly to **Vercel** with static web hosting and serverless Python API endpoints.

### Quick Deploy via Vercel CLI
```bash
npm i -g vercel
vercel --prod
```

### Serverless API Routes
* `GET /api/rates` — Latest parsed Meralco rate schedule & trend metadata.
* `GET /api/appliances` — Appliance wattage standards and operational ranges.
* `POST /api/calculate` — Accepts `{ kwh, generation_rate, other_charges }` and returns itemized bill breakdown.
* `GET /docs` — Interactive API Documentation & Testing Playground.

---

## 📂 Project Structure

* `index.html` — Interactive Web Calculator front-end.
* `docs.html` — Interactive API Documentation & Testing Playground.
* `API.md` — Technical API documentation and JSON schemas.
* `vercel.json` — Vercel routing rules & CORS configuration.
* `api/` — Serverless Python API endpoints (`rates.py`, `appliances.py`, `calculate.py`).
* `bot.py` — Discord Bot script.
* `meralco_parser.py` — Backend utility that parses official Meralco rates from bulletins.
* `rates.json` — Local cache containing the latest parsed rate components.
* `appliance_db.json` — Database of typical Philippine household appliances and wattages.
* `requirements.txt` — Python dependencies.

---

## ⚖️ Disclaimer
This application is not affiliated with, endorsed by, or associated with Manila Electric Company (MERALCO). Calculations are estimates based on parsed rate schedules and standard billing formulas.
