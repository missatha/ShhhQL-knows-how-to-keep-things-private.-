
import os

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SHHHQL_SECRET_KEY")

HTML = """
<!doctype html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ShhhQL — Privacy Engineering</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            background: #10131a;
            color: #f3f4f6;
            font-family: Arial, sans-serif;
        }
        main {
            max-width: 960px;
            margin: 60px auto;
            padding: 24px;
        }
        .brand {
            color: #9bffb0;
            font-size: 14px;
            letter-spacing: 3px;
        }
        h1 { font-size: 44px; margin-bottom: 8px; }
        p { color: #b7bdca; line-height: 1.6; }
        .panel {
            background: #191e29;
            border: 1px solid #30394a;
            border-radius: 14px;
            padding: 24px;
            margin-top: 24px;
        }
        button {
            background: #9bffb0;
            color: #10131a;
            border: 0;
            border-radius: 8px;
            padding: 12px 18px;
            font-weight: bold;
            cursor: pointer;
        }
        pre {
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            color: #9bffb0;
        }
    </style>
</head>
<body>
    <main>
        <div class="brand">🤫 SHHHQL</div>
        <h1>We take data leaks personally.</h1>
        <p>
            A MySQL privacy engineering toolkit for discovering
            sensitive data, assessing risk, and verifying protection.
        </p>

        <section class="panel">
            <h2>Database Discovery</h2>
            <p id="status">Memeriksa kesiapan aplikasi...</p>
            <button onclick="checkStatus()">Check Application</button>
            <pre id="result"></pre>
        </section>
    </main>

    <script>
        async function checkStatus() {
            const status = document.getElementById("status");
            const result = document.getElementById("result");

            status.textContent = "Memeriksa...";
            try {
                const response = await fetch("/api/health");
                if (!response.ok) throw new Error("Request failed");

                const data = await response.json();
                status.textContent = data.status;
                result.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                status.textContent = "Pemeriksaan gagal.";
                result.textContent = "Backend belum tersedia.";
            }
        }
    </script>
</body>
</html>
"""


@app.get("/")
def dashboard():
    return render_template_string(HTML)


@app.get("/api/health")
def health():
    return jsonify({
        "application": "ShhhQL",
        "status": "Backend aktif; database belum dihubungkan.",
        "database_connected": False,
        "scan_available": False
    })


if __name__ == "__main__":
    app.run(debug=False)
