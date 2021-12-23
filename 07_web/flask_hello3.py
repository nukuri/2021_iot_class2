from flask import Flask, render_template

app = Flask(__name__)

#0.0.0.0:5000
@app.route("/")
def hello():
    return render_template(
    "hello.html",
    title="Hello, Flask")
       
@app.route("/first")
def first():
    return render_template(
        "first.html",
        title="First Page")

@app.route("/second")
def first():
    return render_template(
        "second.html",
        title="Second Page")


if __name__=="__main__":
    app.run(host="0.0.0.0")
