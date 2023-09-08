from flask import Flask, request

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json
        user_id = '{}_{}'.format(data['name'], data['dob'])
        email = data['email']
        roll_number = data['roll_number']
        numbers = data['numbers']
        alphabets = data['alphabets']
        highest_alphabet = max(alphabets, key=lambda x: x.upper())

        response = {
            'is_success': True,
            'user_id': user_id,
            'email': email,
            'roll_number': roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_alphabet': highest_alphabet,
        }

        return response, 200

    else:
        response = {
            'operation_code': 1
        }

        return response, 200

if __name__ == '__main__':
    app.run(debug=True)
