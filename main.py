# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
session_name = input("Enter the session number: ")
number_players = int(input("Enter the number of players: "))

unknown_number = random.randint(1, 100)
while number_players > 0:
    player_name = input("Enter the player name: ")
    player_number = int(input("Enter the number: "))
    diff = abs(unknown_number - player_number)
    if player_number == unknown_number:
        print("You win!")
        award = 10
    elif diff <= 3:
        print("Very close!")
        award = 7
    elif diff <= 5:
        print("Close!")
        award = 5
    elif diff <= 10:
        print("Not bad!")
        award = 2
    else:
        print("You lose!")
        award = 0

    with open(f'score {session_name}.txt', 'a') as f:
        f.writelines(f"{player_name} your guess {player_number} and your points are {award}")

    number_players -= 1
print("The number was: ", unknown_number)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
