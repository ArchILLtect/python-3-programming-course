my_dictionary = { }

days_in_month = {'Jan':31, 'Feb':28, 'Mar':31} 
days_in_month2 = {'Apr':30, 'May':31, 'Jun':30}
days_in_month.update(days_in_month2)
print (days_in_month.items())
