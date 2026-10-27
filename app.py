
import os

from flask import Flask, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SHHHQL_SECRET_KEY")


def get_db_connection():
    required = [
        "DB_HOST",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
    ]

    if not all(os.environ.get(key) for key in required):
        return None

    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        connection_timeout=5,
    )


@app.get("/")
def dashboard():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({
        "application": "ShhhQL",
        "status": "Backend aktif",
        "database_connected": False,
        "message": "Status koneksi database belum diperiksa."
    })


@app.get("/api/database/status")
def database_status():
    connection = None

    try:
        connection = get_db_connection()

        if connection is None:
            return jsonify({
                "connected": False,
                "message": "Konfigurasi database belum lengkap."
            }), 503

        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()

        return jsonify({
            "connected": True,
            "message": "Koneksi database berhasil."
        })

    except (Error, ValueError):
        app.logger.warning("Database connection check failed.")
        return jsonify({
            "connected": False,
            "message": "Koneksi database gagal. Periksa konfigurasi."
        }), 503

    finally:
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(debug=False)
