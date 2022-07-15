
def start_game():
    print("Welcome to the number guessing game!")
    import random
    num = random.randrange(1, 10)
    attemps = 0
    while True:
        attemps += 1
        try:
            picked_num = int(input("Pick a number between 1 and 10: "))
            if picked_num >10 or picked_num <1:
                raise ValueError("Please, choose a number from 1 to 10")
            if picked_num > num:
                print("Its lower.")
                continue
            elif picked_num < num:
                print("It's higher.")
                continue
            elif picked_num == num:
                print("You got it!! it took you {} tries.".format(attemps))
                print("The game is over!")
                high_score = attemps
                play_again = input("Would you like to play again?    y/n ")
                if play_again.lower() == "y":
                    print("The HIGHSCORE is {}".format(high_score))
                    num = random.randrange(1,10)
                    attemps = 0
                    continue
                else:
                    print("See you next time")
                    break
        except NameError:
            print("Ooops it was not a valid value. PLEASE TRY AGAIN")

# Kick off the program by calling the start_game function.

start_game()