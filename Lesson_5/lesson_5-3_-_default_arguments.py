# Part 1:
def square(num = 1):
    """This function calculates the square of a number"""
    result = num * num
    return result

print("-" * 80)

# Part 2:
def prompt_user(prompt, num_tries = 2):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)

print("-" * 80)

# Part 3:
print(square(8))
prompt_user("Enter yes or no: ")
prompt_user("Enter yes or no: ", 3)
print("-" * 80)
