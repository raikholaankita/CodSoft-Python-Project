import random

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"

def main():
    user_score = 0
    comp_score = 0
    
    print("=== ROCK PAPER SCISSORS GAME ===")
    print("Rules:Rock beats Scissors,Scissors beats Paper,Ppaper beats Rock\n")
    while True:
        print("Choose: 1.Rock 2.Paper 3.Scissors 0.Exit")
        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue
            
        if user_choice == 0:
            break
        if user_choice < 1 or user_choice > 3:
            print("Invalid choice! Try again.")
            continue
        
        comp_choice = random.randint(1, 3)
        
        print(f"\nYou chose: {get_choice_name(user_choice)}")
        print(f"Computer chose: {get_choice_name(comp_choice)}")
        
        if user_choice == comp_choice:
            print("Result: It's a TIE!")
        elif (user_choice == 1 and comp_choice == 3) or \
             (user_choice == 2 and comp_choice == 1) or \
             (user_choice == 3 and comp_choice == 2):
            print("Result: YOU WIN!")
            user_score += 1
        else:
            print("Result: COMPUTER WINS!")
            comp_score += 1
        
        print(f"Score - You: {user_score} | Computer: {comp_score}")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print(f"\nFinal Score - You: {user_score} | Computer: {comp_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
