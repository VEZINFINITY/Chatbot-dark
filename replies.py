# replies.py
def get_smart_reply(message_text: str) -> str | None:
    text = message_text.lower()

    if "hello" in text or "hi" in text:
        return "Hey there! 👋 How can I help you today?"
    elif "price" in text:
        return "Our pricing depends on the service. Can you tell me what you're looking for?"
    elif "help" in text:
        return "Sure! You can ask about our features, support, or pricing."
    elif "bye" in text:
        return "Goodbye! 👋 Come back anytime."
    else:
        return None  # fallback to AI
