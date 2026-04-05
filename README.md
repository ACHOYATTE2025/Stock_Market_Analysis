# 📈 Stock Market Analysis  
**Full-Stack Financial Analytics Platform**  
FastAPI • React • PostgreSQL • Docker • JWT  

---

## 🚀 Overview
Stock Market Analysis is a full-stack web application that allows authenticated users to analyze historical stock price data. It provides real-time technical indicators, trend detection, and interactive charts powered by Yahoo Finance data.

---

## ⚙️ Features

### 🔐 Backend
- JWT Authentication — register, login, access token + refresh token  
- Stock Analysis — 1-year historical data via yfinance  
- Technical Indicators — RSI, MACD, Bollinger Bands, ATR, Moving Averages  
- Performance Metrics — Sharpe Ratio, annualized volatility, total return  
- Signal Engine — BUY / SELL / HOLD based on combined indicators  
- Support & Resistance — dynamic levels (20-day rolling window)  
- Volume Analysis — detects abnormal volume spikes  

---

### 🎨 Frontend
- Secure Login & Registration with validation  
- Protected Dashboard (JWT required)  
- Ticker Search — analyze any stock  
- Summary Cards — key metrics  
- Interactive Charts — Price, MA, Bollinger Bands, RSI, MACD  
- Responsive UI — dark mode, mobile-friendly  

---

## 🧱 Tech Stack

| Layer     | Technology                     | Purpose                          |
|----------|------------------------------|----------------------------------|
| Backend  | FastAPI 0.101                | REST API framework              |
| Backend  | SQLAlchemy + PostgreSQL      | ORM + database                  |
| Backend  | fastapi-jwt-auth             | JWT authentication              |
| Backend  | passlib[bcrypt]              | Password hashing                |
| Backend  | yfinance + pandas            | Stock data + analytics          |
| Frontend | React + Vite                 | UI framework                    |
| Frontend | React Router DOM             | Routing                         |
| Frontend | Axios                        | API calls + JWT interceptors    |
| Frontend | Chart.js + react-chartjs-2   | Charts                          |
| Frontend | CSS Modules                  | Styling                         |
| DevOps   | Docker + Docker Compose      | Deployment                      |
| DevOps   | Nginx                        | Static file serving             |

---

## 📁 Project Structure
stock-market-analysis/
├── backend/
│ ├── app/
│ │ ├── config/
│ │ ├── entity/
│ │ ├── routers/
│ │ ├── schemas/
│ │ ├── services/
│ │ ├── utils/
│ │ └── main.py
│ ├── .env
│ ├── Dockerfile
│ └── requirements.txt
├── frontend/
│ ├── src/
│ │ ├── api/
│ │ ├── components/
│ │ ├── context/
│ │ ├── pages/
│ │ └── App.jsx
│ ├── Dockerfile
│ └── nginx.conf
└── docker-compose.yml


---

## 🔗 API Endpoints

### Authentication

| Method | Endpoint        | Auth    | Description                     |
|--------|---------------|--------|--------------------------------|
| POST   | /auth/register | Public | Create account                 |
| POST   | /auth/login    | Public | Login + get tokens             |
| POST   | /auth/refresh  | Bearer | Refresh access token           |

---

### 📊 Stock Analysis

| Method | Endpoint                     | Auth    | Description                  |
|--------|------------------------------|--------|------------------------------|
| GET    | /stock/{ticker}              | Bearer | Historical data              |
| GET    | /stock/{ticker}/analysis     | Bearer | Full analysis + signals      |

---

## 📈 Analysis Response

### 🔹 Summary
- overall_signal → BUY / SELL / HOLD  
- trend → bullish / bearish / neutral  
- rsi / rsi_signal  
- macd / macd_signal  
- bollinger bands  
- atr (volatility)  
- support / resistance  
- sharpe_ratio  
- total_return_pct  
- annualized_volatility_pct  
- best_day / worst_day  

---

### 🔹 History
Array of daily data:
- Date, Close, Volume  
- Daily_Return  
- Cumulative_Return  
- MA_20, MA_50  
- RSI  
- MACD  
- Bollinger Bands  
- ATR  

---

## 🐳 Getting Started

### Prerequisites
- Docker & Docker Compose  
- Node.js 20+  
- Python 3.10+  

---

### ▶️ Run with Docker

```bash
git clone https://github.com/your-username/stock-market-analysis.git
cd stock-market-analysis
docker-compose up --build

Services
Frontend → http://localhost:5173
Backend → http://localhost:8000
API Docs → http://localhost:8000/docs


🧪 Run Locally
Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Frontend
cd frontend
npm install
npm run dev

🔑 Environment Variables
Backend (.env)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=stockanalyzedb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
JWT_SECRET_KEY=your_secret_key

🔑 Environment Variables
Backend (.env)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=stockanalyzedb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
JWT_SECRET_KEY=your_secret_key


👨‍💻 Author

Achoyatte Yatte
Full-Stack Developer
Stack: FastAPI • React • Spring Boot • Docker

BYU-Idaho — Software Development Certificate

📄 License

MIT License


---

💡 Si tu veux, je peux maintenant :  
- ajouter des **captures d’écran (UI)**  
- ou transformer ça en **README GitHub premium (avec badges, démo, etc.)**  

Tu veux upgrader ça niveau portfolio 🔥 ?
