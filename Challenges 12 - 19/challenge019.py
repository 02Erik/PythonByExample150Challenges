#019  

#Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display  “Well done”, if they enter a 3, display “Correct”. I they enter anything else, display “Error message”.

number = int(input('Enter a number among 1, 2, 3: '))

if number == 1:
    print('Thank you.')
elif number == 2:
    print('Well done.')
elif number == 3:
    print('Correct.')
else:
    print('Error message.')