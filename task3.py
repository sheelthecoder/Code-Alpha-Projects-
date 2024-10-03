import nltk
from nltk.chat.util import Chat, reflections
import random

# Download the required NLTK data (if not already done)
nltk.download('punkt')
nltk.download('wordnet')

# Task 1: Suggest Python project ideas
def suggest_python_projects():
    projects = [
        "Stock price tracker using Yahoo Finance API",
        "Weather app using an API like OpenWeatherMap",
        "To-do list app with a command-line interface",
        "Simple blog using Flask or Django",
        "Hangman game ",
        "Chatbot using NLTK or spaCy "
    ]
    return random.choice(projects)

# Task 2: Answer questions about Python libraries
def answer_about_python_libraries(library):
    library_info = {
        "nltk": "NLTK is a powerful library for natural language processing with Python. It provides tools for text processing, classification, tokenization, and more.",
        "spacy": "spaCy is an open-source NLP library for Python. It offers fast processing and advanced features like part-of-speech tagging, named entity recognition, and word vectors.",
        "pandas": "Pandas is a data manipulation and analysis library. It's widely used for data cleaning, processing, and analysis in Python.",
        "numpy": "NumPy is a core package for scientific computing in Python, offering support for large, multi-dimensional arrays and matrices, along with many mathematical functions."
    }
    return library_info.get(library.lower(), f"Sorry, I don't have information about {library}. Can you ask about something else?")

# Task 3: Provide programming advice
def programming_advice():
    tips = [
        "Break your code into smaller functions to keep things modular and clean.",
        "Write code every day! Practice is key to improving your skills.",
        "Use online resources like StackOverflow or official documentation when you're stuck.",
        "Test your code regularly to catch bugs early.",
        "Start with small projects and gradually build larger ones as you learn."
    ]
    return random.choice(tips)

# Define chatbot pairs (patterns and responses)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No worries.", "It's okay."]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["That's great to hear!", "Good to know!"]
    ],
    [
        r"what can you do?|what tasks can you do?|what are your tasks?",
        ["I can assist you with the following tasks:\n"
         "- Suggest Python project ideas\n"
         "- Answer questions about Python libraries\n"
         "- Provide programming tips and advice\n"
         "- Help you with basic Python programming issues"]
    ],
    [
        r"can you help me with (.*)",
        ["Yes, I can help you with %1. Could you give me more details?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?"]
    ]
]

# Reflections to enhance natural conversation
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Define the function to start the conversation
def start_chat():
    print("Hi! I am a chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Manually handle dynamic responses based on patterns
        if "give me a python project idea" in user_input.lower():
            response = suggest_python_projects()
        elif "give me programming advice" in user_input.lower():
            response = programming_advice()
        elif "tell me about" in user_input.lower():
            library = user_input.split("about")[-1].strip()
            response = answer_about_python_libraries(library)
        else:
            response = chatbot.respond(user_input)
        
        print("Bot:", response)

# Start the chatbot
start_chat()
