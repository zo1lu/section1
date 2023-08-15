from flask import Blueprint, Flask, render_template, request, redirect, url_for, session, jsonify
from models import check_username, create_member, get_user_by_credentials, get_messages, create_message, delete_message

site = Blueprint('site',__name__)

@site.route("/")
def index():
    return render_template("index.html")

@site.route("/signup", methods=["POST"])
def sign_up():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    #check if username has been used
    if check_username(username):
        return redirect(url_for("site.error",message=["Username has been used!"]))
    else:
        # if not been used, add into database then redirect to homepage
        create_member(name, username, password)
        return redirect("/")


@site.route("/signin", methods=["POST"])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    user_data = get_user_by_credentials(username, password)
    if user_data:
        # save user data in session
        session['user_id'] = user_data["id"]
        session['user_username'] = user_data["username"]
        session['user_name'] = user_data["name"]
        # show user's name in member page
        return redirect("/member")
    else:
        #if found nothing, redirect to error page
        return redirect(url_for("site.error",message=["Username or password incorrect!"]))

@site.route("/error")
def error():
    message = request.args.get("message","Something Wrong!")
    return render_template("error.html",msg=message)

@site.route("/signout")
def sign_out():
    #delete user data in session
    del session['user_id']
    del session['user_username']
    del session['user_name']
    return redirect("/")

@site.route("/member")
def member():
    #use session info to check if user already sign in
    try:
        if session['user_id'] and session['user_name'] and session['user_username']:
            #get user name and ID
            name = session['user_name']
            user_id= session['user_id']
            #get messages from database
            messages = get_messages()
            return render_template("member.html", name = name, messages=messages, user_id=user_id)    
        else:
            redirect("/")
    except:
        return redirect(url_for("site.error",message=["Somthing wrong, please try again!"]))
    
@site.route("/createMessage", methods=["POST"])
def create_message_route():
    #get message from form and id from session 
    message = request.form["message"]
    user_id = session["user_id"]
    #save data into database
    if user_id:
        create_message(user_id, message)
    return redirect("/member")


@site.route("/deleteMessage", methods=["POST"])
def delete_message_route():
    messageId = request.args.get("messageId")
    delete_message(messageId)
    return redirect("/member")