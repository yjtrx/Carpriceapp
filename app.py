import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('reg.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    features = [str(x) for x in request.form.values()]
    cylinders = int(features[0])
    print(cylinders)
    displacement = float(features[1])
    horsepower = float(features[2])
    weight = int(features[3])
    acceleration = float(features[4])
    model_year = int(features[5])
    origin_america = int(features[6])
    origin_asia = int(features[7])
    final_features = []

    final_features.append(cylinders)
    final_features.append(displacement)
    final_features.append(horsepower)
    final_features.append(weight)
    final_features.append(acceleration)
    final_features.append(model_year)
    final_features.append(origin_america)
    final_features.append(origin_asia)
    print(len(final_features))
    prediction = model.predict([final_features])
    output = round(prediction[0],4)
    return render_template('index.html',prediction_text=output)

if __name__=="__main__":
    app.run(debug=True)
