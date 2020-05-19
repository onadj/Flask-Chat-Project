import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello There!</h2>"


app.run(os.getenv('IP'), os.getenv('PORT'))