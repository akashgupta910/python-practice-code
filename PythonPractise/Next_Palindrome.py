print("\n<---- The Next Palindrome ---->\n")

inpTimes = int(input("How many number do you want to Enter: "))
numList = []

n = 1
for i in range(inpTimes):
    inpNumber = int(input(f"Enter Your Number no {n}: "))
    numList.append(inpNumber)
    n += 1

for i in range(len(numList)):
    b = numList[i]
    while True:
        b += 1
        if b == int(str(b)[::-1]):
            print(f"Next Palindrome for {numList[i]} is {b}.")
            break
        b += 1
    