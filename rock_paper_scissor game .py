import random
while True:
    # Human Turn
    print ('Welcome to the game')
    choice = int(input('Please enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissor'))
    if choice > 3 or choice < 1:
        print('Please enter the valid choice')
    elif choice == 1:
        print('You choose: Rock')
    elif choice == 2:
        print('You choose: Paper')
    elif choice == 3:
        print('You choose Scissor') 

    # Computer Turn
    print('Now its computer turn')
    computer_ch = random.randint(1,3)
    if choice > 3 or choice < 1:
        print('Please enter the valid choice')
    elif computer_ch == 1:
        print('Computer choose: Rock')
    elif computer_ch == 2:
        print ('Computer choose: Paper')
    elif computer_ch == 3:
        print ('Computer choose: Scissor')

    #Final result
    if (choice == 1 and computer_ch == 2):
        print('Computer win')
    elif (choice == 2 and computer_ch == 1):
        print('You Win')
    elif (choice == 1 and computer_ch == 3):
        print('You win')
    elif (choice == 3 and computer_ch == 1):
        print('Computer win')
    elif (choice == 2 and computer_ch == 3):
        print('Computer win')
    elif (choice == 3 and computer_ch == 2):
        print('You win')
    else:
        print('Game draw')

 

  



    
    
    
    
