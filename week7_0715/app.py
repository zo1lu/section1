from flask import Flask, render_template, request, redirect, url_for, session, jsonify

from routes.site_routes import site
from routes.api_routes import api

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/")

# Set the secret key for session management
app.config['SECRET_KEY'] = 'secret'

app.register_blueprint(site)
app.register_blueprint(api, url_prefix='/api')


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/signup", methods=["POST"])
# def sign_up():
#     name = request.form['name']
#     username = request.form['username']
#     password = request.form['password']
#     #check if username has been used
#     if check_username(username):
#         return redirect(url_for("error",message=["Username has been used!"]))
#     else:
#         # if not been used, add into database then redirect to homepage
#         create_member(name, username, password)
#         return redirect("/")


# @app.route("/signin", methods=["POST"])
# def sign_in():
#     username = request.form['username']
#     password = request.form['password']
#     user_data = get_user_by_credentials(username, password)
#     if user_data:
#         # save user data in session
#         session['user_id'] = user_data["id"]
#         session['user_username'] = user_data["username"]
#         session['user_name'] = user_data["name"]
#         # show user's name in member page
#         return redirect("/member")
#     else:
#         #if found nothing, redirect to error page
#         return redirect(url_for("error",message=["Username or password incorrect!"]))

# @app.route("/error")
# def error():
#     message = request.args.get("message","Something Wrong!")
#     return render_template("error.html",msg=message)

# @app.route("/signout")
# def sign_out():
#     #delete user data in session
#     del session['user_id']
#     del session['user_username']
#     del session['user_name']
#     return redirect("/")

# @app.route("/member")
# def member():
#     #use session info to check if user already sign in
#     try:
#         if session.get('user_id') and session.get('user_name') and session.get('user_username'):
#             #get user name and ID
#             name = session['user_name']
#             user_id= session['user_id']
#             #get messages from database
#             messages = get_messages()
#             return render_template("member.html", name = name, messages=messages, user_id=user_id)    
#         else:
#             redirect("/")
#     except:
#         return redirect(url_for("error",message=["Somthing wrong, please try again!"]))
    
# @app.route("/createMessage", methods=["POST"])
# def create_message():
#     #get message from form and id from session 
#     message = request.form["message"]
#     user_id = session.get('user_id')
#     #save data into database
#     if user_id:
#         create_message(user_id, message)
#     return redirect("/member")


# @app.route("/deleteMessage", methods=["POST"])
# def delete_message():
#     messageId = request.args.get("messageId")
#     delete_message(messageId)
#     return redirect("/member")

# @app.route("/api/member",methods=['GET'])
# def member_search():
#     username = request.args.get('username')
#     error_case = {"data":None}
#     if session.get("user_id"):
#         user_data = get_user_by_username(username)
#         return jsonify({"data":user_data})
#     return jsonify(error_case)
    

# @app.route("/api/member", methods=['PATCH'])
# def member_update():
#     user_id = session.get('user_id')
#     successful_case = {"ok":True}
#     error_case = {"error":True}
#     if user_id :
#         #make sure the request content-type = application/json to use get_json() method
#         data = request.get_json()
#         new_name = data["name"]
#         if update_user_name(new_name,user_id):
#             return jsonify(successful_case)
#     return jsonify(error_case)

if __name__ == '__main__':
    app.run(port='3000')