"""
Input a list
what item you want to input
How many item you want to input
run for loop
after input ask what type of comprehension you want to make --> list comprehension, dictionary comprehension or set comprehension
make that comprehension and print it
"""

print("\n<--- COMPREHENSIONS --->\n")
print("yes, __ ")
num_item = int(input("How many items you want to input: "))
list_inp = []
num = 1

for i in range(num_item):
    item_inp = input(f"Enter item no {num}: \n")
    list_inp.append(item_inp)
    num = num + 1

print("What type of Comprehension you want?")
compre = int(input("Enter 1 for List comprehension, 2 for Dictionary comprehension or 3 for Set comprehension: "))

if compre == 1:
    list_compre = [item for item in list_inp]
    print(list_compre)

elif compre == 2:
    dict_compre = {item for item in list_inp}
    print(dict_compre)

elif compre == 3:
    set_compre = {item for item in [f"{list_inp}"]}
    print(set_compre)
else:
    print("Invalid Input!")

