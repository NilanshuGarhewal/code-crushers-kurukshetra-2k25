import flask
from flask import Flask, request, jsonify
from manual import train_model, compute_username_features, map_account_type, predict_account_type, main 

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def detect():
    data = request.get_json()
    train_model(data['data'])
    return jsonify({'message': 'Model trained successfully'})