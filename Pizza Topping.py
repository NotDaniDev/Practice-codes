toppings = {'pepperoni' : 50, 'paneer' : 20, 'onions': 10, 'sausage' : 40}
print('Base price of the pizza is 100, you can add toppings with the limit of 3')
print('The prices are \n pepperoni : 50 \n paneer : 20 \n onions : 10 \n sausage : 40')
total = 100
# Base price of pizza is 100
while True:
    n = int(input('Enter how many toppings do you want on your pizza: '))
    if n > 3:
        print('There is a limit of 3 toppings you cannot add more')
        continue
    elif n == 0:
        break
    else:
        pass
    for i in range(n):
        top = str(input('Enter which topping do you want: '))
        if top in toppings:
            total += toppings[top]
    money = float(input('Enter the amount of money you have: '))
    break

while True:
    if money < total:
        print('You do not have enough money to buy the pizza you wish for')
        break
    elif money == total:
        pass
    print(f'You had to pay {total}')
    change = money - total
    print(f'Change you have left is {change}')
    break
