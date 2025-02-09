from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from config import db
from models import User
import requests

auth = Blueprint("auth", __name__, url_prefix="/auth")

# You would replace this with the actual endpoint you need to send the POST request to
SERVER_URL = "https://app.speckle.systems"
CHALLENGE = '123'  # Your challenge key
TOKEN = 'token'
REFRESH_TOKEN = 'refresh_token'


@auth.route('')
def exchange_access_code():
    # The access code will be included as a query parameter in the URL
    access_code = request.args.get('access_code')
    print(access_code)
    # Ensure access code and other necessary parameters are present
    if not access_code:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Prepare the data to send to the token endpoint
    payload = {
        'accessCode': access_code,
        'appId': "23663a9bda",
        'appSecret': "d556c6c8f9",
        'challenge': "123"  # Retrieve challenge from the session
    }

    try:
        # Send the request to the external API (equivalent to `fetch` in JS)
        response = requests.post(f"{SERVER_URL}/auth/token/", json=payload)
        response_data = response.json()

        if response.status_code == 200 and 'token' in response_data:
            # If the response contains a token, store the token and refresh token in session
            session[TOKEN] = response_data['token']
            session[REFRESH_TOKEN] = response_data['refreshToken']

            # Remove challenge if successfully retrieved the token
            session.pop(CHALLENGE, None)

            return jsonify({'message': 'Tokens exchanged successfully', 'token': response_data['token'], 'refreshToken': response_data['refreshToken']}), 200
        else:
            return jsonify({'error': 'Failed to exchange access code for token', 'details': response_data}), 400

    except requests.exceptions.RequestException as e:
        # Handle any request errors (e.g., network issues)
        return jsonify({'error': 'An error occurred while contacting the server', 'details': str(e)}), 500




# Route for user login and JWT creation
@auth.route("/login", methods=["POST", "GET"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Generate JWT token for authenticated user
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

# Route for user registration
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"), method="sha256")

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify(message="User already exists"), 400

    # Create and add new user to the database
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201
