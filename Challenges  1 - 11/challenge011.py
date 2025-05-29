#011  

#Task the user to enter a number over 100 and then enter a number under  10 and tell them how many times the smaller number goes into the larger  number in a user-friendly format.

number1 = int(input('Enter a number over 100: '))
number2 = int(input('Enter a number under 10: '))

operation = number1 / number2

print(f'The number {number2} goes {operation} times into the larger number {number1}')