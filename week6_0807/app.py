from flask import Flask, render_template, request, redirect, url_for, session, g
import mysql.connector

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/")

#set key for session data
app.secret_key="secret"

# Configuration for MySQL database
DB_CONFIG = {
    'user': "root",
    'password': 'admin',
    'host': '127.0.0.1',
    'database': 'website',
}
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DB_CONFIG)
    return g.db

@app.before_request
def before_request():
    g.db = get_db()

@app.after_request
def after_request(response):
    db = g.pop('db', None)
    if db is not None:
        db.close()
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    try:
        cursor = g.db.cursor()
        #check if username has been used
        cursor.execute("SELECT * FROM member WHERE username=%s",(username,))
        data=cursor.fetchall()
        if data:
            return redirect(url_for("error",message=["Username has been used!"]))
        else:
            # if not been used, add into database then redirect to homepage
            cursor = g.db.cursor()
            cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",(name, username,password))
            g.db.commit()
            return redirect("/")
    except Exception as error:
        print(error)
        return redirect(url_for("error",message=["Something wrong, please try again!"]))


@app.route("/signin", methods=["POST"])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    try:
        cursor = g.db.cursor()
        query = "SELECT * FROM member WHERE username=%s and password=%s"
        cursor.execute(query,(username,password))
        data= cursor.fetchone()
        if data:
            valid_id= data[0]
            valid_username = data[2]
            valid_name = data[1]
            # save user data in session
            session['user_id']=valid_id
            session['user_username']=valid_username
            session['user_name']=valid_name
            cursor.close()
            # show user's name in member page
            return redirect("/member")
        else:
            #if found nothing, redirect to error page
            return redirect(url_for("error",message=["Username or password incorrect!"]))
            
    except:
        return redirect(url_for("error",message=["Somthing wrong, please try again!"]))

@app.route("/error")
def error():
    message = request.args.get("message","Something Wrong!")
    return render_template("error.html",msg=message)

@app.route("/signout")
def sign_out():
    #delete user data in session
    del session['user_id']
    del session['user_username']
    del session['user_name']
    return redirect("/")

@app.route("/member")
def member():
    #use session info to check if user already sign in
    try:
        if session['user_id'] and session['user_name'] and session['user_username']:
            #get user name and ID
            name = session['user_name']
            user_id= session['user_id']
            #get messages from database
            cursor = g.db.cursor()
            query = "SELECT message.id, message.member_id, member.name, message.content FROM message LEFT JOIN member ON member.id = message.member_id"
            cursor.execute(query)
            data = cursor.fetchall()
            return render_template("member.html", name = name, messages=data, user_id=user_id)    
        else:
            redirect("/")
    except:
        return redirect(url_for("error",message=["Somthing wrong, please try again!"]))
    
@app.route("/createMessage", methods=["POST"])
def create_message():
    #get message from form and id from session 
    message = request.form["message"]
    user_id = session['user_id']
    #save data into database
    cursor = g.db.cursor()
    query = "INSERT INTO message(member_id,content) VALUES(%s, %s)"
    cursor.execute(query,(user_id,message))
    g.db.commit()
    return redirect("/member")


@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    messageId = request.args.get("messageId")
    cursor = g.db.cursor()
    query = "DELETE FROM message WHERE id=%s"
    cursor.execute(query,(messageId,))
    g.db.commit()
    cursor.close()
    return redirect("/member")

app.run(port=3000)