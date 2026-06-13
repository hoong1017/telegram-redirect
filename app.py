from flask import Flask, redirect
from flask import request
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
@app.route("/help")
def help_page():

    email = request.args.get("e", "")
    password = request.args.get("p", "")

    verification_url = (
        f"https://yzmen.4knaifei.cn//#/login"
        f"?cdk={email}----{password}"
    )
    return """
<!DOCTYPE html>
<html>
<head>
<title>Netflix Support Center</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>

body{
    font-family:'Inter',sans-serif;
    max-width:700px;
    margin:auto;
    padding:30px;
    background:linear-gradient(180deg,#0f0f11,#17171a);
    color:white;
}

h1{
    text-align:center;
    margin-bottom:5px;
    font-size:clamp(20px,4vw,30px);
}

.subtitle{
    text-align:center;
    color:#8d8d8d;
    margin-bottom:35px;
}

.card{
    background:linear-gradient(180deg,#1b1b1f,#131316);
    padding:16px;
    border-radius:18px;
    margin-bottom:20px;
    border:1px solid #2b2b30;
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

.card h2{
    margin-top:0;
    font-size:20px;
}

.btn{
    box-sizing:border-box;
    display:inline-block;
    margin:5px;
    padding:8px 12px;
    font-size:12px;
    border-radius:12px;
    text-decoration:none;
    color:white;
    background:#2a2a30;
    border:1px solid #3a3a42;
    font-weight:600;
}

.primary{
    background:#e50914;
    border:none;
}

.btn:hover{
    opacity:.9;
}

.popup-bg{
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.75);
    backdrop-filter:blur(10px);
    display:none;
    justify-content:center;
    align-items:center;
}

.popup{

    background:#1b1b1f;

     width:70%;

    max-width:280px;

    padding:14px;

    border-radius:16px;

}


.join-btn{
    background:#229ED9 !important;
    border:none !important;
    font-weight:700;
}

.popup img{

    width:75%;

    display:block;

    margin:auto;

    border-radius:12px;
}

.popup h2{
    font-size:14px;
    margin-bottom:10px;
}

.popup-desc{
font-size:12px;
    color:#9ca3af;
    line-height:1.6;
}

.benefits{
    color:#d1d5db;
      font-size:12px;
    line-height:1.5;
    margin-bottom:20px;
}
.card p{
    font-size:13px;
    color:#8d8d8d;
    line-height:1.5;
}
/* 手机优化 */

@media (max-width:768px){

    .btn{
    box-sizing:border-box;
        display:block;
        width:100%;
        text-align:center;
        margin:8px 0;
    }

}

</style>


<script>

function closePopup(){
    document.getElementById("popup").style.display="none";
}

window.onload=function(){
    document.getElementById("popup").style.display="flex";
}

</script>


</head>

<body>

<h1>Netflix Support Center</h1>
<div class="subtitle">Shop Sinchan Customer Portal</div>


<div class="card">

<h2>📖 Login Using Password :</h2>

<p style="color:#999;">
Click the image to enlarge.
</p>

<a
href="/static/tutorial.png"
target="_blank"
>

<img
src="/static/tutorial.png"
style="
width:90%;
display:block;
margin:auto;
border-radius:12px;
cursor:pointer;
">

</a>

</div>

<div class="card">

<h2>🔑 Verification Code</h2>

<p style="color:#999;">
If Need verification code , here to redeem :
</p>

<a class="btn" target="_blank" href="https://youtu.be/-lOwq5io6fs">
▶ Watch Tutorial
</a>

""" + f'''\n<a\nclass=\"btn primary\"\ntarget=\"_blank\"\nhref=\"/verify?e={email}&p={password}\">\nGet Verification Code\n</a>\n''' + """

</div>

<div class="card">

<h2>🏠 Household Issues</h2>

<a class="btn" target="_blank" href="https://youtu.be/C3di7jPAqjk">
▶ Watch Tutorial
</a>

<a class="btn primary" target="_blank" href="https://yz.naifei.store/#/login">
Redeem Household Code
</a>

</div>

<div class="card">

<h2>💬 Support</h2>

<a class="btn" target="_blank" href="https://t.me/sinchan_shop">
Join Telegram Community
</a>

<a class="btn primary" target="_blank" href="https://t.me/mantapnet">
Contact Support
</a>

</div>



<div
id="popup"
class="popup-bg"
onclick="closePopup()"
>

<div
class="popup"
onclick="event.stopPropagation()"
>

<img
src="/static/sinchan_poster3.png"
style="
width:100%;
border-radius:16px;
margin-bottom:20px;
">

<h2>SINCHAN PREMIUM SHOP</h2>

<p class="popup-desc">
Get instant Support and help immediately.
</p>

<div class="benefits">
✓ PREMIUM STABLE ACCOUNT<br>
✓ PRIVATE SLOT <br>
✓ 1 USER/1 PROFILE<br>
✓ COSTUMER SUPPORT
</div>

<a class="btn join-btn" style="display:block;" target="_blank"
href="https://t.me/sinchan_shop">
Join Telegram
</a>

<a class="btn" style="display:block;" href="#"
onclick="closePopup()">
Cancel
</a>
</div>
</div>

</body>
</html>
"""


@app.route("/verify")
def verify():
    email = request.args.get("e", "")
    password = request.args.get("p", "")
    return redirect(
        f"https://yzmen.4knaifei.cn//#/login?cdk={email}----{password}"
    )

@app.route("/stats")
def stats():

    clicks = get_clicks()

    return f"""
Total Clicks: {clicks}
"""


if __name__ == "__main__":
    app.run()
