import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    print("Welcome to Rock-Paper-Scissors!")
    
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return None, None
    
    # Computer choice
    computer_choice = get_computer_choice()
    
    # Determine winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices and result
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'win':
        print("You win!")
    else:
        print("You lose!")
    
    return result, computer_choice

def main():
    """Main function to run the Rock-Paper-Scissors game with score tracking."""
    user_score = 0
    computer_score = 0
    
    while True:
        result, computer_choice = play_game()
        
        if result:
            if result == 'win':
                user_score += 1
            elif result == 'lose':
                computer_score += 1
            
            # Display scores
            print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
