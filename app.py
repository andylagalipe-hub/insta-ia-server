from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Server is running"

@app.route("/reply", methods=["POST"])
def reply():
    data = request.get_json()
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Tu es une femme séduisante, naturelle, jamais vulgaire. Tu flirtes légèrement et poses une question."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        max_tokens=60
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })
