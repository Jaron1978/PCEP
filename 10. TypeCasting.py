# The float() function can be used to covert a string to a float. 

height_cm = input('Height Converter: Please enter your height in CM: ') # The user will now input a number. 
float_height_cm = float(height_cm) # Takes the height_cm variable and converts to a float. 
print('Your height in feet is:', float_height_cm / 30.48) # The print function uses the float's variable as the variable. 

# We can also write the code above like this: 

height_cm = float(input('Height Convertor: Enter your height in CM: ')) # We have added float invocation to include the input invocation.
print('Your height in feet is: ', height_cm / 30.48)

# To use an integer, you simply use int()

year_born = int(input('What year were you born? '))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live that long. ')

# As you can see, in year_born, we use an Integer rather than a float.

# You can convert a calculation to a string using the str()
temp_c = input('Enter todays temparture in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees  Fahrenheit.'
print(temp_statement)
