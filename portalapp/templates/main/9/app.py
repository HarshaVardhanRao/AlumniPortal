from flask import Flask, request, jsonify
from twilio.rest import Client
import random

app = Flask(__name__)

# Twilio configurations (replace with your credentials)
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Dictionary for storing OTPs (temporary storage, replace with secure storage)
user_data = {}

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data['email']
        year = data['year']
        phone = data['phone']

        # Generate a random OTP
        otp = random.randint(100000, 999999)

        # Send OTP to user's phone number
        message = client.messages.create(
            body=f'Your OTP for alumni registration is {otp}',
            from_=TWILIO_PHONE_NUMBER,
            to=phone
        )

        # Store OTP in temporary storage
        user_data[email] = {'year': year, 'phone': phone, 'otp': otp}

        return jsonify(success=True)
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Registration error: {e}")
        return jsonify(success=False, error="An error occurred during registration."), 500

if __name__ == '__main__':
    app.run(debug=True)