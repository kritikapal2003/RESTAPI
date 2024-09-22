from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.json
        # Process the data and return response
        return jsonify({
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": [x for x in data["data"] if x.isdigit()],
            "alphabets": [x for x in data["data"] if x.isalpha()],
            "highest_lowercase_alphabet": [max(filter(str.islower, data["data"]), default="")],
            "file_valid": True,  # You would implement file validation logic here
            "file_mime_type": "image/png",  # Replace with actual MIME type
            "file_size_kb": "400"  # Replace with actual size
        })
    else:
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)


