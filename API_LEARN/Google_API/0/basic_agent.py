from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key = GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide me Info about the VertexAi",
)

print(response.text)