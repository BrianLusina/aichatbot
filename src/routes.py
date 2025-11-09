# Task 6: Import the request module
import os
from flask import Blueprint, render_template, request
from dotenv import load_dotenv
from google import genai
import markdown

# Task 6: Import markdown

# Task 1: Get Gemini API
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")
genai_client = genai.Client(api_key=api_key)

routes = Blueprint('routes', __name__)

history_data=[]

@routes.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        query = request.args.get('query')
        if query == "" or query is None:
            return render_template("response_view.html")
        response = ask(query)
        formatted_response = markdown.markdown(response)
        query_message = {"messageType": "other-message", "message": query}
        response_message = {"messageType": "my-message", "message": formatted_response}
        history_data.append(query_message)
        history_data.append(response_message)
        return render_template("response_view.html", results=[query_message, response_message])
    else:
        return render_template("history.html", results=history_data)


def ask(question: str) -> str:
    response = genai_client.models.generate_content(model=model, contents=question)

    return response.text.strip()