from fpdf import FPDF
import os
import re

class Formatter:
    def make_pdf(self, subject, questions, include_answers=False):
        """
        Create a PDF file with exam questions.
        
        Args:
            subject (str): Subject name
            questions (list): List of questions (strings or dicts with 'question' and 'answer')
            include_answers (bool): Whether to include answers in PDF
        
        Returns:
            str: Filename of the generated PDF
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, f"Exam Paper - {subject}", ln=True, align="C")
        pdf.ln(10)

        # Clean filename for subject
        clean_subject = "".join(c for c in subject if c.isalnum() or c in (' ', '-', '_')).strip()

        # Questions
        for i, q in enumerate(questions, 1):
            # Handle both string and dict formats
            if isinstance(q, dict):
                question_text = q.get('question', str(q))
                answer_text = q.get('answer', '')
            else:
                question_text = str(q)
                answer_text = ''
            
            # Remove leading numbers if present
            question_text = re.sub(r'^\d+[\.\)]\s*', '', question_text).strip()
            
            pdf.set_font("Arial", size=12, style='B')
            pdf.multi_cell(0, 10, f"Q{i}. {question_text}")
            pdf.ln(3)
            
            if include_answers and answer_text:
                pdf.set_font("Arial", size=11, style='I')
                pdf.set_text_color(0, 100, 0)  # Green color for answers
                pdf.multi_cell(0, 8, f"Answer: {answer_text}")
                pdf.set_text_color(0, 0, 0)  # Reset to black
                pdf.ln(3)
            
            pdf.ln(5)

        filename = f"{clean_subject.replace(' ', '_')}_Exam.pdf"
        pdf.output(filename)
        return filename
