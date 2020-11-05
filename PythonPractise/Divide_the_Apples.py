print("\n<---- Divivde The Apples ---->\n")

n = int(input("Enter the no. of apples Harry has: "))
mn = int(input("Enter minimum No: "))
mx = int(input("Enter maximum No: "))

if mn == mx:
    print("There is no Divisor!\n")

elif mn > mx:
    print("Value Error!\n")

else:
    for i in range(mn, mx+1):
        if n%i == 0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")