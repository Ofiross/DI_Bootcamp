import random


class Game:

    def __init__(self):
        self.score = {'win': 0, 'loss': 0, 'draw': 0}

    def get_user_form(self):
        player_form = ''
        accepteble_input = ['1', '2', '3']
        while True:
            player_choice = input("""
                            ***************************************************
                            *  What form would you like to be:                *
                            *  1  for Rock                                    *
                            *  2  for Paper                                   *
                            *  3  for Scissors                                *
                            ***************************************************
                                Please choose from the 3 possibilities: """)
            if player_choice not in accepteble_input:
                continue
            break
        if player_choice == '1':
            player_form = "rock"
        elif player_choice == '2':
            player_form = "paper"
        elif player_choice == '3':
            player_form = "scissors"

        return(player_form)

    def get_computer_item(self):
        computer_random_form = ["rock", "paper", "scissors"]
        return(random.choice(computer_random_form))

    def get_game_result(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item

        if user_item == computer_item:
            print("\n")
            print(
                f'Wow, your choice of {user_item.upper()} is exactly like the {computer_item.upper()} form of the PC.')
            print("It is a draw!")
            return('draw')
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "rock"):
            print("\n")
            print(
                f'Your form {user_item.upper()} is wining over PC choice of {computer_item.upper()}.')
            print("You are the winner of this round!!!")
            return('win')
        elif (computer_item == "rock" and user_item == "scissors") or (computer_item == "paper" and user_item == "rock") or (computer_item == "scissors" and user_item == "rock"):
            print("\n")
            print(
                f'Sorry, PC form is {computer_item.upper()} and it is wining over your {user_item.upper()} form.')
            print("Try better next time, you have lost PC won!")
        return('loss')

    def play(self):
        player = self.get_user_form()
        pc = self.get_computer_item()
        game_score = self.get_game_result(player, pc)
        self.score[game_score] += 1
        return game_score

    def game_score(self):
        return self.score
