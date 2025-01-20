# Part 1:
try:
   user_num = eval( input("Please enter a number: ") )
   result = 10 / user_num
except (NameError, SyntaxError):
   print ("The value you entered was not a number")
except ZeroDivisionError:
   print ("You cannot divide by zero")
else:
   print ("The result of dividing 10 by your number is", result)

# Part 2:
try:
   infile = open('C:/Users/nickh/Documents/data.txt', 'r')
   try:
       value = infile.readline()
       number = int(value)
       print (number)
   finally:
       infile.close()
       print ("the data file was closed")
except IOError as io:
   print ("Could not open file:", io.filename)
except ValueError:
   print ("Could not convert", value, "to a number")
