from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(
        "https://t.me/sinchan_shop",
        code=302
    )

@app.route("/join")
def join():
    return redirect(
        "https://t.me/sinchan_shop",
        code=302
    )

if __name__ == "__main__":
    app.run()