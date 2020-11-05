item = ["Phone","Laptop","Headphone"]

for items in item:
    print(items)

else:
    print("Loop ends properly.")

for items in item:
    if items == "charger":
        print(items)
        break

else:
    print("Your item does not found!")
