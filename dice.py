import random
def dice_simulate():
    number = random.randint(1,6)
    print(number)
    while(1):
        flag = str(input('Do you want to dice it up again? (enter y and if not enter n) '))
        if flag == 'y':
            number = random.randint(1,6)
            print(number)
        else:
            print('Ending the game')
            return

dice_simulate()
