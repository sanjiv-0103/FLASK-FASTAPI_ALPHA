from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '788d982fee41b6615507ef63de0226eeca5ac1e93628c753a74b34f0565e086c'
db = SQLAlchemy(app)
from market import routes