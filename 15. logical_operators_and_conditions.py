# Logical operators: 
# < Less than,
# > Greater than
# <= Less than or Equal too, 
# >= Greater than or Equal too, 
# == Equals
# != Does not equal

password = input('Do you know the secret password? ')
if password != '--secret!':                                 # if Password is not --secret!
    print('Access Denied! This is the wrong Password. ')
else:                                                       # if Password is --secret!
    print('That is the correct Password. Welcome!! ')

