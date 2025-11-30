# AI Exam Generator

A web-based application to generate, download, and evaluate exam questions with answers.

## Features

- Generate exam questions with answers for multiple subjects
- Download questions as PDF
- Evaluate student answers
- Predefined questions for: Python, Java, Machine Learning, Database
- Works without API key (uses predefined questions)

## Project Structure

```
ai-exam-project/
├── api_server.py           # Flask API server (backend)
├── generator.py            # Question generation logic
├── formatter.py            # PDF generation
├── evaluator.py            # Answer evaluation
├── predefined_questions.py  # Predefined Q&A database
├── index.html              # Web frontend (single-page app)
├── requirements.txt       # Python dependencies
├── start.bat               # Quick start script (Windows)
└── README.md               # This file
```

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **(Optional) Set API Key for AI evaluation:**
```bash
set GOOGLE_API_KEY=your_api_key_here
```
Note: API key is optional. The app works with predefined questions without it.

## How to Run

### Windows (Easiest)
Double-click `start.bat` - it will:
- Start the API server
- Open the web interface in Edge browser

### Manual Start

1. **Start the API server:**
```bash
python api_server.py
```

2. **Open the web interface:**
- Open `index.html` in your web browser
- Or navigate to: `file:///path/to/ai-exam-project/index.html`

The API server runs on `http://localhost:5000`

## Usage

1. Select a subject (Python, Java, Machine Learning, or Database)
2. Choose number of questions (1-20)
3. Click "Generate Exam"
4. View questions with answers (click "Show Answer" to reveal)
5. Download PDF or evaluate student answers

## Available Subjects

- **Python** - 10 predefined questions
- **Java** - 10 predefined questions  
- **Machine Learning** - 10 predefined questions
- **Database** - 10 predefined questions

## API Endpoints

- `POST /generate` - Generate exam questions
  - Body: `{"subject": "Python", "num_questions": 5}`
- `POST /evaluate` - Evaluate student answer
  - Body: `{"question": "...", "answer": "..."}`
- `GET /pdf/<filename>` - Download PDF file
- `GET /health` - Health check

## Requirements

- Python 3.7+
- Flask
- flask-cors
- fpdf

Optional (for AI features):
- google-generativeai

## License

Free to use and modify.
