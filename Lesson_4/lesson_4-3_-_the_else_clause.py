# Part 1:
for number in range(1, 11):
         if number == 4:
                   continue
         print (number)
else:
         print ("Exited normally")
print("-" * 80)

# Part 2:
phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
         if phrase [index] == letter:
                   print ("The letter first appears at index: ", index)
                   break
else:
         print ("Your letter wasn't found")
print("-" * 80)
