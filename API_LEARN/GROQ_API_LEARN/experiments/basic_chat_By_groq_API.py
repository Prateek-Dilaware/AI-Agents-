from app.chat import chat_completion

if __name__ == "__main__":
    question = "Summarize the attention is all you need Paper in Short"
    answer = chat_completion(question)
    print("\n AI response : \n")
    print(answer)