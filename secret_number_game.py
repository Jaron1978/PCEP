# Following on from 18. while_loop
secret_number = 19

print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
      
user_input = int(input('Try to guess the magic number! '))
while user_input != secret_number:
    print('I\'m Sorry, that is wrong')
    user_input = int(input('Try to guess the Secret Number. Its between 1 and 20: '))
print('Congratulations! You have learnt the Magic Number! ')