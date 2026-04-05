import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import styles from "./Navbar.module.css";

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav className={styles.navbar}>
      <div className={styles.brand}>
        <span className={styles.logo}>📈</span>
        <Link to="/dashboard" className={styles.brandName}>
          StockAnalyzer
        </Link>
      </div>

      <div className={styles.actions}>
        {user ? (
          <>
            <span className={styles.username}>👤 {user.username}</span>
            <button onClick={handleLogout} className={styles.btnLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login" className={styles.btnLink}>
              Login
            </Link>
            <Link to="/register" className={styles.btnPrimary}>
              Signup
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}