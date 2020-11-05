
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_roman():
    print("Roman Reign is a wrestler.")

# who_is_roman = dec1(who_is_roman)

who_is_roman()
