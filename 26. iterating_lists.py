# Sequences in Python are special data structures that can store more than one value and can be browsed 
# element by element. The same can be done with lists. 

# top_cities = ['New York', 'London', 'Paris', 'Madird', 'Berlin']
# for city in top_cities:
#    print('The Current City:', city)

# We can add the index to the list by using range. 

# top_cities = ['New York', 'London', 'Paris', 'Madird', 'Berlin']
# for city_index in range(len(top_cities)):
#     print('Current Index:', city_index, '| Current City:', top_cities[city_index], )

spendings = [32.50, 20.50, 300.00, 12.00, 19.95]
sum = 0.0
for spending in spendings:
    sum += spending # 0/0 + all the numbers in spendings.
print('Money Spent:', sum )