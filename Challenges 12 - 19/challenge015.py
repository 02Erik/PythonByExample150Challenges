#015  

#Ask the user to enter their favourite colour. If they enter “red”, “RED” or  “Red” display the message “I like red too”, otherwise display the message  “I don’t like [colour], I prefer red”. 

colour = str(input('Enter your favorite colour: ')).upper()

if colour == 'RED':
    print('I like red too')
else:
    print(f'I dont like {(colour).lower()}, I prefer red.')
