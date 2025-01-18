my_dictionary = { }

days_in_month = {'Jan':31, 'Feb':28, 'Mar':31} 
days_in_month2 = {'Apr':30, 'May':31, 'Jun':30}
days_in_month.update(days_in_month2)
print (days_in_month.items())

del days_in_month ['Apr']
print (days_in_month.items())

# Gives error because evens does not exist (after delete):
odds = {1:'one', 3:'three', 5:'five'}
evens = {2:'two', 4:'four', 6:'six'}
odds.clear()

print ("After clearing odds:")
print (odds)

del evens
print ("After clearing evens:")
print (evens)
