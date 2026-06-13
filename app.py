from flask import Flask, redirect, request
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

DB = "stats.db"
STATS_PASSWORD = "sinchan123"


def init_db():

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# Render / Gunicorn 启动时立即创建表
init_db()


def add_click(ip):

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute(
        """
        INSERT INTO clicks (
            ip,
            created_at
        )
        VALUES (?, ?)
        """,
        (
            ip,
            (datetime.utcnow() + timedelta(hours=8)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    conn.commit()
    conn.close()


@app.route("/")
def home():

    ip = request.headers.get(
        "X-Forwarded-For",
        request.remote_addr
    )

    add_click(ip)

    return redirect(
        "https://t.me/sinchan_shop",
        code=302
    )


@app.route("/join")
def join():

    ip = request.headers.get(
        "X-Forwarded-For",
        request.remote_addr
    )

    add_click(ip)

    return redirect(
        "https://t.me/sinchan_shop",
        code=302
    )


@app.route("/stats")
def stats():

    key = request.args.get("key")

    if key != STATS_PASSWORD:
        return "Access Denied"

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute(
        "SELECT COUNT(*) FROM clicks"
    )

    total_clicks = c.fetchone()[0]

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    c.execute(
        """
        SELECT COUNT(*)
        FROM clicks
        WHERE DATE(created_at)=?
        """,
        (today,)
    )

    today_clicks = c.fetchone()[0]

    c.execute(
        """
        SELECT COUNT(DISTINCT ip)
        FROM clicks
        """
    )

    unique_visitors = c.fetchone()[0]

    c.execute(
        """
        SELECT created_at
        FROM clicks
        ORDER BY id DESC
        LIMIT 1
        """
    )

    row = c.fetchone()

    last_visit = row[0] if row else "-"

    conn.close()

    return f"""
    <h2>📊 Sinchan Shop Statistics</h2>

    <p><b>Total Clicks:</b> {total_clicks}</p>

    <p><b>Today's Clicks:</b> {today_clicks}</p>

    <p><b>Unique Visitors:</b> {unique_visitors}</p>

    <p><b>Last Visit:</b> {last_visit}</p>
    """


if __name__ == "__main__":
    app.run()
