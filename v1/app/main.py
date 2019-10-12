import socket
hostname = (socket.gethostname())

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is v1 running on pod" + hostname

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
