# This is a sample Python script.
import random
import emoji
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


unknown_number = random.randint(1, 100)
class Number_game():
    def __init__(self,  session_name,number_players):
        self.session_name = session_name
        self.number_players = number_players
    def random_guess(self):
        while self.number_players > 0:
            player_name = input("Enter the player name: ")
            player_number = int(input("Enter the number: "))
            diff = abs(unknown_number - player_number)
            if player_number == unknown_number:
                print(emoji.emojize("You win! :exploding_head:"))
                award = 10
            elif diff <= 3:
                print(emoji.emojize("Very close! :fire:"))
                award = 7
            elif diff <= 5:
                print(emoji.emojize("Close! :partying_face:"))
                award = 5
            elif diff <= 10:
                print(emoji.emojize("Not bad! :thumbs_up:"))
                award = 2
            else:
                print(emoji.emojize("You lose! :crying_face:"))
                award = 0

            with open(f'score {self.session_name}.txt', 'a') as f:
                f.writelines(f"{player_name} your guess {player_number} and your points are {award}\n")

            self.number_players -= 1

class main():

    try:
        session_name = input("Enter the session name: ")
        number_players = int(input("Enter the number of players: "))
        if number_players <= 0:
            print("The number of players must be greater than 0")
        game = Number_game(session_name, number_players)
        game.random_guess()
        print("The number was: ", unknown_number)
    except ValueError:
        print("The number of players must be an integer")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
