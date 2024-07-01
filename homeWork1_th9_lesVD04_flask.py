from flask import Flask, render_template
from datetime import datetime

def print_current_datetime():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Текущая дата и время:", formatted_now)

print_current_datetime()

app = Flask(__name__)

@app.route("/")
def date_time():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("dt.html", datetime=formatted_now)

if __name__ == "__main__":
    app.run()