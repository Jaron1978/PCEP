# if statements can be created inside if statements. 

answer_a = input('Do you like to Travel? Y / N: ')
if answer_a == 'Y':
    answer_b = input('And do you like Asia? Y / N: ')
    if answer_b == 'Y':
        print('You\'ve won a Holiday to Japan! ')
    else: 
        print('No free Holiday to Japan for you then! ')

else:
    print('Ah, No free Holiday for you then! ')
# If the user answers 'Y' to both questions, they win a Holiday to Japan
# Any use of 'N' voids the entry. 