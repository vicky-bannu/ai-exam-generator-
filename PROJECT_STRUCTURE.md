# Project Structure

## Core Files

### Backend (Python)
- **api_server.py** - Flask REST API server
  - Handles `/generate` endpoint for question generation
  - Handles `/evaluate` endpoint for answer evaluation
  - Serves PDF files via `/pdf/<filename>`
  
- **generator.py** - Question generation module
  - Uses predefined questions (no API key required)
  - Can use AI generation if API key provided
  
- **formatter.py** - PDF generation module
  - Creates PDF files with questions and answers
  
- **evaluator.py** - Answer evaluation module
  - Evaluates student answers using AI (requires API key)
  
- **predefined_questions.py** - Question database
  - Contains 10 questions each for:
    - Python
    - Java
    - Machine Learning
    - Database

### Frontend
- **index.html** - Single-page web application
  - Self-contained HTML/CSS/JavaScript
  - No external dependencies
  - Connects to API server at localhost:5000

### Configuration
- **requirements.txt** - Python package dependencies
- **start.bat** - Quick start script for Windows
- **README.md** - Project documentation
- **.gitignore** - Git ignore rules

## Data Flow

```
User (Browser)
    ↓
index.html (Frontend)
    ↓ HTTP POST
api_server.py (Backend)
    ↓
generator.py → predefined_questions.py
    ↓
Returns JSON with questions & answers
    ↓
index.html displays results
```

## File Dependencies

```
api_server.py
  ├── generator.py
  ├── formatter.py
  ├── evaluator.py
  └── predefined_questions.py

generator.py
  └── predefined_questions.py

formatter.py
  └── (standalone)

evaluator.py
  └── (standalone, optional google-generativeai)
```

## Generated Files (ignored by git)

- `*.pdf` - Generated exam PDFs
- `__pycache__/` - Python cache files

