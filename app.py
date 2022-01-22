from flask import Flask
#Flask is microframework 

app = Flask(__name__)

@app.route("/")
def butopea():
    return "<p>Hello, butopea!</p>"

if __name__ == "__main__" :
    app.run() 