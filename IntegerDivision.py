from random import randrange

def problem():
    b = 0
    while (b == 0):
        b = randrange(5)
        
    answer = randrange(5)
    t = b * answer
    
    guess = input(str(t) + "/" + str(b) + "=")
    if guess.strip().lower() == "q":
        return False
    
    try:
        guess = int(guess)
        if guess == answer:
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError as e:
            print("Please enter Integers Only! ", e)
    
    return True

print("Integer Divisions: (type 'q' to quit)")
while(problem()):
    pass
