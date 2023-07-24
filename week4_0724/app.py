from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
app = Flask(
            __name__,
            static_folder="public",
            static_url_path="/")
app.secret_key="secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def sign_in():
        username = request.form["username"]
        password = request.form["password"]
        if (username=="") or (password==""):
            return render_template("error.html", msg="Please enter username and password")
        elif (username=="test" and password=="test"):
             session["SIGNED-IN"]=True
             return redirect("/member")
        else:
             return render_template("error.html", msg="Username or password is not correct")

@app.route("/member")
def member():
    if session["SIGNED-IN"]:
        return render_template("member.html")
    else:
         return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message","Somthing Wrong!")
    return render_template("error.html", msg=message)

@app.route("/signout")
def sign_out():
     session["SIGNED-IN"] = False
     return redirect("/")

@app.route("/square/<number>")
def squaring(number):
     return render_template("result.html",num=int(number))

app.run(port=3000)
