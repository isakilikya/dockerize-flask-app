from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><p>{0} is the __name__</p>".format(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

