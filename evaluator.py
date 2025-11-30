import os

# Optional import - only needed if using AI evaluation
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None

class Evaluator:
    def __init__(self, api_key=None):
        """
        Initialize the Evaluator with API key.
        
        Args:
            api_key (str): Google Generative AI API key. If None, reads from GOOGLE_API_KEY env var.
        """
        if api_key is None:
            api_key = os.getenv("GOOGLE_API_KEY")
        
        if api_key is None:
            raise ValueError("API key required. Set GOOGLE_API_KEY environment variable or pass api_key parameter.")
        
        if not GENAI_AVAILABLE:
            raise ValueError("google-generativeai package not installed. Install it with: pip install google-generativeai")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")
    
    def check_answer(self, question, student_answer):
        """
        Evaluate a student's answer against a question.
        
        Args:
            question (str): The exam question
            student_answer (str): Student's answer
        
        Returns:
            str: Evaluation with score and feedback
        """
        prompt = f"""
        Question: {question}
        Student Answer: {student_answer}

        Give a score from 1 to 10.
        Give very short feedback.
        Format:
        Score: <number>
        Feedback: <short text>
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error evaluating answer: {e}\nScore: N/A\nFeedback: Unable to evaluate at this time."
