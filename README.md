# Gemini ChatBot AI

A simple chatbot application built with Flask and Google's Gemini AI SDK. This web-based chatbot provides an interactive interface to communicate with Google's Gemini AI model.

## Features

- 🤖 Interactive chat interface powered by Google Gemini AI
- 💬 Conversation history tracking
- 📝 Markdown-formatted responses
- 🎨 Clean and responsive web UI

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13 or higher**
- **uv** (Python package installer) - [Installation guide](https://github.com/astral-sh/uv)
- **Google Gemini API Key** - Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd gemini-chatbot
```

### 2. Install dependencies

This project uses `uv` for dependency management. Install all required packages:

```bash
uv sync
```

Alternatively, if you prefer using `pip`:

```bash
pip install -r requirements.txt
```

> **Note**: If `requirements.txt` doesn't exist, you can generate it from `pyproject.toml`:
> ```bash
> uv pip compile pyproject.toml -o requirements.txt
> ```

### 3. Configure environment variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add the following environment variables to the `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash-exp
```

**Important**: 
- Replace `your_gemini_api_key_here` with your actual Google Gemini API key
- You can use different Gemini models (e.g., `gemini-1.5-pro`, `gemini-1.5-flash`)

## Running the Application

### Using Python directly

```bash
python app.py
```

### Using uv

```bash
uv run python app.py
```

The application will start in debug mode and be accessible at:

```
http://127.0.0.1:5000
```

## Project Structure

```
gemini-chatbot/
├── app.py                  # Application entry point
├── pyproject.toml          # Project dependencies and configuration
├── .env                    # Environment variables (not tracked in git)
├── .gitignore              # Git ignore rules
├── src/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # Application routes and Gemini AI integration
│   ├── models.py          # Database models (if used)
│   ├── database.db        # SQLite database file
│   ├── templates/         # HTML templates
│   │   ├── base.html
│   │   ├── history.html
│   │   └── response_view.html
│   └── static/            # Static files (CSS, JS, images)
└── README.md              # This file
```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Type your question or message in the input field
3. Press Enter or click Send
4. View the AI-generated response in markdown format
5. Access conversation history via the history page

## Dependencies

- **Flask** (>=3.1.2) - Web framework
- **Flask-SQLAlchemy** (>=3.1.1) - Database ORM
- **python-dotenv** (>=0.9.9) - Environment variable management
- **google-genai** (>=1.49.0) - Google Gemini AI SDK
- **markdown** (>=3.10) - Markdown parsing for formatted responses

## Development

To run the application in development mode with auto-reload:

```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

## Troubleshooting

### API Key Issues
- Ensure your `.env` file is in the project root directory
- Verify your Gemini API key is valid and active
- Check that the API key has no extra spaces or quotes

### Module Import Errors
- Ensure all dependencies are installed: `uv sync`
- Verify you're using Python 3.13 or higher: `python --version`

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, port=5001)  # Use a different port
```

## License

[Add your license here]

## Contributing

[Add contributing guidelines here]
