from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date
import os


host = os.environ.get("FLASK_HOST")
port = os.environ.get("FLASK_PORT")

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():



    return render_template("home.html")



if __name__ == "__main__":
    app.run(host=host, port=port, debug=False)