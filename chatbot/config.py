import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment.")

openai = OpenAI()
MODEL = "gpt-4o-mini"

system_message = (
    "You are a helpful assistant for an Airline called FlightAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "Always be accurate. If you don't know the answer, say so."
)
