inp_name = input("What's your Name: ")
inp_salary = input("How much do you earn: ")

if int(inp_salary) == 0:
    raise ZeroDivisionError("What the F**k! ")


if inp_name.isnumeric():
    raise Exception("Number are not allowed!")

print(f"Hello {inp_name}")

# With Try Except :

name = input("Enter your Name: ")

try:
    print(inp_name)

except Exception as error:
    if name == "akash":
        raise ValueError("Akash is not allowed!")

    print(name)

