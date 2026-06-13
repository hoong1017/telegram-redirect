from flask import Flask, redirect

app = Flask(__name__)

CLICK_FILE = "clicks.txt"

def get_clicks():

    try:

        with open(
            CLICK_FILE,
            "r"
        ) as f:

            return int(
                f.read()
            )

    except:

        return 0


def save_clicks(clicks):

    with open(
        CLICK_FILE,
        "w"
    ) as f:

        f.write(
            str(clicks)
        )


@app.route("/")
def home():

    clicks = get_clicks()

    clicks += 1

    save_clicks(clicks)

    return redirect(
        "https://t.me/sinchan_shop",
        code=302
    )


@app.route("/stats")
def stats():

    clicks = get_clicks()

    return f"""
Total Clicks: {clicks}
"""


if __name__ == "__main__":
    app.run()
