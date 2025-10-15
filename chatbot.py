"""
Simple Chatbot using Hugging Face Transformers
Author: Kevin Lee
Description: A minimal conversational chatbot using facebook/blenderbot-400M-distill.
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model (downloads on first run, then uses local cache)
print("Loading model, please wait... :)")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Model loaded successfully! Thank you for your patience!")

conversation_history = []

print("Chatbot is ready! Type 'quit' or press Ctrl+C to exit.\n")

while True:
    try:
        # Create conversation history string
        history_string = "\n".join(conversation_history)

        # Get input from user
        input_text = input("> ")
        if input_text.lower() in {"quit", "exit"}:
            print("Chatbot: Goodbye!")
            break

        # Tokenize input text and history
        inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

        # Generate response
        outputs = model.generate(**inputs)

        # Decode response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Display response
        print(f"Chatbot: {response}\n")

        # Update conversation history
        conversation_history.append(input_text)
        conversation_history.append(response)

    except KeyboardInterrupt:
        print("\n👋 Chatbot: Conversation ended.")
        break
