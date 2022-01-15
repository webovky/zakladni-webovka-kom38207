from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps


# from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = (
    b"\xe3\x84t\x8b\x02\x1c\xfb\x82PH\x19\xe8\x98\x05\x90\xa8\xc83\xf1\xe2\xf4v\xfe\xf0"
    b"\xe3\x84t\x8b\x02\x1c\xfb\x82PH\x19\xe8\x98\x05\x90\xa8\xc83\xf1\xe2\xf4v\xfe\xf0"
)


def login_required(f):
    
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash(f'Fur site sehen, ({request.path}) du hast singen in!', 'err')
            return redirect(url_for('login', next=request.path))

    
    wrapper.__name__ = f.__name__
    wrapper.__name__ = f.__name__
    return wrapper


@app.route("/")
def index():
    return render_template("hlavni.html.j2", a=12, b=3.14)


@app.route("/odhad/")
def abc():
    return render_template("odhad.html.j2")

@app.route("/horniny/<path:parametr>/")
def urcitenebanany(parametr):
    return render_template("horniny.html.j2", parametr=parametr)

@app.route("/blog/")
@login_required
def blog():
    return render_template("blog.html.j2")

@app.route("/login/", methods=["GET"])
def login():
    if request.method == "GET":  
        login = request.args.get("login")
        passwd = request.args.get("passwd")
        print(login, passwd)
    return render_template("login.html.j2")


@app.route("/login/", methods=["POST"])
def login_post():
    login = request.form.get("login")
    passwd = request.form.get("passwd")
    next = request.args.get('next')
    if passwd == "putin":
        session["user"] = login
        flash("Charašo", "pass")
        return render_template("hlavni.html.j2")
        if next:
            return redirect(next)
    else:
        flash("Niet", "err")
    if next: 
        return redirect(url_for("login", next=next))
    else:
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    session.pop("user", None)
    flash("Právě jste se odhlásili", "pass")
    return redirect(url_for("index"))
