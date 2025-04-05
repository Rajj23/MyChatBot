from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


genai.configure(api_key="AIzaSyAnyr1aU1MIIOdp2YdhFcZhf-RYs6WDYyE")  


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")


app = Flask(__name__)


def get_gemini_career_advice(user_input):
    prompt = f"""
You are an expert career advisor chatbot. The user said: "{user_input}"

Please reply with:
- 3 to 5 possible career options
- Required skills
- Recommended degrees or certifications
- A short reason why those careers match the user's interest

Use bullet points for clarity.
"""

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Sorry, there was an error: {str(e)}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    if not user_message.strip():
        return jsonify({"reply": "Please tell me what you're interested in!"})
    
    reply = get_gemini_career_advice(user_message)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
