# Daily Challenge: Caesar Cypher:

cypher_text = ''
answer = ''
normal_message = ''
user_inpt = input('Please enter your message here: ').lower()

answer = input(
    "Would you like to encrypt your message?, y for yes, n for no: ").lower()
if answer == 'y':
    for letter in user_inpt:
        cypher_text += chr(ord(letter) + 3)
print(cypher_text)

answer = input(
    "Would you like to decrypt your message?, y for yes, n for no: ").lower()
if answer == 'y':
    for letter in cypher_text:
        normal_message += chr(ord(letter) - 3)
print(normal_message)
