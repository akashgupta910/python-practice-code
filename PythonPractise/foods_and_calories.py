print("\n<---- Foods And Calories ---->\n")

nItems = int(input("How many items do you want to Enter: "))
_list = []

n = 1
for i in range(1, nItems+1):
    inpItems = input(f"Enter Item no {n}: ")
    _list.append(inpItems)
    n += 1

# Method 1st - Inbuilt Method of Python
print(list(reversed(_list)))

# Method 2nd - Slicing Trick
print(_list[::-1])

# Method 3rd - Swapping first element with last one and second element with second last one and so on..
_list[0], _list[-1] = _list[-1], _list[0]

for i in range(1, len(_list)//2):
    _list[i], _list[len(_list) -i -1] = _list[len(_list) -i -1], _list[i]

print(_list)