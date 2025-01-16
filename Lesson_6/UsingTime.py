from Time import Time

# First Time object

myTime = Time()

myTime.set_time( 8, 59, 45)

for i in range(20):
    myTime.print_time()
    myTime.tick()

myTime.set_time( 0, 0, 0)


myTime.tick(5)
myTime.print_time()
print()
myTime.tick(65)
myTime.print_time()
print()
myTime.tick(125)
myTime.print_time()
print()
myTime.tick(36000)
myTime.print_time()
