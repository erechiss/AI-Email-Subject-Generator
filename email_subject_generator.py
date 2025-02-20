import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_email_subject(content, tone="engaging"):
    prompt = f"Generate a catchy and {tone} email subject line for the following email content:\n\n{content}\n\nSubject line:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative copywriter specializing in email marketing."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    content = input("Enter email content: ")
    tone = input("Enter desired tone (e.g., engaging, professional, humorous): ")
    subject = generate_email_subject(content, tone)
    print("\nGenerated Email Subject Line:\n", subject)
