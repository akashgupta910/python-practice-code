# GENERATOR

"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(9)
print(g.__next__())
print(g.__next__())

name = "Akash"
iter_name = iter(name)
# print(iter_name.__next__())

for i in iter_name:
    print(i,end="")

