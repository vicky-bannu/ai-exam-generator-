"""
Predefined Questions and Answers for Java, Python, Machine Learning, and Database
"""

PREDEFINED_QUESTIONS = {
    "Java": [
        {
            "question": "What is Object-Oriented Programming (OOP) in Java?",
            "answer": "OOP is a programming method based on classes and objects. It uses concepts like inheritance, polymorphism, encapsulation, and abstraction."
        },
        {
            "question": "What is the difference between an abstract class and an interface?",
            "answer": "Abstract class can contain both abstract and non-abstract methods. Interface contains only abstract methods (before Java 8). A class can extend one abstract class but implement multiple interfaces."
        },
        {
            "question": "What is JVM?",
            "answer": "JVM (Java Virtual Machine) runs Java bytecode and provides memory management, garbage collection, and execution engine."
        },
        {
            "question": "What is exception handling in Java?",
            "answer": "Exception handling is used to handle runtime errors using try, catch, finally, throw, and throws."
        },
        {
            "question": "What is multithreading?",
            "answer": "Multithreading allows multiple parts of a program to run concurrently for better performance."
        },
        {
            "question": "What is the difference between == and equals() in Java?",
            "answer": "== compares references (memory addresses) for objects, while equals() compares the actual content/value of objects."
        },
        {
            "question": "What is a constructor in Java?",
            "answer": "A constructor is a special method used to initialize objects. It has the same name as the class and no return type."
        },
        {
            "question": "What is method overloading?",
            "answer": "Method overloading allows multiple methods with the same name but different parameters in the same class."
        },
        {
            "question": "What is method overriding?",
            "answer": "Method overriding occurs when a subclass provides a specific implementation of a method already defined in its parent class."
        },
        {
            "question": "What is the difference between String, StringBuffer, and StringBuilder?",
            "answer": "String is immutable. StringBuffer is mutable and thread-safe. StringBuilder is mutable but not thread-safe (faster)."
        }
    ],
    "Python": [
        {
            "question": "What are key features of Python?",
            "answer": "Easy syntax, interpreted, dynamically typed, huge libraries, supports OOP."
        },
        {
            "question": "What is the difference between list and tuple?",
            "answer": "List is mutable, tuple is immutable."
        },
        {
            "question": "What is a function in Python?",
            "answer": "A function is a reusable block of code declared using 'def'."
        },
        {
            "question": "What are lambda functions?",
            "answer": "Anonymous one-line functions used for short operations."
        },
        {
            "question": "Explain exception handling in Python.",
            "answer": "Uses try, except, else, finally blocks to handle runtime errors."
        },
        {
            "question": "What is the difference between append() and extend() in Python lists?",
            "answer": "append() adds a single element to the end of the list. extend() adds all elements from an iterable to the list."
        },
        {
            "question": "What is a dictionary in Python?",
            "answer": "A dictionary is an unordered collection of key-value pairs, enclosed in curly braces {}."
        },
        {
            "question": "What is list comprehension?",
            "answer": "List comprehension is a concise way to create lists using a single line of code with a for loop inside square brackets."
        },
        {
            "question": "What is the difference between __str__ and __repr__?",
            "answer": "__str__ returns a human-readable string representation. __repr__ returns an unambiguous string representation for developers."
        },
        {
            "question": "What are decorators in Python?",
            "answer": "Decorators are functions that modify the behavior of other functions without changing their code."
        }
    ],
    "Machine Learning": [
        {
            "question": "What is Machine Learning?",
            "answer": "Machine Learning is a field of AI where computers learn patterns from data to make predictions."
        },
        {
            "question": "What are the types of machine learning?",
            "answer": "Supervised, Unsupervised, Reinforcement."
        },
        {
            "question": "What is overfitting?",
            "answer": "When a model performs well on training data but poorly on unseen data."
        },
        {
            "question": "Difference between classification and regression?",
            "answer": "Classification predicts categories, regression predicts continuous values."
        },
        {
            "question": "What is Gradient Descent?",
            "answer": "It's an optimization algorithm that reduces error by adjusting model weights."
        },
        {
            "question": "What is cross-validation?",
            "answer": "A technique to assess model performance by splitting data into multiple folds and training/testing on different combinations."
        },
        {
            "question": "What is feature engineering?",
            "answer": "The process of selecting, modifying, or creating features from raw data to improve model performance."
        },
        {
            "question": "What is the bias-variance tradeoff?",
            "answer": "Bias is error from oversimplifying assumptions. Variance is error from sensitivity to small fluctuations. Models need to balance both."
        },
        {
            "question": "What is regularization?",
            "answer": "Techniques used to prevent overfitting by adding a penalty term to the loss function (e.g., L1, L2 regularization)."
        },
        {
            "question": "What is a neural network?",
            "answer": "A computing system inspired by biological neural networks, consisting of interconnected nodes (neurons) organized in layers."
        }
    ],
    "Database": [
        {
            "question": "What is a database?",
            "answer": "A database is an organized collection of data stored and accessed electronically."
        },
        {
            "question": "What is SQL?",
            "answer": "SQL is a language used to interact with relational databases. It includes DDL, DML, DCL, TCL commands."
        },
        {
            "question": "What is a primary key?",
            "answer": "Primary key uniquely identifies each record in a table."
        },
        {
            "question": "What is a foreign key?",
            "answer": "Foreign key establishes a relationship between two tables."
        },
        {
            "question": "What are joins?",
            "answer": "Joins combine rows from two or more tables based on related columns. Types: Inner, Left, Right, Full."
        },
        {
            "question": "What is normalization?",
            "answer": "Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity."
        },
        {
            "question": "What is ACID in database?",
            "answer": "ACID stands for Atomicity, Consistency, Isolation, Durability - properties that ensure reliable database transactions."
        },
        {
            "question": "What is the difference between DELETE and TRUNCATE?",
            "answer": "DELETE removes rows one by one and can be rolled back. TRUNCATE removes all rows at once and cannot be rolled back."
        },
        {
            "question": "What is an index?",
            "answer": "An index is a database structure that improves the speed of data retrieval operations on a table."
        },
        {
            "question": "What is a view in SQL?",
            "answer": "A view is a virtual table based on the result of a SQL statement. It contains rows and columns like a real table."
        }
    ]
}

def get_predefined_questions(subject, count=5):
    """
    Get predefined questions for a subject.
    
    Args:
        subject (str): Subject name (Java, Python, Machine Learning, Database)
        count (int): Number of questions to return
    
    Returns:
        list: List of question-answer dictionaries
    """
    # Normalize subject name
    subject_lower = subject.lower()
    
    # Map variations to standard names
    subject_map = {
        "java": "Java",
        "python": "Python",
        "machine learning": "Machine Learning",
        "ml": "Machine Learning",
        "database": "Database",
        "db": "Database",
        "dbms": "Database",
        "sql": "Database"
    }
    
    standard_subject = subject_map.get(subject_lower, subject)
    
    if standard_subject in PREDEFINED_QUESTIONS:
        questions = PREDEFINED_QUESTIONS[standard_subject]
        # Return requested number of questions
        return questions[:count] if count <= len(questions) else questions
    else:
        # Return empty list if subject not found
        return []

