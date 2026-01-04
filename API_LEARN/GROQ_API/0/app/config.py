import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ API not founbd in environment")
else :
    print(" GROQ API KEY is present we are ready to proceed further ")