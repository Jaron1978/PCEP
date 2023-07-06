# Conditioanl statement or if statement

user_age = int(input('Please enter your age: '))
if user_age > 30:
    print('You are over 30 Years old. ') # Notice the for indent spaces. 
    print('Sorry, you do not qualify. ')
elif user_age == 30: # Notice the double == sign. 
    print('You are exactly 30 Years old. ')
    print('You just qualify. ')
else:
    print('You are under 30 Years old. ')
    print('Congratulations, you qualify. ')

# In the code above we are using the if statement as well as an else statement. If the user is over 30, they will be informed of this, if they are under 30, the else statement
# kicks in and advises the user they are under 30. The elif statement kicks in if the user specifies their age as 30.
# If is required, elif and else are optional. 


