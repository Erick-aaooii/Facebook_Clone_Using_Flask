from flask import Flask, render_template, url_for, request 

app = Flask(__name__, template_folder="html_folder", static_folder="styles")


@app.route('/')
def hompage():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)