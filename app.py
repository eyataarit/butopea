from flask import Flask
#Flask is microframework 

app = Flask(__name__)

@app.route("/")
def butopea():
    return "Here you can find the XML file shown, and you can downloaded it"

if __name__ == "__main__" :
    app.run() 