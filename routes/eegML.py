from flask import Blueprint, render_template, redirect, url_for,request
import pickle
import numpy as np

pickle_in = open('model\model.pkl', 'rb')
classifier = pickle.load(pickle_in)
scaler = pickle.load(open('model\scaler.pkl', 'rb'))
eeg_routes = Blueprint("eeg_routes", __name__)

@eeg_routes.route("/eegML")
def eegML():
    return render_template("eeghome.html")

@eeg_routes.route("/eegML/introduction")
def introduction():
    return render_template("eegIntroduction.html")

@eeg_routes.route("/predict",methods=['POST'])
def prediction():
    int_features = [int(x) for x in request.form.values()]
    print("intial values -->", int_features)
    pre_final_features = [np.array(int_features)]
    final_features = scaler.transform(pre_final_features)
    print("scaled values -->", final_features)
    prediction = classifier.predict(final_features)   
    print('predictio value is ', prediction[0])
    if (prediction[0] == 1):
        output = "Open"
    else:
        output = "Closed"
   
        

    return render_template('eeghome.html', prediction='Based on EEG value your Eye is {}'.format(output))