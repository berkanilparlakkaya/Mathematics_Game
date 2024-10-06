import random

OPERATORS = ("+", "-", "/", "*")
MIN_OPERAND = 2
MAX_OPERAND = 9
TotalProblems = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + (operator) + " " + str(right)
    answer = eval(expr)

    return expr, answer

for i in range(TotalProblems):
    expr, answer = generate_problem()
    while True:
    
        guess = input("Problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            print("Right!")
            break
        else:
            print("Wrong! Try again.")
            
        
