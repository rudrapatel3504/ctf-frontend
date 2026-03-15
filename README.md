# CTF Recon – Frontend (Vercel)

This is the **static frontend** extracted from the CTF Recon Web tool, ready to deploy on Vercel.

## Project Structure

```
ctf-recon-frontend/
├── public/
│   └── index.html      ← The entire frontend UI
├── vercel.json         ← Vercel static hosting config
└── README.md
```

## Deploy to Vercel

### Option 1 — Vercel CLI
```bash
npm i -g vercel
vercel
```

### Option 2 — GitHub + Vercel Dashboard
1. Push this folder to a GitHub repository
2. Go to [vercel.com](https://vercel.com) → New Project → Import your repo
3. Vercel auto-detects the static config — just click **Deploy**

## Connecting to Your Backend

The frontend calls your Flask backend API. You have two ways to configure the API URL:

### A) Hardcode it (recommended for permanent deploys)

In `public/index.html`, find this line near the top of the `<script>` section:

```js
const DEFAULT_API_BASE = '';  // e.g. 'https://ctfrecon-api.onrender.com'
```

Replace the empty string with your deployed Flask backend URL, e.g.:
```js
const DEFAULT_API_BASE = 'https://ctfrecon-api.onrender.com';
```

### B) Set it in the browser (runtime)

When you open the app, you'll see an **⚙ API BASE URL** bar at the top.  
Paste your backend URL there and click **SAVE** — it persists in `localStorage`.

## Backend Requirements

Your Flask backend (`app.py`) must:
- Be deployed and publicly reachable (e.g. Render, Railway, EC2, etc.)
- Have **CORS enabled** so the Vercel frontend can call it

Add this to your `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

And install: `pip install flask-cors`

## API Endpoints Used

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/portscan` | Port scanner |
| POST | `/api/subdomain` | Subdomain enumeration |
| POST | `/api/whois` | WHOIS / GeoIP lookup |
| POST | `/api/dirbrute` | Directory brute-force |
| POST | `/api/pdfunlock` | PDF password cracker |
| POST | `/api/wordlist` | Targeted wordlist generator |
| POST | `/api/fullrecon/pdf` | Full recon PDF report |
