import { useEffect, useRef } from "react";
import {
  Chart,
  LineElement,
  PointElement,
  LineController,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler,
} from "chart.js";
import styles from "./StockChart.module.css";

Chart.register(
  LineElement,
  PointElement,
  LineController,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler
);

export default function StockChart({ history, ticker }) {
  const priceRef = useRef(null);
  const rsiRef = useRef(null);
  const macdRef = useRef(null);
  const priceChart = useRef(null);
  const rsiChart = useRef(null);
  const macdChart = useRef(null);

  const labels = history.map((d) => d.Date.slice(0, 10));
  const closes = history.map((d) => d.Close);
  const ma20 = history.map((d) => d.MA_20 || null);
  const ma50 = history.map((d) => d.MA_50 || null);
  const rsi = history.map((d) => d.RSI || null);
  const macd = history.map((d) => d.MACD || null);
  const macdSignal = history.map((d) => d.MACD_Signal || null);
  const bbUpper = history.map((d) => d.BB_Upper || null);
  const bbLower = history.map((d) => d.BB_Lower || null);

  useEffect(() => {
    // Destroy existing charts
    if (priceChart.current) priceChart.current.destroy();
    if (rsiChart.current) rsiChart.current.destroy();
    if (macdChart.current) macdChart.current.destroy();

    const commonOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { labels: { color: "#9ca3af" } } },
      scales: {
        x: {
          ticks: {
            color: "#6b7280",
            maxTicksLimit: 10,
            maxRotation: 0,
          },
          grid: { color: "#1f2937" },
        },
        y: {
          ticks: { color: "#6b7280" },
          grid: { color: "#1f2937" },
        },
      },
    };

    // --- Price + MA + Bollinger Bands ---
    priceChart.current = new Chart(priceRef.current, {
      type: "line",
      data: {
        labels,
        datasets: [
          {
            label: `${ticker} Close`,
            data: closes,
            borderColor: "#6366f1",
            backgroundColor: "rgba(99,102,241,0.08)",
            borderWidth: 2,
            pointRadius: 0,
            fill: true,
          },
          {
            label: "MA 20",
            data: ma20,
            borderColor: "#f59e0b",
            borderWidth: 1.5,
            pointRadius: 0,
            fill: false,
          },
          {
            label: "MA 50",
            data: ma50,
            borderColor: "#10b981",
            borderWidth: 1.5,
            pointRadius: 0,
            fill: false,
          },
          {
            label: "BB Upper",
            data: bbUpper,
            borderColor: "#94a3b8",
            borderDash: [4, 4],
            borderWidth: 1,
            pointRadius: 0,
            fill: false,
          },
          {
            label: "BB Lower",
            data: bbLower,
            borderColor: "#94a3b8",
            borderDash: [4, 4],
            borderWidth: 1,
            pointRadius: 0,
            fill: false,
          },
        ],
      },
      options: { ...commonOptions },
    });

    // --- RSI ---
    rsiChart.current = new Chart(rsiRef.current, {
      type: "line",
      data: {
        labels,
        datasets: [
          {
            label: "RSI",
            data: rsi,
            borderColor: "#a78bfa",
            borderWidth: 2,
            pointRadius: 0,
            fill: false,
          },
        ],
      },
      options: {
        ...commonOptions,
        plugins: {
          ...commonOptions.plugins,
          annotation: {},
        },
        scales: {
          ...commonOptions.scales,
          y: {
            ...commonOptions.scales.y,
            min: 0,
            max: 100,
            ticks: { color: "#6b7280" },
          },
        },
      },
    });

    // --- MACD ---
    macdChart.current = new Chart(macdRef.current, {
      type: "line",
      data: {
        labels,
        datasets: [
          {
            label: "MACD",
            data: macd,
            borderColor: "#34d399",
            borderWidth: 2,
            pointRadius: 0,
            fill: false,
          },
          {
            label: "Signal Line",
            data: macdSignal,
            borderColor: "#f87171",
            borderWidth: 2,
            pointRadius: 0,
            fill: false,
          },
        ],
      },
      options: { ...commonOptions },
    });

    return () => {
      priceChart.current?.destroy();
      rsiChart.current?.destroy();
      macdChart.current?.destroy();
    };
  }, [history, ticker]);

  return (
    <div className={styles.container}>
      <div className={styles.chartBox}>
        <h3 className={styles.chartTitle}>Price — MA20 — MA50 — Bollinger Bands</h3>
        <div className={styles.chartWrapper}>
          <canvas ref={priceRef} />
        </div>
      </div>

      <div className={styles.row}>
        <div className={styles.chartBox}>
          <h3 className={styles.chartTitle}>RSI (14)</h3>
          <div className={styles.chartWrapper}>
            <canvas ref={rsiRef} />
          </div>
        </div>

        <div className={styles.chartBox}>
          <h3 className={styles.chartTitle}>MACD</h3>
          <div className={styles.chartWrapper}>
            <canvas ref={macdRef} />
          </div>
        </div>
      </div>
    </div>
  );
}