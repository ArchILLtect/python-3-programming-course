num_of_nums = int(input(
         "How many numbers do you want to average? "))

sum = 0.0
for count in range (num_of_nums):
         value = int(input("Enter a value: "))
         sum = sum + value

average = sum / num_of_nums
print ("The average is:", average)
