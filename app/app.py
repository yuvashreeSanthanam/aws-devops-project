
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS DevOps CI/CD Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                color: #1e293b;
            }

            header {
                background: #172554;
                color: white;
                padding: 25px 40px;
            }

            header h1 {
                margin: 0;
                font-size: 25px;
            }

            header p {
                margin-bottom: 0;
                color: #cbd5e1;
            }

            .container {
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }

            .welcome {
                margin-bottom: 25px;
            }

            .welcome h2 {
                margin-bottom: 8px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
            }

            .card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.06);
            }

            .card h3 {
                color: #64748b;
                font-size: 14px;
                margin-top: 0;
            }

            .card p {
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 0;
            }

            .success {
                color: #16a34a;
            }

            .deployment {
                background: white;
                padding: 25px;
                border-radius: 12px;
                margin-top: 25px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.06);
            }

            .deployment h3 {
                margin-top: 0;
            }

            .status {
                display: inline-block;
                background: #dcfce7;
                color: #166534;
                padding: 8px 15px;
                border-radius: 20px;
                font-weight: bold;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #64748b;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>AWS DevOps Dashboard</h1>
            <p>Continuous Integration and Continuous Deployment Demo</p>
        </header>

        <div class="container">

            <div class="welcome">
                <h2>Welcome to the CI/CD Dashboard!</h2>
                <p>Your Flask application is running successfully on AWS EC2.</p>
            </div>

            <div class="cards">

                <div class="card">
                    <h3>Application Status</h3>
                    <p class="success">● Running</p>
                </div>

                <div class="card">
                    <h3>Application Version</h3>
                    <p>Version 7.0</p>
                </div>

                <div class="card">
                    <h3>Deployment Platform</h3>
                    <p>AWS EC2</p>
                </div>

                <div class="card">
                    <h3>Container Technology</h3>
                    <p>Docker</p>
                </div>

            </div>

            <div class="deployment">
                <h3>Deployment Information</h3>
                <p><strong>CI/CD Tool:</strong> Jenkins</p>
                <p><strong>Source Code:</strong> GitHub</p>
                <p><strong>Deployment Method:</strong> Automated Pipeline</p>
                <p><strong>Application:</strong> Python Flask</p>
                <p><strong>Status:</strong>
                    <span class="status">Deployment Successful</span>
                </p>
            </div>

        </div>

        <footer>
            AWS DevOps CI/CD Demo | Powered by Flask, Docker and Jenkins
        </footer>

    </body>
    </html>
    """)


@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "message": "Application is running successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
