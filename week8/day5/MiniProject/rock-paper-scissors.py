from game import Game


def get_user_menu_choice():
    options = ['1', '2', '3']
    while True:
        print("\n")
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
    print("\n")
    print("""
                                                  ***********
                                                  *  SCORE  *
                                                  ***********
    """)
    for k, v in results.items():
        print("\t" + "\t" + "\t" + "\t" + "\t" +
              "\t" + "    " + f"{k}" + ' - ' + f"{v}")


def main():
    print("\n")
    print("""
                     /$$      /$$ /$$$$$$$$ /$$        /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$      
                    | $$  /$ | $$| $$_____/| $$       /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/      
                    | $$ /$$$| $$| $$      | $$      | $$  \__/| $$  \ $$| $$$$  /$$$$| $$            
                    | $$/$$ $$ $$| $$$$$   | $$      | $$      | $$  | $$| $$ $$/$$ $$| $$$$$         
                    | $$$$_  $$$$| $$__/   | $$      | $$      | $$  | $$| $$  $$$| $$| $$__/         
                    | $$$/ \  $$$| $$      | $$      | $$    $$| $$  | $$| $$\  $ | $$| $$            
                    | $$/   \  $$| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$$      
                    |__/     \__/|________/|________/ \______/  \______/ |__/     |__/|________/ 
    """)

    print("""
    MMMMMMMMMMMMWNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMWNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMWNWMNkc:oxKMWNWMMMMMMMMMMMMMMMMMMMMMWWWMMMMMXxlox0WMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMNKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;',dd.    ck;',oXNK0XMMMMMMMMMMMMMWk;';xNMMNl    .OMMMMMMMMMMMMMMMM
    MMMMMMMMMWOlco0k,..cxKNOkKWMMWWMMMMMMMMMMMMMMMX;   .:.    ,,   .oc...xWMMMMMMMMMMMX;   .kMMN:    .xMMMMMMMMMMMMMMMM
    MMMMMMMMMO.   ;:.  .'l:  .oOc',oXMMMMMMMMMMMMMX;   .:.    ,,   .oc...xWMMMMMMMMMMMWd    ;XMN:    .xMMMMMMMMMMMMMMMM
    MMMMMMMMMO;...,,'''',;.   ,;   .xMMMMMMMMMMMMMX;   .;.    ,,   .;.   :NMMMMMMMMMMMMK;   .xMN:    .xMMMMMMMMMMMMMMMM
    MMMMMMMKo;...     'clc.   ';    dMMMMMMMMMMMMMX;   .;.    ,'   .;.   :NMMMMMMMMMMMMMx.   ,KN:    .xMMMMMMMMMMMMMMMM
    MMMMMMWl         .,:c:.   ';    dMMMMMMMMMMMMMX;   'c,.   ,'   .;.   :NMMMMMMMMMMMMMX:    dX:    .xNOkKWMWNWMMMMMMM
    MMMMMMWd.   .';loc;:ll.   ;;    dMMMMMMMMMMMMMXl...','','.;'   .;.   :NMMMMMMMMMMMMMMk.   ,0l    .l;  .oO:',oXMMMMM
    MMMMMMMX;   ...':cc'..,''';:'..,OMMMMMMMMMMMXo'.       .;l,     .    :NMMMMMMMMMMMMMMNl...':;.''.';.   ,,   .xMMMMM
    MMMMMMMMx.        .;:' ..   .'''kMMMMMMMMMMMx.        .,,..          :NMMMMMMMMMMMMMKl,..      'll:.   ,,   .xMMMMM
    MMMMMMMMX:          .;'         dMMMMMMMMMMMK,   ..':c:.             :NMMMMMMMMMMMMNc         .,::;.   ,,   .xMMMMM
    MMMMMMMMMk.          .;.       .xMMMMMMMMMMMWd.      .',..           :NMMMMMMMMMMMMWo    .';:;,. .;.   ;;   .xMMMMM
    MMMMMMMMMNo..         '.     .'oXMMMMMMMMMMMMX;         ';;.         :NMMMMMMMMMMMMMK,   ....'''...,''';:...;0MMMMM
    MMMMMMMMMMWNx.              .dNMMMMMMMMMMMMMMMx.          .;.        :NMMMMMMMMMMMMMWd.        .,;. ..   .'.,kMMMMM
    MMMMMMMMMMMM0'              .kMMMMMMMMMMMMMMMMX:           ,,        cNMMMMMMMMMMMMMMX;           ;'        .xMMMMM
    MMMMMMMMMMMM0'              .kMMMMMMMMMMMMMMMMM0c,.        ..     .;oKMMMMMMMMMMMMMMMMx.          .;.       .kMMMMM
    MMMMMMMMMMMMKc..............;OMMMMMMMMMMMMMMMMMMMN:               cWMMMMMMMMMMMMMMMMMMNo..         '.     .,oXMMMMM
    MMMMMMMMMMMMWNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMNc               lWMMMMMMMMMMMMMMMMMMMWNx.              .xNMMMMMMM
    MMMMMMMMMMMMWNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMNc               lWMMMMMMMMMMMMMMMMMMMMMO.              .OMMMMMMMM
    MMMMMMMMMMMMWNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMNc               lWMMMMMMMMMMMMMMMMMMMMM0:.'..........'':0MMMMMMMM
    """)

    menu = get_user_menu_choice()
    game_on = Game()
    while menu != '3':
        if menu == '1':
            game_on.play()
        elif menu == '2':
            print_results(game_on.game_score())

        menu = get_user_menu_choice()
    print("""
     _____ ______ ______     __     ______  _    _      _   _ ________   _________      _______ _____ __  __ ______  
     / ____|  ____|  ____|    \ \   / / __ \| |  | |    | \ | |  ____\ \ / /__   __|    |__   __|_   _|  \/  |  ____| 
    | (___ | |__  | |__        \ \_/ / |  | | |  | |    |  \| | |__   \ V /   | |          | |    | | | \  / | |__    
     \___ \|  __| |  __|        \   /| |  | | |  | |    | . ` |  __|   > <    | |          | |    | | | |\/| |  __|   
     ____) | |____| |____        | | | |__| | |__| |    | |\  | |____ / . \   | |          | |   _| |_| |  | | |____  
    |_____/|______|______|       |_|  \____/ \____/     |_| \_|______/_/ \_\  |_|          |_|  |_____|_|  |_|______| 
    """)


main()
