from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="font-size:300%;background-color:pink;"><center>liron + adir = perfect gay couple!</center><body>'

app.run(host='0.0.0.0', port=8081)
