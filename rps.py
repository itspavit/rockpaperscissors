import random

#rock > scissors, scissors > paper, paper > rock

def start():
    user_choice = input("choose your item?? 'r' is rock, 'p' is paper, 's' is scissors: ")
    computer_choice = random.choice(['r','p','s'])

    if user_choice == computer_choice:
        return 'It\'s a draw'
    
    if winner(user_choice, computer_choice):
        return f"You win Human Computer\'s choice was {computer_choice}"
    
    return f"You lost Human! Computer\'s choice was {computer_choice}"

def winner(player1, player2):
    if (player1=='r' and player2=='s') or (player1 == 'p' and player2 == 'r')\
    or (player1 == 's' and player2 == 'p'):
        return True
    
print(start())