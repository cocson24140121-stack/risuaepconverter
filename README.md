# risuaepconverter

A lightweight web app to convert and downgrade Adobe After Effects (`.aep`) files.

## 🚀 Quick Run Locally
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run server:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser.

## ☁️ Free 24/7 Hosting on Render
1. Create a repository on GitHub and upload all files.
2. Go to [Render](https://render.com) and create a new **Web Service**.
3. Link your GitHub repository.
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free
5. Deploy!
