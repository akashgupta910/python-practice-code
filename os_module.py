import os

print(dir(os))

print(os.getcwd())
os.chdir("c://")
print(os.getcwd())

f = open("file/file.txt")
print(os.listdir())
print(os.listdir("c://"))

os.mkdir("this")
os.makedirs("that/this")

os.rename("that","folder")

print(os.environ.get("Path"))

print(os.path.join("c:/","folder"))

print(os.path.exists("c://Program Files"))
print(os.path.isdir("c://Program Files"))
print(os.path.isfile("c://Program Files"))
