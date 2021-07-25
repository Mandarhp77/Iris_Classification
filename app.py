
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('IRIS_RFC.pkl', 'rb'))

    
@app.route('/',methods=['GET'])
def Home():
    return render_template('indexx.html')

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        spl = float(request.form["spl"])
        spw = float(request.form["spw"])
        ptl = float(request.form["ptl"])
        ptw = float(request.form["ptw"])
  
        prediction = model.predict([[spl,spw,ptl,ptw]])

        return render_template('indexx.html',prediction_text="The Class is {}".format(prediction))
    else:
        return render_template('indexx.html')

if __name__=="__main__":
    app.run()