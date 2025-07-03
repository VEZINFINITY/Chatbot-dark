# ai_reply.py
import openai
import config

openai.api_key = config.OPENAI_API_KEY

def get_ai_reply(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful Telegram chatbot."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return "Hmm, I’m having trouble thinking right now. Please try again later."
