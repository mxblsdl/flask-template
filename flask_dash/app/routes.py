from flask import current_app as app, render_template


@app.route("/")
@app.route("/index")
def index():

    return render_template("index.html", content="Welcome to Flask", title="Flask-Dash")
