from Time2 import Time

myTime1 = Time()
print("Using the object name:")
print (myTime1.__doc__)

print()
print("Using just the class name:")
print (Time.__doc__)

print()
print("Getting the class name from the object:")
print (myTime1.__class__)
