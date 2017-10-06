from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
    name = request.form['name']
    clan = request.form['clan']
    text = request.form['text']
    return render_template('results.html', name=name, clan=clan, text=text)

# @app.route('/results')
# def results():
#     return render_template('results.html', name=name, clan=clan, text=text)

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/news')
def dojosnews():


    return render_template('dojos.html', something="some news")

app.run(debug=True)
