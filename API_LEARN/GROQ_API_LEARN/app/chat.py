from app.client import get_groq_client
from app.prompts import build_chat_prompt

def chat_completion(
    user_input: str,
    model: str = "openai/gpt-oss-120b",
    temperature: float = 0.7,
    max_tokens: int = 512
):
    client = get_groq_client()

    response = client.chat.completions.create(
        model=model,
        messages=build_chat_prompt(user_input),
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
