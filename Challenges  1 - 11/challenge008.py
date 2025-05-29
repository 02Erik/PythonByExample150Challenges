#008  

#Ask for the total price of the bill, then ask how  many diners there are. Divide the total bill by the  number of diners and show how much each  person must pay. 

bill_price = float(input('Enter the price of the bill: '))
dinners = int(input('How many dinners are there?: '))

pay = bill_price / dinners

print(f'Each person has to pay {pay}')