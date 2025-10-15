from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

# Load the chatbot model
print("Loading chatbot model, please wait...")
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Chatbot model loaded successfully!")

conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])

def handle_prompt():
    # Read prompt from HTTP request body
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Combine convo history
    history = "\n".join(conversation_history)

    # Tokenize input text + history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate response
    outputs = model.generate(**inputs, max_length=60)

    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    # Return chatbot reply as plain text
    return response

if __name__ == '__main__':
    app.run()
    