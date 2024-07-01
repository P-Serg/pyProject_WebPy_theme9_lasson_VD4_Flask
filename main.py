from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
# @app.route("/<password>/")
# def hello_world(password=None):
#     if password == "1234":
#         return f"Доступ разрешен"
#     else:
#         return f"Доступ запрещен"

# def hello_world():
#     html = """
#     <h1>Тестовый запуск локального сервера</h1>
#     <p>просто текст</p>
#     """
#     return html

def herоes():
    return render_template("index.html")
@app.route("/films/")
def films():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
