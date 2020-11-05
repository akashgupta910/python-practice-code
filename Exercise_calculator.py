# CALCULATOR

def calculator_sqr(sqr_num):
    print(f"Square of {sqr_num} is {sqr_num * sqr_num}")

def calculator_cube(cube_num):
    print(f"Cube of {cube_num} is {cube_num * cube_num * cube_num}")

def calculator(num1, num2):
    operator = input("Enter '+' for Addition, '-' for Subtraction, '*' for Multiplication or '/' for division: ")

    if operator == '+':
        print(f"sum of these two no. is {num1 + num2}")

    elif operator == '-':
        print(f"Subtraction of these two no. is {num1 - num2}")

    elif operator == '*':
        print(f"Multiplication of these two no. is {num1 * num2}")

    elif operator == '/':
        print(f"Division of these two no. is {num1 / num2}")

    else:
        print("Invalid input!")


if __name__=="__main__":
    print("\n<--- This is a Advance Calculator ---> \n --> What do you want to do, ")
    inp = int(input("Enter '1' for calculation, '2' for square root and '3' cube root: "))

    if inp == 1:
        num1 = int(input("Enter your first no: "))
        num2 = int(input("Enter your second no: "))
        calculator(num1,num2)

    elif inp == 2:
        num = int(input("Enter your no: "))
        calculator_sqr(num)

    elif inp == 3:
        num = int(input("Enter your no: "))
        calculator_cube(num)

    else:
        print("Invalid input!")

