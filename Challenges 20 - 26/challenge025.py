#025  

#Ask the user to enter their first name. If the length  of their first name is under five characters, ask  them to enter their surname and join them  together (without a space) and display the name  in upper case. If the length of the first name is five  or more characters, display their first name in lower case. 

name = input('Enter your name: ')

if len(name) < 5:
    surname = input('Enter your surname: ')
    together = name + surname
    print(together.upper())
else:
    print(name.lower())