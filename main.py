from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/kush")
def kush():
    return "kush resume"


@app.route("/competitiveProgramming")
def prog():
    return render_template("competitiveProgramming.html")


@app.route("/softwareDev")
def soft():
    return render_template("softwareDev.html")


@app.route("/webDev")
def web():
    return render_template("webDev.html")


@app.route("/androidDev")
def android():
    return render_template("androidDev.html")


app.run(debug=True)
