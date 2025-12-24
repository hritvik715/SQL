from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key exists: {bool(api_key)}")
print(f"API Key length: {len(api_key) if api_key else 0}")

# Configure the API
genai.configure(api_key=api_key)

try:
    # List available models
    print("\nAvailable models:")
    for model in genai.list_models():
        print(f"- {model.name}")
        if "gemini-pro" in model.name:
            print(f"  ✓ Found Gemini Pro model: {model.name}")
    
    # Try a simple request to Gemini Pro
    print("\nTesting Gemini Pro model:")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello in 5 words")
    print(f"Response: {response.text}")
    print("\nYour API key has access to the Gemini Pro model!")
    
except Exception as e:
    print(f"\nError: {e}")
    print("\nYour API key might not have access to the Gemini Pro model.")