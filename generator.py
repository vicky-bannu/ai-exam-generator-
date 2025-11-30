import os
from predefined_questions import get_predefined_questions

# Optional import - only needed if using AI generation
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None

class QuestionGenerator:
    def __init__(self, api_key=None, use_predefined=False):
        """
        Initialize the QuestionGenerator with API key.
        
        Args:
            api_key (str): Google Generative AI API key. If None, reads from GOOGLE_API_KEY env var.
            use_predefined (bool): If True, use predefined questions instead of AI generation
        """
        self.use_predefined = use_predefined
        self.api_key = api_key
        
        if not use_predefined:
            if api_key is None:
                api_key = os.getenv("GOOGLE_API_KEY")
            
            if api_key is None:
                # If no API key, fall back to predefined questions
                self.use_predefined = True
            else:
                if not GENAI_AVAILABLE:
                    # If genai not available, use predefined questions
                    self.use_predefined = True
                else:
                    self.api_key = api_key
                    genai.configure(api_key=api_key)
                    self.model = genai.GenerativeModel("gemini-1.5-pro")
    
    def create_questions(self, subject, count, include_answers=True):
        """
        Generate exam questions with answers for a given subject.
        
        Args:
            subject (str): The subject/topic for questions
            count (int): Number of questions to generate
            include_answers (bool): Whether to include answers
        
        Returns:
            list: List of dictionaries with 'question' and 'answer' keys
        """
        # Try predefined questions first (for Java, Python, ML, Database)
        predefined = get_predefined_questions(subject, count)
        if predefined:
            return predefined
        
        # If using predefined mode or no API key, return predefined if available
        if self.use_predefined:
            predefined = get_predefined_questions(subject, count)
            if predefined:
                return predefined
            # If no predefined found, return sample questions
            return [{'question': f"{i+1}. Sample question about {subject}?", 'answer': f"Sample answer for question {i+1}"} for i in range(count)]
        
        # Use AI generation if API key is available and genai is installed
        if not GENAI_AVAILABLE or not hasattr(self, 'model'):
            # Fall back to predefined questions
            predefined = get_predefined_questions(subject, count)
            if predefined:
                return predefined
            return [{'question': f"{i+1}. Sample question about {subject}?", 'answer': f"Sample answer for question {i+1}"} for i in range(count)]
        
        if include_answers:
            prompt = f"""
            Generate {count} exam questions with answers for the subject: {subject}.
            Give easy, medium, and hard mixed questions.
            Format each question and answer pair as:
            Q1: <question>
            A1: <answer>
            Q2: <question>
            A2: <answer>
            etc.
            Make sure answers are clear and concise.
            """
        else:
            prompt = f"""
            Generate {count} simple exam questions for the subject: {subject}.
            Give easy, medium, and hard mixed questions.
            Format each question on a new line starting with a number:
            1. <question>
            2. <question>
            etc.
            """

        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            if include_answers:
                # Parse questions and answers
                questions_with_answers = []
                lines = text.split('\n')
                current_question = None
                current_answer = None
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Check if line starts with Q or Question
                    if line.upper().startswith('Q') and ':' in line:
                        # Save previous pair if exists
                        if current_question and current_answer:
                            questions_with_answers.append({
                                'question': current_question,
                                'answer': current_answer
                            })
                        # Extract question
                        current_question = line.split(':', 1)[1].strip() if ':' in line else line[1:].strip()
                        current_answer = None
                    # Check if line starts with A or Answer
                    elif line.upper().startswith('A') and ':' in line:
                        current_answer = line.split(':', 1)[1].strip() if ':' in line else line[1:].strip()
                    # If we have a question but no answer marker, might be continuation
                    elif current_question and not current_answer:
                        current_question += " " + line
                    elif current_question and current_answer:
                        current_answer += " " + line
                
                # Add last pair
                if current_question:
                    if current_answer:
                        questions_with_answers.append({
                            'question': current_question,
                            'answer': current_answer
                        })
                    else:
                        # If no answer found, create a placeholder
                        questions_with_answers.append({
                            'question': current_question,
                            'answer': f"Answer for: {current_question}"
                        })
                
                # If parsing failed, try alternative format
                if not questions_with_answers:
                    # Fallback: split by numbered questions
                    questions = [q.strip() for q in text.split('\n') if q.strip() and (q.strip()[0].isdigit() or q.strip().upper().startswith('Q'))]
                    questions_with_answers = [{'question': q, 'answer': f'Answer for question {i+1}'} for i, q in enumerate(questions[:count])]
                
                return questions_with_answers[:count] if questions_with_answers else [{'question': f"Question about {subject}?", 'answer': f"Answer about {subject}"} for _ in range(count)]
            else:
                # Original format without answers
                questions = text.split("\n")
                questions = [q.strip() for q in questions if q.strip() and q.strip()[0].isdigit()]
                return [{'question': q, 'answer': ''} for q in questions] if questions else [{'question': f"Question about {subject}?", 'answer': ''} for _ in range(count)]
                
        except Exception as e:
            print(f"Error generating questions: {e}")
            # Return sample questions as fallback
            return [{'question': f"{i+1}. Sample question about {subject}?", 'answer': f"Sample answer for question {i+1}"} for i in range(count)]


