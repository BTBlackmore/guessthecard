"""Generates a playing card"""
import random

def generate_card():
    suits = ['spades','clubs','hearts','diamonds']
    rand_number = random.randint(1,13)
    # Generates the value of the card
    rand_suit = random.choice(suits)
    # Generates the suit

    # Converts numbers to face cards
    if rand_number == 1:
        rand_number = "Ace"
    elif rand_number == 11:
        rand_number = "Jack"
    elif rand_number == 12:
        rand_number = "Queen"
    elif rand_number == 13:
        rand_number = "King"
    return rand_number, rand_suit

card, suit = generate_card()
full_card = (f"{card} of {suit}")

#Starting messages
print("Let's play a game! I am going to pick a card from this pile. Ah, what a good card. Can you guess what it is?")
print("Your guesses should be formatted like so: 'Ace of spades', 'Queen of diamonds', '3 of clubs' etc.")
print("Also, if you type 'I give up!', the game will end and the card will be revealed.")
print("If you type 'hint', I'll give you a hint - but you only get one! Let's get going!")

#player guesses the card, and the game checks it against random card

def main():
    guess = input("Guess the card: ")
    still_playing = 1
    hints = 1

    while still_playing == 1:
        if guess == "I give up!":
            print(f"No worries. My card was {full_card}. Better luck next time!")
            break
        elif guess == "hint":
            if hints == 1:
                hint = random.randint(1,2)
                if hint == 1:
                    print("The suit is " + suit)
                    hints = 0
                    guess = input("Try again: " )
                else:
                    print("The value is " + str(card))
                    hints = 0
                    guess = input("Try again: " )
            else:
                print("You have no more hints!")
                guess = input("Try again: ")
        elif guess != full_card:
            print("That's not my card.")
            guess = input("Try again: " )
        elif guess == full_card: 
            print("Congratulations! That's my card.")
            still_playing -= 1
            break

main()
play_again = input("Would you like to play again? (Y/N)")

if play_again.lower() == "y":
    card, suit = generate_card()
    full_card = (f"{card} of {suit}")
    main()
else:
    print("Thanks for playing! See you next time.")