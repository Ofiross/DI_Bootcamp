from anagram_checker import AnagramChecker


def get_user_menu_choice():
    options = ['1', '2', '3']
    while True:
        print("\n")
        checker_menu = input("""
                                            ************************
                                            *      -----------     *
                                            *     | Main Menu |    *
                                            *      -----------     *
                                            *  1 Check single word *
                                            *  2  Check two words  *
                                            *  3       Quit        *
                                            ************************
                                            Enter your choice: """)

        if checker_menu not in options:
            continue
        break
    return checker_menu


def ask_user_word():
    while True:
        usr_word = input(
            'Please choose a word to see if it an anagram: ').upper()
        if not usr_word.isalpha():
            continue
        break
    return usr_word


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

    menu = get_user_menu_choice()
    anagram_check = AnagramChecker('sowpods.txt')
    while menu != '3':
        if menu == '1':
            user_word = ask_user_word()
            anagram_check.is_valid_word(user_word)
            anagram_check.check_more_words(user_word)
        elif menu == '2':
            first_word = ask_user_word()
            second_word = ask_user_word()
            anagram_check.is_anagram(first_word, second_word)
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
