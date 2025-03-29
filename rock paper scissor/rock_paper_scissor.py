# Import packages
import signal
import colored
import random

# Function to detect Ctrl + C from the user to quit the game nicely.
def exit_gracefully(signum, frame):
    print("\nGoodbye!")
    exit(0)
    
# Player choice function
def player_input():
    """
    Asks the user for their choice of rock, paper, or scissor.
    
    Returns:
        str: The user's choice, either 'r', 'p', or 's'.
    """
    value = input("Enter your choice: ")
    
    # Dictionary of the possible values
    possible_values = {'r': ['rock', 'r', 'ro', 'roc', 'rocky'], 
                       'p': ['paper', 'p', 'pa', 'pap', 'pape', 'paperino'],
                       's': ['scissor', 's', 'sc', 'sci', 'scis', 'sciss', 'scissi', 'scissio']}
    
    value = value.strip().lower()
    if value in possible_values or any(value in s for s in possible_values.values()):
        return list(possible_values.keys())[list(possible_values.values()).index(next(s for s in possible_values.values() if value in s))]
    else:
        print(f"{colored.fg('red')}Invalid choice. Please enter 'r', 'p', or 's'.{colored.attr('reset')}")
        return player_input()
    
# Start game function
def start_game():
    print(f"\n{colored.fg('green')}Rock, Paper, Scissor!{colored.attr('reset')}")
    print(f"{colored.fg('green')}Enter 'r' for rock, 'p' for paper, 's' for scissor.{colored.attr('reset')}")
    
    while True:
        computer_choice = random.choice(['r', 'p', 's'])
        player_choice = player_input()
        
        if player_choice not in ['r', 'p', 's']:       
            print(f"{colored.fg('red')}Invalid choice. Please enter 'r', 'p', or 's'.{colored.attr('reset')}")
            continue
        
        if player_choice == computer_choice:
            print(f"{colored.fg('yellow')}It's a tie!{colored.attr('reset')}")
        elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p'):
            print(f"{colored.fg('green')}You win!{colored.attr('reset')}")
        else:
            print(f"{colored.fg('red')}You lose!{colored.attr('reset')}")
        
        play_again = input("Do you want to play again? (yes/no): ").casefold().strip()
        
        if play_again != 'yes':
            break 
    
# Main Functiton
def main():
    # Display welcome message to the user
    print(f"\n{colored.fg('green')}Welcome to the Rock Paper Scissor Game!{colored.attr('reset')}")
    
    signal.signal(signal.SIGINT, exit_gracefully)
    
    # Start the game
    start_game()
    
    # Display goodbye message to the user
    print("\nGoodbye!")
    
main()