from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<p>Hey kijk nou, dit werkt!</p>'