from flask import Flask, render_template, request
import pickle
import numpy as np
from routes.eegML import eeg_routes


#create a simple flask application
app = Flask(__name__)



@app.route("/")

def home():
    return render_template("home.html")

# @app.route("/eegML", methods=["GET", "POST"])
# def eegML():
#     if request.method == "POST":
#         # Get the values from the form
#         electrode_values = [
#             float(request.form.get("AF3")),
#             float(request.form.get("F7")),
#             float(request.form.get("F3")),
#             float(request.form.get("FC5")),
#             float(request.form.get("T7")),
#             float(request.form.get("P7")),
#             float(request.form.get("O1")),
#             float(request.form.get("O2")),
#             float(request.form.get("P8")),
#             float(request.form.get("T8")),
#             float(request.form.get("FC6")),
#             float(request.form.get("F4")),
#             float(request.form.get("F8")),
#             float(request.form.get("AF4"))
#         ]
#         electrode_array = np.array([electrode_values])
#         scaledfeatures = scaler.transform(electrode_array)
#         prediction1 = classifier.predict(scaledfeatures)
#         result = ""
#         if prediction1 == 1:
#             return render_template("eegML.html",result="Eyes Closed" )
#         else:
#             return render_template("eegML.html", result="Eyes Open")

#     return render_template("eegML.html",result="")

app.register_blueprint(eeg_routes)
@app.route("/chatDataAnalyzer")
def chatDataAnalyzer():
    return render_template("chatDataAnalyzer.html")
if __name__ == "__main__":
    app.run(debug=True,port = 3000) 