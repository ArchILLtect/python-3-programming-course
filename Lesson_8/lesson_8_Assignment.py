number = 0
userNumbers = []
userSum = 0
while number != -999:
    userInput = input("Please enter a number (-999 quits): ")
    number = int(userInput)
    if number == -999:
        continue
    userNumbers.append(number)
    userSum = userSum + int(number)
    

#On exit
if len(userNumbers) != 0:
    userAverage = userSum / len(userNumbers)
    print("Using the numbers: ")
    for i in range(len(userNumbers)):
        print(userNumbers[i], end = " ")
    print("\nThe average is: " + str(userAverage))
else: print("You must enter some numbers!!!")

