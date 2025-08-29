from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

# Home endpoint
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to DevOps Dashboard API",
        "status": "Running",
        "pods": random.randint(1, 10),          # simulate dynamic pod count
        "deployments": random.randint(1, 5),    # simulate dynamic deployments
        "timestamp": datetime.datetime.now().isoformat()
    })

# Health endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "Healthy",
        "uptime": f"{random.randint(1, 72)}h",  # simulate uptime in hours
        "cpu_usage": f"{random.randint(1, 80)}%",   # simulate CPU %
        "memory_usage": f"{random.randint(100, 800)}MB",  # simulate memory usage
        "timestamp": datetime.datetime.now().isoformat()
    })

# metrics endpoint for Prometheus-style scraping
@app.route('/metrics')
def metrics():
    return f"""
    pods {random.randint(1, 10)}
    deployments {random.randint(1, 5)}
    cpu_usage_percent {random.randint(1, 80)}
    memory_usage_mb {random.randint(100, 800)}
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)