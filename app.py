from flask import Flask, request, render_template
import pickle 

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        nitrogen = request.form["nitrogen"]
        phosphorus = request.form["phosphorus"]
        potassium = request.form["potassium"]
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        ph = request.form["ph"]
        rainfall = request.form["rainfall"]

        crop_predict = model.predict([[nitrogen, phosphorus, potassium,temperature, humidity, ph, rainfall]])[0]
        crop_predict = crop_predict.capitalize()
        
        return render_template("index.html", prediction_text = "The best crop you should grow is {} .".format(crop_predict))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 8000)