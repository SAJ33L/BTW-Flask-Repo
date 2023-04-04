from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():

    return render_template("index.html")

@app.route("/result")
def result():
    
    output = request.form.to_dict()
    name = output[name]
    city = output[city]

    return render_template("index.html", nme =name, shehr = city)