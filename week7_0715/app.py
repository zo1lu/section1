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

if __name__ == '__main__':
    app.run(port='3000')