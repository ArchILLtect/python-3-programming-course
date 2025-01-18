my_list = [ ]

my_list.append(10)
my_list.append('ten')

my_list.extend( [20, 'twenty'] )


print(my_list)

my_list = my_list + [30, 'thirty']

print(my_list)

my_list.insert(3, 'hi there!')

print(my_list)

my_list.remove('hi there!')

print(my_list)
