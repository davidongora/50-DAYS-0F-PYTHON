from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample list of technical questions
questions = [
    {
        "id": 1,
        "title": "Generate 10 random emails and print the usernames.",
        "description": "Write a program that generates 10 random email addresses and prints only the usernames."
    },
    {
        "id": 2,
        "title": "Reverse a string.",
        "description": "Write a program that takes a string as input and prints the reverse of that string."
    },
    # Add more questions here
]

@app.route('/api/question', methods=['GET'])
def get_random_question():
    random_question = random.choice(questions)
    return jsonify(random_question)

@app.route('/api/submit', methods=['POST'])
def submit_code():
    # Assuming the submitted code is in a file named 'code_file'
    code_file = request.files.get('code_file')
    # Process the code file and evaluate the submission
    # You can store the code file for later evaluation or perform immediate evaluation here

    # Return a response indicating successful submission
    return jsonify({"message": "Code submitted successfully."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
