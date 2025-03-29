# Import packages
import signal

print("Welcome to the Quiz Game!")

# Data for the quiz game
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
]

def user_input():
    """
    Asks the user for their name and returns it.
    
    Returns:
        str: The user's name.
    """
    name = input("What is your name? ")
    return name

# Check if user wants to play or not
def user_wants_to_play():
    """
    Asks the user if they want to play the game.
    
    Returns:
        bool: True if the user wants to play, False otherwise.
    """
    return input("Do you want to play? (yes/no) ").lower() == "yes"

def play_game():
    """
    Plays the quiz game.
    """
    name = user_input()
    print(f"Hello, {name}!")
    score = 0

    for question in questions:
        print(question["question"])
        user_answer = input("Your answer: ")
        if user_answer.casefold().strip() == question["answer"].casefold():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"Your score: {score}/{len(questions)}")

# Function to detect Ctrl + C from the user to quit the game nicely.
def exit_gracefully(signum, frame):
    print("\nGoodbye!")
    exit(0)

signal.signal(signal.SIGINT, exit_gracefully)

while user_wants_to_play():
    play_game()