# Task 6: Import the request module
from flask import Blueprint, render_template

# Task 6: Import markdown

# Task 1: Get Gemini API

routes = Blueprint('routes', __name__)

# Task 5: Add the ask function


# Task 3, 6, 9: Change the code below
@routes.route('/')
def home():
    return "Welcome to Educative!"