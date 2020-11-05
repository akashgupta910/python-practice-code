def names():
    import time
    names = "akash harry haris carry amit ajey bhuvan shubham rahul aftab hrithik vivek ujjawal mohit rohit"
    time.sleep(2)

    while True:
        text = (yield)
        if text in names:
            print("Your name is in the list.")
        else:
            print("Your name is not in the list.")

name = names()
next(name)
name.send(input("Type your Name: "))
name.close()

