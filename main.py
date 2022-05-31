import random

while True:
    game=['rock', 'paper', 'scissors']
    comp=random.choice(game)
    player=None

    while player not in game:
        player=input('rock,paper, or scissors :').lower()

    if player==comp:
        print('player: ', player)
        print('computer: ', comp)
        print('Tie!')
    elif player=='rock':
        if comp=='paper':
            print('player: ', player)
            print('computer: ', comp)
            print('You lose!')
        if comp=='scissors':
            print('player: ', player)
            print('computer: ', comp)
            print('You win!')
    elif player=='paper':
        if comp=='rock':
            print('player: ', player)
            print('computer: ', comp)
            print('You win!')
        if comp=='scissors':
            print('player: ', player)
            print('computer: ', comp)
            print('You lose!')
    elif player =='scissors':
        if comp=='rock':
            print('player: ', player)
            print('computer: ', comp)
            print('You lose!')
        if comp=='paper':
            print('player: ', player)
            print('computer: ', comp)
            print('You win!')
    again = input('Do you wanna play again? yes/no :').lower()

    if again!='yes':
        break
print('Bye!')




