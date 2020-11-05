from random import randint

print("\n<---- Funny Names ---->\n")

inpTimes = int(input("Enter Number of Friends: "))

namesList = []

print(f"\n<-- Enter the Name of your {inpTimes} friends -->")
for i in range(inpTimes):
    inpNames = input()
    namesList.append(inpNames.split())

n = 0
for i in range(len(namesList)):
    randomNum = randint(0, len(namesList)-1)
    if randomNum == n:
        randomNum += 1
    namesList[i][-1] = namesList[randomNum][-1]
    n += 1
    
print("\n<-- Funny Names :-) -->\n")

for i in range(len(namesList)):
    for j in namesList[i]:
        print(j, end=" ")
    print("\n")
                                                                                                           