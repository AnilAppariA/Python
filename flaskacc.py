from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/customer")
def customer():
    return "<p>this is , customer!</p>"

@app.route("/cliemts")
def cliemts():
    return "<p>Hello, cliemts!</p>"
app.run()