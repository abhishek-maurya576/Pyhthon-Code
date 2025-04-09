import requests
import json

# Replace with your actual Gemini API Key
API_KEY = "TODO"

# Use the correct Gemini 2.0 Flash model endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def get_user_input():
    subject = input("Enter the subject: ")
    topic = input("Enter the topic: ")
    sub_topic = input("Enter the sub-topic (optional): ")
    question = input("Type your question (optional, press Enter to skip): ")
    return subject, topic, sub_topic, question

def generate_prompt(subject, topic, sub_topic, question):
    prompt = f"Generate educational content for the subject '{subject}', topic '{topic}'."    
    if sub_topic.strip():
        prompt += f" Sub-topic: '{sub_topic}'."
    if question.strip():
        prompt += f" Specifically, answer this question: '{question}'."
    else:
        prompt += " Provide an explanation and key points."
    return prompt

def make_gemini_api_call(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        try:
            content = response_json['candidates'][0]['content']['parts'][0]['text']
            return content
        except (KeyError, IndexError):
            return "Failed to parse Gemini API response."
    else:
        return f"API call failed with status code {response.status_code}: {response.text}"

def main():
    subject, topic, sub_topic, question = get_user_input()
    prompt = generate_prompt(subject, topic, sub_topic, question)

    print("\n--- Sending request to Gemini API ---\n")
    response_content = make_gemini_api_call(prompt)

    print("\n--- Gemini API Response ---\n")
    print(response_content)

if __name__ == "__main__":
    main()
