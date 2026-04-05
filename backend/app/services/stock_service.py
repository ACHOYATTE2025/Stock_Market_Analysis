import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")
    df = df.reset_index()
    return df[["Date", "Open", "High", "Low", "Close", "Volume"]].to_dict(orient="records")


def get_stock_analysis(ticker: str):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")
    df = df.reset_index()

    # --- Returns ---
    df["Daily_Return"] = df["Close"].pct_change()
    df["Cumulative_Return"] = (1 + df["Daily_Return"]).cumprod() - 1

    # --- Moving Averages ---
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()
    df["MA_200"] = df["Close"].rolling(window=200).mean()

    # --- Bollinger Bands ---
    df["BB_Middle"] = df["Close"].rolling(window=20).mean()
    df["BB_Std"] = df["Close"].rolling(window=20).std()
    df["BB_Upper"] = df["BB_Middle"] + 2 * df["BB_Std"]
    df["BB_Lower"] = df["BB_Middle"] - 2 * df["BB_Std"]

    # --- RSI (Relative Strength Index) ---
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # --- MACD ---
    ema_12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema_12 - ema_26
    df["MACD_Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    df["MACD_Histogram"] = df["MACD"] - df["MACD_Signal"]

    # --- Average True Range (ATR) ---
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = abs(df["High"] - df["Close"].shift(1))
    df["L-PC"] = abs(df["Low"] - df["Close"].shift(1))
    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(window=14).mean()

    # --- Support & Resistance ---
    support = df["Low"].rolling(window=20).min().iloc[-1]
    resistance = df["High"].rolling(window=20).max().iloc[-1]

    # --- Trend ---
    latest = df.iloc[-1]
    if latest["MA_20"] > latest["MA_50"]:
        trend = "bullish"
    elif latest["MA_20"] < latest["MA_50"]:
        trend = "bearish"
    else:
        trend = "neutral"

    # --- RSI Signal ---
    rsi_value = latest["RSI"]
    if rsi_value > 70:
        rsi_signal = "overbought"
    elif rsi_value < 30:
        rsi_signal = "oversold"
    else:
        rsi_signal = "neutral"

    # --- MACD Signal ---
    if latest["MACD"] > latest["MACD_Signal"]:
        macd_signal = "bullish"
    else:
        macd_signal = "bearish"

    # --- Bollinger Signal ---
    if latest["Close"] > latest["BB_Upper"]:
        bb_signal = "overbought"
    elif latest["Close"] < latest["BB_Lower"]:
        bb_signal = "oversold"
    else:
        bb_signal = "neutral"

    # --- Overall Signal ---
    signals = [trend, macd_signal]
    bullish_count = signals.count("bullish")
    bearish_count = signals.count("bearish")
    if rsi_signal == "overbought":
        bearish_count += 1
    elif rsi_signal == "oversold":
        bullish_count += 1

    if bullish_count > bearish_count:
        overall_signal = "BUY"
    elif bearish_count > bullish_count:
        overall_signal = "SELL"
    else:
        overall_signal = "HOLD"

    # --- Performance ---
    start_price = df["Close"].iloc[0]
    end_price = df["Close"].iloc[-1]
    total_return = (end_price - start_price) / start_price * 100
    volatility = df["Daily_Return"].std() * (252 ** 0.5) * 100
    sharpe_ratio = (df["Daily_Return"].mean() / df["Daily_Return"].std()) * (252 ** 0.5)

    # --- Best & Worst Days ---
    best_day = df.loc[df["Daily_Return"].idxmax()]
    worst_day = df.loc[df["Daily_Return"].idxmin()]

    # --- Volume Analysis ---
    avg_volume = df["Volume"].mean()
    latest_volume = df["Volume"].iloc[-1]
    volume_signal = "high" if latest_volume > avg_volume * 1.5 else "normal"

    summary = {
        "ticker": ticker.upper(),
        "overall_signal": overall_signal,
        "trend": trend,
        "rsi_signal": rsi_signal,
        "macd_signal": macd_signal,
        "bb_signal": bb_signal,
        "start_price": round(start_price, 2),
        "end_price": round(end_price, 2),
        "total_return_pct": round(total_return, 2),
        "max_price_1y": round(df["Close"].max(), 2),
        "min_price_1y": round(df["Close"].min(), 2),
        "annualized_volatility_pct": round(volatility, 2),
        "sharpe_ratio": round(sharpe_ratio, 2),
        "rsi": round(rsi_value, 2),
        "macd": round(latest["MACD"], 4),
        "macd_signal_line": round(latest["MACD_Signal"], 4),
        "atr": round(latest["ATR"], 2),
        "support": round(support, 2),
        "resistance": round(resistance, 2),
        "ma_20": round(latest["MA_20"], 2),
        "ma_50": round(latest["MA_50"], 2),
        "ma_200": round(latest["MA_200"], 2) if not pd.isna(latest["MA_200"]) else None,
        "bb_upper": round(latest["BB_Upper"], 2),
        "bb_lower": round(latest["BB_Lower"], 2),
        "avg_volume": int(avg_volume),
        "latest_volume": int(latest_volume),
        "volume_signal": volume_signal,
        "best_day": {
            "date": str(best_day["Date"])[:10],
            "return_pct": round(best_day["Daily_Return"] * 100, 2)
        },
        "worst_day": {
            "date": str(worst_day["Date"])[:10],
            "return_pct": round(worst_day["Daily_Return"] * 100, 2)
        }
    }

    # --- Historical data ---
    df["Date"] = df["Date"].astype(str)
    history = df[[
        "Date", "Close", "Volume", "Daily_Return", "Cumulative_Return",
        "MA_20", "MA_50", "RSI", "MACD", "MACD_Signal",
        "BB_Upper", "BB_Lower", "ATR"
    ]].fillna(0).round(4).to_dict(orient="records")

    return {"summary": summary, "history": history}