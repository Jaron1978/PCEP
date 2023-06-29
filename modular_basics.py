income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

# We have created three variables, income, lowtaxland_rate and ripoffland_rate. 
# We then carry out some basic calculations to establish how much tax is paid in both locations, then finally, we calculate the saving we make. 

print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 
      'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')