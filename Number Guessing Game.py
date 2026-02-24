import random

best_score = float('inf') 

def play_game():
    global best_score
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"Guess the number between 1-100! You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter guess: "))
        attempts += 1
        
        if guess == secret:
            print(f" Correct! You got it in {attempts} attempts!")
            if attempts < best_score:
                best_score = attempts
                print(f" New best score: {best_score} attempts!")
            else:
                print(f"Current best score: {best_score} attempts")
            return True
            
        elif guess < secret:
            remaining = max_attempts - attempts
            print(f" Too low! ({remaining} attempts remaining)")
        else:
            remaining = max_attempts - attempts
            print(f" Too high! ({remaining} attempts remaining)")
    
    
    print(f" Game over! The number was {secret}")
    print(f"You used all {max_attempts} attempts")
    return False


while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print(f"Final best score: {best_score} attempts")
        break
