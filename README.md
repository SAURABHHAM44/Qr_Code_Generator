# QR Code Generator

This is a web-based QR Code generator. Enter any text or URL and this site generates a QR code image.

## Features
- Generate QR codes for any text or URL.
- Download the QR code image.
- Simple and intuitive web UI (Flask based).

## Usage (Local)
1. Clone this repo and install requirements:
   ```bash
git clone https://github.com/SAURABHHAM44/Qr_Code_Generator.git
cd Qr_Code_Generator
pip install -r requirements.txt
python app.py
```
2. Open http://localhost:5000 in your browser.

## Deployment (Vercel)
- Ensure both requirements.txt and vercel.json are present as below.
- Import the repo into Vercel.
- If deploying for the first time, Vercel will auto-detect everything.

## File Descriptions
- app.py – Flask app source.
- requirements.txt – Python dependencies.
- vercel.json – Vercel build settings for Python.

---
## Credits
Original desktop version with Tkinter by SAURABHHAM44
Web version (Flask) for deployment
