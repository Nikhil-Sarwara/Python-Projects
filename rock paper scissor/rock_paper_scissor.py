# Import packages
import signal
import colored
import random

# Function to detect Ctrl + C from the user to quit the game nicely.
def exit_gracefully(signum, frame):
    print("\nGoodbye!")
    exit(0)
    
# Start game function
def start_game():
    print(f"\n{colored.fg('green')}Rock, Paper, Scissor!{colored.attr('reset')}")
    print(f"{colored.fg('green')}Enter 'r' for rock, 'p' for paper, 's' for scissor.{colored.attr('reset')}")
    
    while True:
        player_choice = input("Enter your choice: ").lower()
        computer_choice = random.choice(['r', 'p', 's'])
        
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