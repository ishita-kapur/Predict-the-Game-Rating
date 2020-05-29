import os
import sys
import flask
import pickle
import numpy as np
import joblib
#from sklearn.svm import LinearSVR
# Use pickle to load in the pre-trained model.

application_model = r'D:\UTA Spring 2020 Sem II\CSE 5334\Term Project\webapp\model\model_xgboost.joblib'
vectorizer_dump = r'D:\UTA Spring 2020 Sem II\CSE 5334\Term Project\webapp\model\vectorizer.joblib'

loaded_model=joblib.load(application_model)
loaded_vec=joblib.load(vectorizer_dump)

app = flask.Flask(__name__, template_folder='templates')

def roundOf(rating):
    return round(rating * 2) / 2

def ratingPrediction(document):
    X = loaded_vec.transform([document])
    print(type(loaded_model), flush=False)
    y = loaded_model.predict(X)[0]
    return roundOf(y)

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        Comment = flask.request.form['Comment']
        input_variables = Comment
        prediction = ratingPrediction(input_variables)
        return flask.render_template('main.html',
                                     original_input={'Comment':Comment},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()