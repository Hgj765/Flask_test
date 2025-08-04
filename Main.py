from flask import Flask, jsonify, render_template, request
from Backend.Benford_calculus import benford_calculus
import os

# Create the Flask app with absolute path to templates

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/message")
def get_message():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/benfords_law")
def Benfords_law():
    return render_template("benford.html")

@app.route("/benford/calculus", methods=['POST'])
def ben_calculus():
    data = request.get_json()
    number = data.get('number')

    # Call your benford calculation function here
    result = benford_calculus(number)  # Implement this function as needed
    return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')