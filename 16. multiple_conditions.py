# 3 Boolean Operators in Python
# And
# Or
# Not

# Using And
# user_age = int(input('How old are you? '))
# user_country = input('Where are you based? ')

# if user_age < 25 and user_country == 'England': # Adding and means there are two requirements. 
#    print('You are under 25 and based in', user_country, 'You meet the requirements. ')
#else:
#    print('You are ', user_age, 'and are based in', user_country, 'You do meet the criteria. ')

# Using Or

#user_country = input('Where do you reside? ')

#if user_country == 'Sweden' or user_country == 'England' or user_country == 'Germany': # Using or to list Sweden, England or Germany. 
#    print('Access is granted')
#else:
#    print('I am sorry, access has been denied. ')

# Use of And & Or

user_age = int(input('What is your age? '))
user_location = input('Where are you based? ')

if not user_location == 'England' and user_age < 25 or user_location == 'England' and user_age <23: # The use of not, and & or
    print('You qualify!')
else:
    print('Sorry, you do not qualify')

# Order process is:
# not
# and
# or