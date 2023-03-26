from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)
request_counter = Counter('myflaskapp_requests_total', 'Total number of requests received by the app')

@app.route('/')
def hello():
    request_counter.inc()
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return generate_latest(), {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(debug=True, ssl_context=('server.crt','server.key'))