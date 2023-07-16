# numbers = ['1, 2, 3, 4'] # Numbers listed from 1 to 4. But what if we wanted 1 to 100? 

#numbers = []
#for i in range(1, 101):
#    numbers.append(i)
# print(numbers)
# However, we can use list comprehensions:

# numbers = [i for i in range(1, 101)]
# print(numbers)
# See how easier it is to write 1 to 100 using list comprehension. 

numbers = [i for i in range(1, 101) if i % 3 !=0]
print(numbers)
# Removes any numver that can be divised by 3. 