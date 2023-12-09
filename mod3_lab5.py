## While and Conditions ##

money = 50
shopping_cart = {}
fruits = {
    "apple": 5,
    "raspberry": 10,
    "lemon": 20
}

while True:
    if money <= 0:
        print('Thanks for shopping!')
        break
    else:
        fruits_display = ', '.join([f'{key.title()}(${value})' for key, value in fruits.items()])
        player_choice = input(f'Select a fruit: {fruits_display}: ').lower()
        if player_choice in fruits:
            if money >= fruits[player_choice]:
                shopping_cart[player_choice] = shopping_cart.get(player_choice, 0) + 1
                money -= fruits[player_choice]
                shopping_cart_display = '\n'.join([f"{quantity} {fruit}{'s' if quantity > 1 else ''}" for fruit, quantity in shopping_cart.items()])
                print(f'Shopping cart:\n{(shopping_cart_display.title())} \nMoney remaining: ${money}')
            else:
                print('You dont have enough money to make this purchase')
        else:
            print('Invalid choice!')
