from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "I am a secret key! Don't share me!"

# this email regex may have some false positives, but at least it
# won't have false negatives like emails container ñ or ö
EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    # custom validations occur here
    valid = True

    if len(request.form["name"]) < 1:
        flash('Name is required', 'name')
        valid = False
    elif len(request.form["name"]) < 2:
        flash('Name must be 2 characters or longer', 'name')
        valid = False

    if len(request.form["email"]) < 1:
        flash('Email is required', 'email')
        valid = False
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash('Invalid email', 'email')
        valid = False

    if valid:
        return redirect("/success")
    else:
        return redirect("/")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)