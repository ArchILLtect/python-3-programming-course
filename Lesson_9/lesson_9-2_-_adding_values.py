my_dict = {}

days_in_month = {'Jan':31,
                 'Feb':28,
                 'Mar':31}

print(days_in_month ['Jan'])
print(days_in_month)
print(my_dict)

print (days_in_month.keys())
print (days_in_month.values())
print (days_in_month.items())

# Will return 'True':
print ('Feb' in days_in_month)

# Adding values:
days_in_month ['Apr'] = 20
print(days_in_month ['Apr'])
days_in_month ['Apr'] = 30
print(days_in_month ['Apr'])
