# Import packages
import signal
import colored
import random
import time

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
        computer_choice = computer_think()
        player_choice = player_input()
        
        if player_choice not in ['r', 'p', 's']:       
            print(f"{colored.fg('red')}Invalid choice. Please enter 'r', 'p', or 's'.{colored.attr('reset')}")
            continue
        
        choice_display(player_choice, computer_choice)
        
        if player_choice == computer_choice:
            print(f"{colored.fg('yellow')}It's a tie!{colored.attr('reset')}")
        elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p'):
            print(f"{colored.fg('green')}You win!{colored.attr('reset')}")
        else:
            print(f"{colored.fg('red')}You lose!{colored.attr('reset')}")
        
        play_again = input("Do you want to play again? (yes/no): ").casefold().strip()
        
        if play_again != 'yes':
            break 
        
# Function to return possible ascii arts left side computer in red color and green color on right which is player choice
def choice_display(player_choice, computer_choice):
    player_art = ""
    computer_art = ""
    
    if player_choice == 'r':
        player_art = f"""
{colored.fg('green')}
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
You chose rock.{colored.attr('reset')}
"""
    elif player_choice == 'p':
        player_art = f"""
{colored.fg('green')}
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
You chose paper.{colored.attr('reset')}
"""
    else:
        player_art = f"""
{colored.fg('green')}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You chose scissor.{colored.attr('reset')}
"""
        
    if computer_choice == 'r':
        computer_art = f"""
{colored.fg('red')}
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
I chose rock.{colored.attr('reset')}
"""
    elif computer_choice == 'p':
        computer_art = f"""
{colored.fg('red')}
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
I chose paper.{colored.attr('reset')}
"""
    else:
        computer_art = f"""
{colored.fg('red')}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
I chose scissor.{colored.attr('reset')}
"""
        
    print(computer_art)
    print(player_art)

# Computer think function
def computer_think():
    
    # Display the thinking process
    print(f"\n{colored.fg('green')}I'm thinking...", end="", flush=True)
    for char in "...":
        print(char, end="", flush=True)
        time.sleep(0.5)
    print(f"{colored.attr('reset')}\n")
    
    # Return a random choice
    return random.choice(['r', 'p', 's'])
    
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