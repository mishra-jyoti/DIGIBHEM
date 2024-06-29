from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    [
        r"how are you?",
        ["I am doing well, thank you.", "I am great! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"(.*) age?",
        ["I am a computer program, age doesn't apply to me.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am a chatbot, I exist in the virtual world.",]
    ],
]

# Initialize chatbot with NLTK Chat class
chatbot = Chat(pairs, reflections)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for getting chatbot response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    bot_response = chatbot.respond(user_message)
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
