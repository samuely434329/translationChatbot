#pip install google-genai to get api access
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
# secret_key = os.getenv("SECRET_KEY")
# if not secret_key:
#     raise RuntimeError("SECRET_KEY environment variable is not set")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

client = genai.Client(
    api_key=api_key
)

model = "gemini-2.5-flash"
tools = [
    types.Tool(googleSearch=types.GoogleSearch(
    )),
]

if __name__ == "__main__":
    pass

def chatbot_response(user_input: str, target_lang: str = "english") -> str:

    system_instruction = [
    types.Part.from_text(text=f"""You are a language translation tutor. 
    The user will write in SOURCE LANGUAGE. Your task is:
    
    1. Respond in SOURCE LANGUAGE. 
    2. Translate user message from the source language into {target_lang}.
    3. Explain any nuances and special things about the translation.
    4. Respond in {target_lang} keep the conversation going naturally.
    Do not deviate from this role. Only translate and explain.
    4. BE CONCISE AND SIMPLE. For each user word, use at most 8 words in your response. 
    5. After the translation or explanation, continue the conversation in {target_lang}, clarify that you are continuing conversation.
    """)
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        thinking_config=types.ThinkingConfig(thinking_budget=300),
        media_resolution="MEDIA_RESOLUTION_LOW",
        system_instruction=system_instruction,
    )

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=user_input
                ),
            ],
        ),
    ]
    response_text = ""
    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if getattr(chunk, "text", None):
                response_text += chunk.text
    except Exception as e:
        return f"[chatbot error] {e}"
    return response_text


