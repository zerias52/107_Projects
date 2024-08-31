from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask!"

@app.get("/about")
def about():
    me = {"name": "Brett Byrd"}
    return json.dumps(me)

@app.get("/footer")
def footer():
    page_name = {"pageName": "organika"}
    return json.dumps(page_name)
#Create an API to a footer that contains the name of the page

app.run(debug=True)