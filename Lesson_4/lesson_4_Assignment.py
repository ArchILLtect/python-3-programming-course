# Lesson 04 Assignment

count = 0
sum = 0.0
average = 0.0
value = int(input("Please enter a number (use -1 to exit): "))

while (value != -1):
    sum = sum + value
    count = count + 1

    value = int(input("Please enter a number (-1 quits): "))

if (count != 0):
    average = sum / count

print ("The sum of your entered numbers is", sum)
print ("The average of your entered numbers is", average)
