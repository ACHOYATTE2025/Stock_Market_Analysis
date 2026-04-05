import styles from "./SummaryCard.module.css";

export default function SummaryCard({ label, value, type = "neutral" }) {
  return (
    <div className={`${styles.card} ${styles[type]}`}>
      <p className={styles.label}>{label}</p>
      <p className={styles.value}>{value}</p>
    </div>
  );
}