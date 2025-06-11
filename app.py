from flask import Flask, Response
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

# 🔸 Counter: total number of Hello World requests
hello_counter = Counter('hello_world_requests_total', 'Total Hello World Requests')

# 🔸 Gauge: random simulated value (e.g., active users)
active_users_gauge = Gauge('active_users', 'Number of active users')

# 🔸 Histogram: response time of /hello endpoint
request_duration_histogram = Histogram(
    'hello_world_request_duration_seconds',
    'Histogram for request duration of hello endpoint'
)

@app.route("/hello")
@request_duration_histogram.time()  # Automatically measures duration
def hello():
    hello_counter.inc()  # Increment counter

    # Simulate random number of active users
    active_users = random.randint(5, 1000)
    active_users_gauge.set(active_users)

    # Simulate processing time
    time.sleep(random.uniform(0.1, 0.7))

    return f"Hello, World! (Active users: {active_users})"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=False, use_reloader=False)
