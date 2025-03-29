import colored
import signal

# Function to take user details
def user_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age
    
# Function to display user details
def display_user_details(name, age):
    print(f"\n{colored.fg('green')}Name: {colored.attr('reset')}{name}")
    print(f"{colored.fg('green')}Age: {colored.attr('reset')}{age}\n")
    
    
# Function to start the game
def start_game():
    number = int(input("Enter a number between 1 and 100: "))
    attempts = 0
    
    while True:
        attempts += 1
        guess = int(input("Enter your guess: "))
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations, you guessed the number in {attempts} attempts!")
            break
    
# Function to check for Ctrl + C from the user to quit the game nicely.
def exit_gracefully(signum, frame):
    print("\nGoodbye!")
    exit(0)
    
signal.signal(signal.SIGINT, exit_gracefully)

# Entry point function
def main():
    # Display welcome message to the user
    print(f"\n{colored.fg('green')}Welcome to the Number Guesser!{colored.attr('reset')}")
    name, age = user_details() 
    
    # Display user details
    display_user_details(name, age)
    
    # Start the game
    start_game()
    
    # Display goodbye message to the user
    print(f"\n{colored.fg('green')}Goodbye, {name}!{colored.attr('reset')}")
    
main()