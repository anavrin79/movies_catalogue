from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    movies.append("dupa jana")
    movies.append("tofik gnije")
    movies.append("helena szaleje")
    movies.append("świat sie kończy")
    return render_template("homepage.html", movies=movies)    