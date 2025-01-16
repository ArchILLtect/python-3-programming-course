def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1

number = 5
print ("Outside, number is:", number)
change_number()
print ("Outside, number is now:", number)
