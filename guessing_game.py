
def start_game():
    print("Welcome to the number guessing game!")
    import random
    num = random.randrange(1, 10)
    attemps = 0
    while True:
        attemps += 1
        try:
            picked_num = int(input("Pick a number between 1 and 10: "))
            if picked_num > num:
                print("Its lower.")
                continue
            elif picked_num < num:
                print("It's higher.")
                continue
            elif picked_num == num:
                print("You got it!! it took you {} tries.".format(attemps))
                print("The game is over!")
                break
        except NameError as err:
            print("Ooops it was not a valid value.  PLEASE TRY AGAIN")
# Kick off the program by calling the start_game function.

start_game()