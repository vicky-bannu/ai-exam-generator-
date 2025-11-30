"""
Flask API Server for AI Exam Generator
Provides REST endpoints for the frontend HTML application
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from generator import QuestionGenerator
from formatter import Formatter
from evaluator import Evaluator
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store API key in app config (can be set via environment variable)
app.config['API_KEY'] = os.getenv('GOOGLE_API_KEY')

# Initialize components (will be initialized with API key when needed)
generator = None
evaluator = None
formatter = Formatter()


def get_api_key():
    """Get API key from environment or request header"""
    # Try environment variable first
    api_key = os.getenv('GOOGLE_API_KEY')
    
    # Try request header (if frontend sends it)
    if not api_key and request.headers.get('X-API-Key'):
        api_key = request.headers.get('X-API-Key')
    
    return api_key


def initialize_components(api_key=None, use_predefined=False):
    """Initialize generator and evaluator with API key"""
    global generator, evaluator
    
    if not api_key:
        api_key = get_api_key()
    
    # Use predefined questions if no API key (for Java, Python, ML, Database)
    if not api_key:
        use_predefined = True
    
    generator = QuestionGenerator(api_key=api_key, use_predefined=use_predefined)
    
    # Only initialize evaluator if we have API key
    if api_key:
        evaluator = Evaluator(api_key=api_key)
    else:
        evaluator = None


@app.route('/generate', methods=['POST'])
def generate_exam():
    """Generate exam questions endpoint"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        subject = data.get('subject', '').strip()
        num_questions = data.get('num_questions', 5)
        
        if not subject:
            return jsonify({'error': 'Subject is required'}), 400
        
        if not isinstance(num_questions, int) or num_questions < 1:
            num_questions = 5
        
        # Initialize components (will use predefined questions if no API key)
        api_key = get_api_key()
        use_predefined = not bool(api_key)
        initialize_components(api_key, use_predefined=use_predefined)
        
        # Generate questions with answers (will use predefined if available)
        questions_data = generator.create_questions(subject, num_questions, include_answers=True)
        
        # Create PDF (with answers) - pass full questions_data
        try:
            pdf_filename = formatter.make_pdf(subject, questions_data, include_answers=True)
            pdf_url = f"/pdf/{pdf_filename}"
        except Exception as e:
            print(f"Error creating PDF: {e}")
            pdf_url = None
        
        return jsonify({
            'questions': questions_data,  # Return full data with answers
            'pdf_url': pdf_url,
            'subject': subject,
            'num_questions': len(questions_data)
        }), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/evaluate', methods=['POST'])
def evaluate_answer():
    """Evaluate student answer endpoint"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        question = data.get('question', '').strip()
        answer = data.get('answer', '').strip()
        
        if not question:
            return jsonify({'error': 'Question is required'}), 400
        
        if not answer:
            return jsonify({'error': 'Answer is required'}), 400
        
        # Initialize components (evaluation requires API key)
        api_key = get_api_key()
        if not api_key:
            return jsonify({'error': 'API key required for evaluation. Set GOOGLE_API_KEY environment variable.'}), 500
        
        initialize_components(api_key, use_predefined=False)
        
        if not evaluator:
            return jsonify({'error': 'Evaluator not initialized. API key required.'}), 500
        
        # Evaluate answer
        evaluation_text = evaluator.check_answer(question, answer)
        
        # Parse score and feedback from the evaluation text
        score = None
        feedback = evaluation_text
        
        # Try to extract score from text (format: "Score: 8" or "Score: 8/10")
        score_match = re.search(r'Score:\s*(\d+)', evaluation_text, re.IGNORECASE)
        if score_match:
            score = int(score_match.group(1))
            # Remove score line from feedback
            feedback = re.sub(r'Score:\s*\d+.*?\n', '', evaluation_text, flags=re.IGNORECASE).strip()
        
        # Try to extract feedback section
        feedback_match = re.search(r'Feedback:\s*(.+)', evaluation_text, re.IGNORECASE | re.DOTALL)
        if feedback_match:
            feedback = feedback_match.group(1).strip()
        
        return jsonify({
            'score': score,
            'feedback': feedback,
            'evaluation': evaluation_text
        }), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/pdf/<filename>', methods=['GET'])
def get_pdf(filename):
    """Serve PDF files"""
    try:
        # Security: only allow PDF files from current directory
        if not filename.endswith('.pdf'):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Remove any path traversal attempts
        filename = os.path.basename(filename)
        filepath = os.path.join(os.getcwd(), filename)
        
        if not os.path.exists(filepath):
            return jsonify({'error': 'PDF file not found'}), 404
        
        return send_file(filepath, mimetype='application/pdf', as_attachment=True)
        
    except Exception as e:
        return jsonify({'error': f'Error serving PDF: {str(e)}'}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'api_key_configured': bool(get_api_key())
    }), 200


if __name__ == '__main__':
    print("=" * 50)
    print("AI Exam Generator API Server")
    print("=" * 50)
    print("\nStarting server on http://localhost:5000")
    print("\nMake sure to set GOOGLE_API_KEY environment variable")
    print("Example: set GOOGLE_API_KEY=your_api_key_here")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True)

