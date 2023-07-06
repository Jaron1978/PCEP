purchase_days_ago = int(input('How many days ago did you purchase the item? '))
is_used = input('Has the item been used? [Y / N] ')
is_broken = input('Has the item broken on its own? [Y / N] ')

if (is_broken == 'Y' or (purchase_days_ago <= 30 and is_used == 'N')):
    print('You can get a refund!')
else:
    print('This is out of warranty. ')


# If the item has been purchsed within 30 Days, has not been used and broke on its own, a refund is possible. 
# Other wise, no refund. 