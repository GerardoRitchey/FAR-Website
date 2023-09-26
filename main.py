from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date
import sys, os, requests
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

#load load environment variables
load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET")
Bootstrap5(app)

host = os.environ.get("FLASK_HOST")
port = os.environ.get("FLASK_PORT")

fb_client_id = os.environ.get("FB_APP_ID")
fb_secret = os.environ.get("FB_APP_SECRET")

oauth = OAuth(app)

# Instagram OAuth Configuration
oauth.register(
    name='instagram',
    client_id= fb_client_id,
    client_secret= fb_secret, 
    authorize_url='https://api.instagram.com/oauth/authorize',
    authorize_params=None,
    authorize_params_callback=None,
    authorize_url_params=None,
    fetch_token='https://api.instagram.com/oauth/access_token',
    fetch_token_params=None,
    fetch_token_method='POST',
    client_kwargs={'scope': 'user_profile,user_media'},
)




@app.route('/')
def home():

    return render_template("home.html")


@app.route("/insta/")
def instagram_imgs():


    return render_template("instagram.html")


@app.route("/login")
def login():
    redirect_uri = url_for('authorize', _external=True)

    return oauth.instagram.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.instagram.authorize_access_token()
    session['token'] = token
    return redirect(url_for('profile'))


# Display Instagram Profile
@app.route('/profile')
def profile():
    token = session.get('token')
    if token is None:
        return 'Not authenticated.'
    user_info = oauth.instagram.get('me', token=token)
    return f'Instagram User ID: {user_info["id"]}, Username: {user_info["username"]}'


if __name__ == "__main__":
    debug_mode = False
    if "--debug" in sys.argv:
        debug_mode = True
    app.run(host=host, port=port, debug=debug_mode)