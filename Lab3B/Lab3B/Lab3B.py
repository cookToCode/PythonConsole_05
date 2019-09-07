#cookToCode
#This program emulates a cash register

#variable library
answer = 'y'
price = float(0.0)
total = float(0.00)
pay = float(0.0)
change = float(0.0)

#These loops are called "While loops"   the syntax is very specific
#This is also an introduction to "conditional or comparison statements"

#       == means equals | != means does not equal | > means greater than | < means less than 
#       you can also do <= which means less than or equal to | >= means greater than or equal to

#Start the loop
while (answer == 'y'):      #BE CAREFUL, if a while loop doesn't have an exit, it will run forever
    price = float(input('\nWhat is the price of the item? '))
    total = total+price
    answer = input('Do you want to add another item (y/n)? ')   #<--- This allows the user to exit the loop

#The space after the "while (answer == 'y'):" is very specific | it is ONE tab key | visual studio can do this for you automatically


print(f'\nYour total is ${total}')
pay = float(input('How much money are you going to give the clerk? '))

#added while statement for fun
while (pay < total):
    print('''\nBud.....
    That doesn't even cover the bill.....''')
    pay = float(input('\nWanna try that again??\n How much money are you going to give the clerk? '))


change = round(pay-total, 2)
print(f'\nYour change is ${change}')