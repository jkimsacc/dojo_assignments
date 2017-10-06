from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("index.html", name="Joseph")

app.run(debug=True)
