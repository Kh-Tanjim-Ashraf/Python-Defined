import random


def choices():
    options = ['rock', 'paper', 'scissors']
    user_val = input("Enter value:").lower()
    comp_val = random.choice(options)
    print(f"User chose: {user_val}, Computer chose: {comp_val}")
    return [user_val, comp_val]


def check_winning(user_val, comp_val):
    if user_val == comp_val:
        return "It's a tie!"
    
    if user_val == "rock":
        if comp_val == "paper":
            return "Computer wins!"
        else:
            # Logically comp_val=scissors; thus comparing between "rock" & "scissors", rock (user) wins 
            return "User wins!"

    if user_val == "paper":
        if comp_val == "rock":
            return "User wins!"
        else:
            # Logically comp_val=scissors; thus comparing between "paper" & "scissors", scissors (comp) wins 
            return "Computer wins!"


    if user_val == "scissors":
        if comp_val == "rock":
            return "Computer wins!"
        else:
            # Logically comp_val=paper; thus comparing between "scissors" & "paper", scissors (user) wins 
            return "User wins!"


user_val, comp_val = choices()

print(check_winning(user_val, comp_val))