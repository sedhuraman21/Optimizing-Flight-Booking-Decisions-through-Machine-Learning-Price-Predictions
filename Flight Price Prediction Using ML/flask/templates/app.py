from flask import Flask,render_template,request
import numpy as np
import pickle
model = pickle.load(open(r"model1.pkl",'rb'))
app= Flask(__name__)
@app.route('/home')
def home():
    return render_template('home.html')
@app.route("/predict")
def home1():
     return render_template('predict.html')
@app.route("/pred", methods=['POST','GET'])
def predict():
     x = [[int(x) for x in request.form.values()]]
     print (x)
     x = np.array(x)
     print(x.shape)
     print(x) 
     pred = model.predict(x)
     print(pred)
     return render_template('submit.html', prediction_text=pred)
if __name__ =="__main__":
     app.run(debug=False)