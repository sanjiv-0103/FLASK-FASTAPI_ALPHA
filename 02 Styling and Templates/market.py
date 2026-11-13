from flask import Flask, render_template

app = Flask(__name__) # built in variable refer to local py file ; parameter for flask
@app.route('/') # decorator- one step before to create the function; root url
@app.route('/home') # result in fixing the error msg that we get will inc other route /home
#def hello_world(): # without hardcoding
    #return '<h1>Hello World</h1>' # to make a heading  ; http://127.0.0.1:5000 

def home_page():
    return render_template('home.html') # It handles request and directs to html files

#to refer how routing works
#set FAST_APP=market.py
#new route