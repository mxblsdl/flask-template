from app import init_app

""""
Main application file that runs the app. The init_app function builds the flask app 
with the dash component
"""

app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
