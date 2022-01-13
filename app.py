from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps


# from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
"""
* secret_key se generuje nejlépe pomocí os.urandom(24)
* ale obecně je to prostě velké náhodné číslo
* proměnnou secrec_key nikdi nikdy nidky nesdílím v repositáři!!! tak jako teď :)
"""
app.secret_key = (
    b"\xe3\x84t\x8b\x02\x1c\xfb\x82PH\x19\xe8\x98\x05\x90\xa8\xc83\xf1\xe2\xf4v\xfe\xf0"
    b"\xe3\x84t\x8b\x02\x1c\xfb\x82PH\x19\xe8\x98\x05\x90\xa8\xc83\xf1\xe2\xf4v\xfe\xf0"
)
# app.secret_key = os.urandom()
"""
1#
def login_required(f):
    
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash(f'Pro zobrazení této stránky ({request.path}) je nutné se přihlásit!', 'err')
            return redirect(url_for('login', next=request.path))

    
    wrapper.__name__ = f.__name__
    wrapper.__name__ = f.__name__
    return wrapper
"""
2#
@app.route("/")
def index():
    return render_template("hlava.html.j2")

3#
@app.route("/filozo/", methods=["GET"])

def filozo():
    return render_template("filozo.html.j2")

4#
@app.route("/filozo/", methods=["POST"])
def filozo_post():

    jmeno = request.form.get("jmeno")
    heslo = request.form.get("heslo")
    print("POST:", jmeno, heslo)

    return redirect(url_for("filozo"))

5#
@app.route("/kinema/")
def kinema():
    return render_template("kinema.html.j2")

6#
@app.route("/litera/")
def litera():

        return redirect(url_for('login', next=request.path))

7#
@app.route("/login/", methods=["GET"])
def login():
    if request.method == "GET":  # nemá funkčí význam -- jen ukázka
        login = request.args.get("login")
        passwd = request.args.get("passwd")
        print(login, passwd)
    return render_template("login.html.j2")

8#
@app.route("/login/", methods=["POST"])
def login_post():
   
        return redirect(url_for("login"))

9#
@app.route("/logout/")
def logout():
    session.pop("user", None)
    flash("Právě jsi se odhlásil", "pass")
    return redirect(url_for("index"))
