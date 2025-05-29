#006

#Ask how many slices of pizza the user  started with and ask how many slices they have eaten.  Work out how many slices they have left  and display the  answer in a user friendly format. 

pizza_initial = int(input('How many slices of pizza do you start with?: '))
pizza_eaten = int(input('How many slices of pizza have they eaten?: '))

operation = pizza_initial - pizza_eaten

print(f'You started with {pizza_initial} slices of pizza and They have eaten {pizza_eaten} slices so There are {operation} slices left')