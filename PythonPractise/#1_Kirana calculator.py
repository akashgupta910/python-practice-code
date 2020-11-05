print("Calculator for Shopkeeper")
numbers = []

n = 1
while True:
    if n == 1:
        inp = input("Enter Number: ")
    else:
        inp = input("Enter Number or press 'q' to Quit: ")

    if inp == 'q':
        break
    
    numbers.append(inp)
    n += 1

numbers = [int(i) for i in numbers]
total = sum(numbers)
print(f"Total: {total}")