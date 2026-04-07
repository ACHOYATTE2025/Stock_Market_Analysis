<div align="center">

# 📈 Stock Market Analysis

**Full-Stack Financial Analytics Platform**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.101-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*Analyze historical stock data with real-time technical indicators, signal detection, and interactive charts — powered by Yahoo Finance.*

</div>

---

## 🎬 Demo

<div align="center">

[![Watch the demo](https://img.youtube.com/vi/mwRRK-tUg3U/maxresdefault.jpg)](https://youtu.be/mwRRK-tUg3U)

> 📺 **[Watch the full demo on YouTube](https://youtu.be/mwRRK-tUg3U )**

</div>

---

## 🚀 Overview

**Stock Market Analysis** is a production-ready full-stack web application that lets authenticated users:

- 🔍 Search any publicly traded ticker
- 📊 Visualize 1-year historical price data with interactive charts
- 🤖 Get automated BUY / SELL / HOLD signals based on combined technical indicators
- 📐 Analyze RSI, MACD, Bollinger Bands, ATR, Moving Averages, and more
- 📈 Track performance metrics: Sharpe Ratio, volatility, total return

---

## ✨ Features

### 🔐 Backend (FastAPI)
| Feature | Details |
|--------|---------|
| Authentication | JWT — register, login, access + refresh token |
| Stock Data | 1-year historical data via `yfinance` |
| Technical Indicators | RSI, MACD, Bollinger Bands, ATR, MA20/MA50 |
| Performance Metrics | Sharpe Ratio, annualized volatility, total return |
| Signal Engine | BUY / SELL / HOLD based on combined indicator consensus |
| Support & Resistance | Dynamic levels — 20-day rolling window |
| Volume Analysis | Abnormal volume spike detection |

### 🎨 Frontend (React + Vite)
| Feature | Details |
|--------|---------|
| Auth Flow | Secure login & registration with validation |
| Protected Routes | JWT-gated dashboard |
| Ticker Search | Analyze any stock in real time |
| Summary Cards | Key metrics at a glance |
| Interactive Charts | Price, MA, Bollinger Bands, RSI, MACD |
| Responsive UI | Dark mode, mobile-friendly |

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | FastAPI 0.101 | REST API framework |
| Backend | SQLAlchemy + PostgreSQL | ORM + relational database |
| Backend | fastapi-jwt-auth | JWT authentication |
| Backend | passlib[bcrypt] | Secure password hashing |
| Backend | yfinance + pandas | Stock data retrieval + analytics |
| Frontend | React + Vite | UI framework + build tool |
| Frontend | React Router DOM | Client-side routing |
| Frontend | Axios | HTTP client + JWT interceptors |
| Frontend | Chart.js + react-chartjs-2 | Interactive chart rendering |
| Frontend | CSS Modules | Scoped component styling |
| DevOps | Docker + Docker Compose | Containerized deployment |
| DevOps | Nginx | Static file serving |

---

## 📁 Project Structure

```
stock-market-analysis/
├── backend/
│   ├── app/
│   │   ├── config/
│   │   ├── entity/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── .env
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml
```

---

## 🔗 API Reference

### 🔐 Authentication

| Method | Endpoint | Auth | Description |
|--------|---------|------|-------------|
| POST | `/auth/register` | Public | Create a new account |
| POST | `/auth/login` | Public | Login and receive tokens |
| POST | `/auth/refresh` | Bearer | Refresh access token |

### 📊 Stock Analysis

| Method | Endpoint | Auth | Description |
|--------|---------|------|-------------|
| GET | `/stock/{ticker}` | Bearer | Fetch historical OHLCV data |
| GET | `/stock/{ticker}/analysis` | Bearer | Full technical analysis + signals |

### 📦 Analysis Response Structure

**Summary fields:**
`overall_signal` · `trend` · `rsi` / `rsi_signal` · `macd` / `macd_signal` · `bollinger_bands` · `atr` · `support` / `resistance` · `sharpe_ratio` · `total_return_pct` · `annualized_volatility_pct` · `best_day` / `worst_day`

**History (array of daily data):**
`Date` · `Close` · `Volume` · `Daily_Return` · `Cumulative_Return` · `MA_20` · `MA_50` · `RSI` · `MACD` · `Bollinger Bands` · `ATR`

---

## 🐳 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- Node.js 20+
- Python 3.10+

### ▶️ Run with Docker (Recommended)

```bash
git clone https://github.com/your-username/stock-market-analysis.git
cd stock-market-analysis
docker-compose up --build
```

| Service | URL |
|--------|-----|
| Frontend | http://localhost:5173 |
| Backend | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |

---

### 🛠️ Run Locally

**Backend**
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend/` directory:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=stockanalyzedb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
JWT_SECRET_KEY=your_secret_key
```

---

## 👨‍💻 Author

<div align="center">

**Achoyatte Yatte**
Full-Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-achoyatte-181717?style=flat-square&logo=github)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/your-profile)

*Stack: FastAPI · React · Spring Boot · Docker*
*BYU-Idaho — Software Development Certificate*

</div>

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ using FastAPI, React, and yfinance</sub>
</div>
