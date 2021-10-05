import random
import time
import sys
from typing import Optional

clue = random.randrange(1, 101)
high = ["high", "h", "1"]
low = ["low", "l", "2"]
jackpot = ["jackpot", "j", "3"]
num = random.randrange(1, 101)

print("Welcome to the High or Low game made by Birb#2018\n")
time.sleep(1)
name = input("Enter your name here: \n")
time.sleep(1)

def rules():
    rule = input(f"\nHello {name}! Do you know the rules to this game?(Y or N) \n")
    time.sleep(1)
    if rule.lower() == "y":
        print(f"\nOkay! Goodluck {name}!\n")
        time.sleep(2)

    elif rule.lower() == "n":
        print(f"""
        Ok here are the rules.
        I will give you a random number.
        You have to guess if the unknown number is higher or lower than the number I gave you.
        Oh and if you think the the random number is exactly the clue number you guess jackpot.
        Guess right win, guess wrong lose. Duh
        Those are all the rules to this game. I hope you have fun. Goodluck {name}!
        """)
        time.sleep(10)

    else:
        time.sleep(.5)
        print("\nInvalid Input")
        time.sleep(.5)
        print("Try again.")
        rules()

def play_loop():
    play_game = ""
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("\nDo You want to play again? Y or N \n")
        time.sleep(1)

    if play_game.lower() == "y":
      main()
    else:
      print("\nThanks For Playing! Come back another time!")
      sys.exit()

def game(one: int, two: int, three: str) -> Optional[bool]:
    if one == two:
        if three == "jackpot":
            return None
        else:
            return False

    if one > two:
      return three == "low"

    if one < two:
      return three == "high"

    raise ValueError(f"Invalid item {three}.")

def main():
    print("Let's play!")
    time.sleep(.5)

    print(f"\nThis is your clue: {clue}.")
    pick = input("1. High\n2. Low\n3. Jackpot\n\n")
    time.sleep(1)

    if pick.lower() in high:
        choice = "high"
    elif pick.lower() in low:
        choice = "low"
    elif pick.lower() in jackpot:
        choice = "jackpot"
    else:
        print(f"\nInvalid choice {pick}.")
        time.sleep(1)
        play_loop()

    result = game(clue, num, choice)

    if result is True:
        print("\nYou won! Noice!")
        print(f"The number was {num}.")
        play_loop()
    elif result is None:
        print("\nJackpot!")
        print(f"The number was {num}.")
        play_loop()
    elif result is False:
        print("\nSorry, you lost")
        print(f"The number was {num}.")
        play_loop()
    else:
        print("\nAn error has occured")
        print("Please forgive me and try again")
        main()

rules()
main()
