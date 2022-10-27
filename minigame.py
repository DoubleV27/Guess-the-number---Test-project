import random

print('This program will generate a number between 0 and 100. You need to guees correctly the number, being that with each attempt you will receive a hint. Good game!')
input('Press enter to begin!')


print('A value from 0 to 100 was generated.')


correct=False
stay_in_game=True


while stay_in_game==True:
    random_number = random.randint(0,100)
    while correct==False:
        try:
            guess=int(input('Take a guess of a number from 1 to 100: '))
            if guess > random_number:
                print('Insert a lower value!')
            elif guess < random_number:
                print('Insert a higher value!')
            elif guess==random_number:
                correct==True
                print(f'CONGRATULATIONS! YOU WON')
                break
        except:
            print('Please insert just numbers!')


    while True:    
        stay=input('Would you like to play again? (y/n)')
        if stay=='y':
            break
        elif stay=='n':
            print('GAME OVER!')
            stay_in_game=False
            break
        else:
            print('Please insert just "y" or "n"')

