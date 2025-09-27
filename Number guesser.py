import random
import Logo

print(Logo.art)
number = random.randint(1, 100)

def no_of_attempts():
    difficulty = input("Choose a difficulty level. Enter 'e' for easy or 'h' for hard: ").lower()
    
    if difficulty == "e":
        attempts = 10
        print(attempts)
    elif difficulty == "h":
        attempts = 5
        print(attempts)
    return attempts


lives = no_of_attempts()
game_over = False

def make_a_guess():
    global lives
    global number
    global game_over
    user_guess = int(input(f"Make a guess. You have {lives} attempts left:\n"))

    if user_guess == number:
        game_over = True
        print("You have guessed correctly. You win!")
    if user_guess < number:
        lives -= 1
        print("Too low. Try again.")
    if user_guess > number:
        lives -= 1
        print("Too high. Try again.")
    if lives == 0:
        game_over = True
        print("You have exhausted your attempts. You lose!")

while not game_over:
    make_a_guess()
     