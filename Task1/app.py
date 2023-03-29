from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    city = output["city"]
    age = output["age"]
    school = output["school"]
    session_one = output["session_one"]
    college = output["college"]
    session_two = output["session_two"]
    university = output["university"]
    session_three = output["session_three"]

    return render_template("bio.html", name = name, age = age, city = city,
                           school = school, college = college, university = university, session_one = session_one,
                           session_two = session_two, session_three = session_three)


if __name__ == '__main__':
    app.run(debug= True, port = 5001)