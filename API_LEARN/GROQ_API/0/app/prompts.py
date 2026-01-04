SYSTEM_PROMPT = "You are a helpful AI assistant ."

def build_chat_prompt(user_input:str):
    return [
        {"role": "system","content": SYSTEM_PROMPT},
        {"role": "user","content": user_input}
    ]