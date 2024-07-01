from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def person():
    return render_template("index.html")

@app.route("/films/")
def films():
    return render_template("films.html")

if __name__ == "__main__":
    app.run()
