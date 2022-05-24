from flask import Flask, render_template, redirect, request, session, jsonify
from cs50 import SQL
from flask_session import Session
from hashlib import sha256
from memebot import *

app = Flask(__name__)

db = SQL("sqlite:///users.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)






@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        isin = session['id']
    except:
        isin = 0
    return render_template('index.html', isin=isin)

@app.route("/signup", methods=["POST",  "GET"])
def singup():
    if request.method == "GET":
        return render_template("signup.html", isin=0)
    username = request.form.get('username')
    email = request.form.get('email')
    fbpassword = request.form.get('fbpassword')
    password = request.form.get('password')
    password = sha256(str(username+password).encode('utf-8')).hexdigest()

    db.execute('INSERT INTO users(hash) VALUES(?)', password)

    options=Options()
    options.headless = False
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    paths = open('path', 'r').read().splitlines()
    PATH = paths[0]
    memes = paths[1]
    login_type(webdriver.Chrome(PATH, chrome_options=options), password+'.pkl', email, fbpassword)


    return redirect('/login', code=307)
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    password=sha256((username+password).encode('utf-8')).hexdigest()
    id = db.execute('SELECT id FROM users WHERE hash=?',password)[0]['id']
    session['id'] = id
    return redirect('/')
@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect("/")


@app.route("/post", methods = ["POST"])
def post():
    id = session["id"]
    acc = db.execute("SELECT hash FROM users WHERE id=?", id)[0]['hash'] + '.pkl'
    min = int(request.form.get("min"))
    max = int(request.form.get("max"))
    sources = request.form.get("sources")
    links = request.form.get("links")
    try:
        if sources == "quote":
            if links == "profile":
                quote(acc, min, max)
            else :
                return redirect("/")
        else :
            subreddits = open(str(id), 'w')
            for i in sources.split():
                subreddits.write(i)
                subreddits.write('\n')
            subreddits.close()
            if links == "profile":
                memeit(acc, min, max, id)
            elif "group" in links:
                grp(acc, min, max, id)
            else:
                page(acc, min, max, id)
    except:
        if sources == "quote":
            if links == "profile":
                quote(acc, min, max)
            else :
                return redirect("/")
        else :
            subreddits = open(str(id), 'w')
            for i in sources.split():
                subreddits.write(i)
                subreddits.write('\n')
            subreddits.close()
            if links == "profile":
                memeit(acc, min, max, id)
            elif "group" in links:
                grp(acc, min, max, id)
            else:
                page(acc, min, max, id)