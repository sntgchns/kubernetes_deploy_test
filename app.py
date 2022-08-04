from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'Time': time.strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)