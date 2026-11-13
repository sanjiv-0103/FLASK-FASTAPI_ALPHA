from flask import Flask
# Create the Flask application
app = Flask(__name__)

# Home page
@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

# Dynamic route-username changes based on the URL
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

#run it using - flask --app app run

#default local URL: http://127.0.0.1:5000

#enable debug mode: flask --app app run --debug

#dynamic URL:
# http://127.0.0.1:5000/about/Sanjii