from flask import Flask

app = Flask(__name__)


print("starting")


@app.route("/")
def home():
    return "<div>Welcome To Flask</div>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
