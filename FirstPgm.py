import random
number_to_guess = random.randint(1, 10)

# Prompt the user to enter an integer between 1 et 10
user_input_str = input("Please enter a whole number between 1 et 10:\n ")
# Convert the input string to an integer
number_as_int = int(user_input_str)
# number of attempts
number_of_attempt = 1
  
while number_as_int != number_to_guess :
        
    if number_as_int > number_to_guess:
        print("number you give > number to guess ")
        
    elif  number_as_int < number_to_guess:
        print("number you give < number to guess ")
        

    user_input_str = input("Please enter a whole number between 1 et 10:\n ")
    number_as_int = int(user_input_str)
    number_of_attempt = number_of_attempt + 1


print(f"\n You guess it you won after { number_of_attempt} attempts")