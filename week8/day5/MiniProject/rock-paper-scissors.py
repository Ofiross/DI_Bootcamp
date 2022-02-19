from game import Game


def get_user_menu_choice():
    options = ['1', '2', '3']
    while True:
        game_menu = input("""
            ************************
            *      -----------     *
            *     | Main Menu |    *
            *      -----------     *
            *  1 Play a new game   *
            *  2   Show scores     *
            *  3      Quit         *
            ************************
              Enter your choice: """)

        if game_menu not in options:
            continue
        break
    return game_menu


def print_results(results):
    print("""
    ***********
    *  SCORE  *
    ***********
    """)
    for k, v in results.items():
        print(k, v, sep=' - ')


def main():
    print("""
    *******************************************
    * WELCOME TO THE ROCK PAPER SCISSORS GAME *
    *******************************************
    """)
    menu = get_user_menu_choice()
    game_on = Game()
    while menu != '3':
        if menu == '1':
            game_on.play()
        elif menu == '2':
            print_results(game_on.game_score())

        menu = get_user_menu_choice()
    print("See you next time.")


main()
