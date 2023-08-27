from flask import Flask, render_template, request
import pickle
import numpy as np
from routes.eegML import eeg_routes


#create a simple flask application
app = Flask(__name__)



@app.route("/")

def home():
    return render_template("home.html")

app.register_blueprint(eeg_routes)
@app.route("/chatDataAnalyzer")
def chatDataAnalyzer():
    return render_template("chatDataAnalyzer.html")
if __name__ == "__main__":
    app.run(debug=True,port = 3000) 
