from flask import Blueprint, Flask, render_template, request, redirect, url_for, session, jsonify
from models import get_user_by_username, update_user_name

api = Blueprint('api',__name__,url_prefix='/api')

@api.route("/member",methods=['GET'])
def member_search():
    username = request.args.get('username')
    error_case = {"data":None}
    if session["user_id"]:
        user_data = get_user_by_username(username)
        return jsonify({"data":user_data})
    return jsonify(error_case)

@api.route("/member", methods=['PATCH'])
def member_update():
    user_id = session['user_id']
    successful_case = {"ok":True}
    error_case = {"error":True}
    if user_id :
        #make sure the request content-type = application/json to use get_json() method
        data = request.get_json()
        new_name = data["name"]
        if update_user_name(new_name,user_id):
            return jsonify(successful_case)
    return jsonify(error_case)

# @api.route("" ,methods=[])