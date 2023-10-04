from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from social_apis.instagram import Instagram
from datetime import date
import sys, os, requests
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
far_llat = os.environ.get("IG_FAR_LLAT")

ig = Instagram(
    client_id=fb_client_id,
    client_secret=fb_secret,
    ll_at=far_llat
)


@app.route('/')
def home():

    #the IG api right now does not allow us to query specific types of content, so we pull it all, and filter it here
    #todo add a method to the IG object that returns only the data type we want. Could be helpful for later
    user_media_data = ig.get_user_media(limit=10)
    user_images = []

    for media in user_media_data["data"]:
        if media["media_type"] == "IMAGE":
            user_images.append(media)
        elif media["media_type"] == "CAROUSEL_ALBUM":
            caption = media["caption"]
            for image in media["children"]["data"]:
                image["caption"] = caption  #IG child edges don't have captions, we need to use the ALBUM'S CAPTIONS
                user_images.append(image)
    

    user_images = user_images[:(len(user_images) %4 * -1)] #get a full block on the home page

    return render_template("home.html", ig_images=user_images)


@app.route("/insta/")
def instagram_imgs():

    user_media_list = ig.get_user_media(limit=15)

    #filter down to just images until we sort out how to handle videos
    user_images = [ media for media in user_media_list["data"] if media["media_type"] != "VIDEO"]

    return render_template("instagram.html", ig_media=user_images)





#     return render_template("gallery.html", ig_images=user_images)


if __name__ == "__main__":
    debug_mode = False
    if "--debug" in sys.argv:
        debug_mode = True
    app.run(host=host, port=port, debug=debug_mode)