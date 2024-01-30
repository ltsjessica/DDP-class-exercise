import random 

player1 = input ("please enter your name:")
player2 = input ("please enter your name:")

while True: 
    price= random.randrange(0,100)

    player1_guess = int(input("please input your guess"))
    player2_guess = int(input("please input your guess"))
    
    
    if player1 == price:
        print(f"{player1} is correct!{player1} win!")
        break
    elif player2 == price:
        print(f"{player2} is correct!{player2} win!")
        break
    elif abs(price-player1) < abs(price-player2):
        print(f"{player1} answer is closer to the price")
    else:
        print(f"{player2} answer is closer to the price") 


