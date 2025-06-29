import random

while True:  # Outer loop for game sessions
    secret_number = random.randint(1, 10)
    guess_count = 0
    
    while True:  # Inner loop for guessing
        try:
            guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?\n"))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        guess_count += 1
        
        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it in {guess_count} tries!")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _:
                print("Nope, your guess is a bit low. Give it another shot!")
    
    play_again = input("Play again? (yes/no) ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break