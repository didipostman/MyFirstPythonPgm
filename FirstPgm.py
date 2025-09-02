import random
number_to_guess = random.randint(1, 10)

# number of attempts
number_of_attempt = 0
begin = False

input_str = input("Please enter a whole number between 1 et 10:\n ")
while not begin :


     
    while (input_str.isdigit() == False) :
        input_str = input("Please enter a whole number between 1 et 10:\n ")
        
 
    while int(input_str) not in range (1,11) :
        input_str = input("Please enter a whole number between 1 et 10:\n ")
        
    number_as_int = int(input_str)

    
    if number_as_int > number_to_guess:
        print("number you give > number to guess ")
        input_str = input("Please enter a whole number between 1 et 10:\n ")
        
    elif  number_as_int < number_to_guess:
        print("number you give < number to guess ")
        input_str = input("Please enter a whole number between 1 et 10:\n ")
    if number_as_int == number_to_guess :
      begin = True
      
    number_of_attempt = number_of_attempt + 1


print(f"\n You guess it you won after { number_of_attempt} attempts")
