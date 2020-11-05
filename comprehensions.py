# COMPREHENSIONS

# List Comprehensions

list = []

for i in range(100):
    if i%2==0:
        list.append(i)

print(list)

ls = [item for item in range(100) if item%2==0]
print(ls)

# Dictionary Comprehensions

dict1 = {i:f"Item{i}" for i in range(100)}
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

# Set Comprehensions

item = {item for item in ["item1","item2"]}
print(item)

# Generator Comprehensions

odd = (i for i in range(100) if i%3==0)
# print(odd.__next__())
for items in odd:
    print(items,end="")