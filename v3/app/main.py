import socket
hostname = (socket.gethostname())
count = 0
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    if count >= 5:
      raise ValueError('A very specific bad thing happened.')
    else:
      return "This is v3 running on pod " + hostname

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
