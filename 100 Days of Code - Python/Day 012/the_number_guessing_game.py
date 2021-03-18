import random
def game_level(guesses):
    number = random.randint(1,100)
    while guesses > 0:
        try:
            guess = int(input("Whats Your guess: "))
            guesses = guesses - 1
            if guess == number:
                print("You win!")
                break
            elif guess > number:
                print("Too hight")
            else:
                print("Too low")
            print(f"You still have {guesses}")
        except:
            print("Invalid argument")
    if guesses == 0:
        print("You lose this chalange")
    play_again = input("Do you want to play again? 'y' or 'n': ")
    if play_again == 'y':
        game()
        
def game():
    print("wellcome to The Number Guessing Game!")
    level = input("Chose between 'hard' or 'easy': ").lower()
    if level == 'hard':
        level_value = 5
        print(f"You are in hard mode you have 5 guesses")
    else:
        level_value = 10
        print(f"You are in easy mode you have 10 guesses")
    game_level(level_value)


game()