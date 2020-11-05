import pickle

# Pickling a Python Object

phone = ["Samsung J7", "LG Magna", "Mi A1"]
file = "file/phone.pic"
file_object = open(file, "wb")
pickle.dump(phone, file_object)
file_object.close()

# Depickling a Python Object

file = "file/phone.pic"
file_object = open(file, "rb")
phone = pickle.load(file_object)
print(phone)
print(type(phone))
