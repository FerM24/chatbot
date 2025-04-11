def preprocess_text(text):
    # Function to clean and prepare text data
    cleaned_text = text.strip().lower()
    return cleaned_text

def format_response(response):
    # Function to format the chatbot's responses
    formatted_response = f"Chatbot: {response}"
    return formatted_response