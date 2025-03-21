from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import util

@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    response = jsonify({
        'city': util.get_city_names()
    })
    response.headers.add('Access-Control-Allow_Origin','*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    City = request.form['City']
    bath = int(request.form['bath'])
    beds = int(request.form['beds'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(City, sqft, bath, beds)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()

