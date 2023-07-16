# invited_guests = ['Kate', 'Ron', 'Jane', 'Adam', 'Kerry', 'Joe']
# name = input('Please enter your Name! ')
# if name in invited_guests: # <-- in operator
#     print('Welcome!')
# else:
#     print('Access Denied')

invited_guests = ['Kate', 'Ron', 'Jane', 'Adam', 'Kerry', 'Joe']
name = input('Please enter your Name! ')
if name not in invited_guests: # <-- Still using the in operator. 
    print('You are not invited! ')
else:
    print('Welcome', name)