import { useState } from "react";
import { useAuth } from "../../context/AuthContext";
import api from "../../api/axiosInstance";
import StockChart from "../../components/StockChart/StockChart";
import SummaryCard from "../../components/SummaryCard/SummaryCard";
import styles from "./Dashboard.module.css";

export default function Dashboard() {
  const { user } = useAuth();
  const [ticker, setTicker] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!ticker.trim()) return;
    setLoading(true);
    setError("");
    setAnalysis(null);
    try {
      const res = await api.get(`/stock/${ticker.toUpperCase()}/analysis`);
      setAnalysis(res.data);
    } catch (err) {
      setError("Ticker not found or server error.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      {/* Header */}
      <div className={styles.header}>
        <h1 className={styles.title}>Hello, {user?.username} 👋</h1>
        <p className={styles.subtitle}>Analyze stock performance and trends</p>
      </div>

      {/* Search */}
      <form onSubmit={handleSearch} className={styles.searchBar}>
        <input
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          placeholder="Enter a ticker (e.g. AAPL, TSLA, MSFT)"
          className={styles.input}
        />
        <button type="submit" className={styles.btn} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {error && <div className={styles.error}>{error}</div>}

      {analysis && (
        <>
          {/* Summary Cards */}
          <div className={styles.grid}>
            <SummaryCard
              label="Overall Signal"
              value={analysis.summary.overall_signal}
              type="signal"
            />
            <SummaryCard
              label="1-Year Return"
              value={`${analysis.summary.total_return_pct}%`}
              type={analysis.summary.total_return_pct >= 0 ? "positive" : "negative"}
            />
            <SummaryCard
              label="Current Price"
              value={`$${analysis.summary.end_price}`}
              type="neutral"
            />
            <SummaryCard
              label="Annualized Volatility"
              value={`${analysis.summary.annualized_volatility_pct}%`}
              type="neutral"
            />
            <SummaryCard
              label="RSI"
              value={`${analysis.summary.rsi} — ${analysis.summary.rsi_signal}`}
              type="neutral"
            />
            <SummaryCard
              label="Sharpe Ratio"
              value={analysis.summary.sharpe_ratio}
              type={analysis.summary.sharpe_ratio >= 1 ? "positive" : "neutral"}
            />
            <SummaryCard
              label="Support"
              value={`$${analysis.summary.support}`}
              type="neutral"
            />
            <SummaryCard
              label="Resistance"
              value={`$${analysis.summary.resistance}`}
              type="neutral"
            />
          </div>

          {/* Indicators Row */}
          <div className={styles.indicators}>
            <div className={styles.indicator}>
              <span className={styles.indicatorLabel}>Trend</span>
              <span className={`${styles.badge} ${styles[analysis.summary.trend]}`}>
                {analysis.summary.trend}
              </span>
            </div>
            <div className={styles.indicator}>
              <span className={styles.indicatorLabel}>MACD</span>
              <span className={`${styles.badge} ${styles[analysis.summary.macd_signal]}`}>
                {analysis.summary.macd_signal}
              </span>
            </div>
            <div className={styles.indicator}>
              <span className={styles.indicatorLabel}>Bollinger</span>
              <span className={`${styles.badge} ${styles[analysis.summary.bb_signal]}`}>
                {analysis.summary.bb_signal}
              </span>
            </div>
            <div className={styles.indicator}>
              <span className={styles.indicatorLabel}>Volume</span>
              <span className={`${styles.badge} ${styles[analysis.summary.volume_signal]}`}>
                {analysis.summary.volume_signal}
              </span>
            </div>
          </div>

          {/* Charts */}
          <StockChart history={analysis.history} ticker={analysis.summary.ticker} />
        </>
      )}
    </div>
  );
}