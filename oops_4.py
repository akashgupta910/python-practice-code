# MULTILEVEL INHERITANCE

class Electronic_device:

    def __init__(self, devices):
        self.device = devices

    def printdev(self):
        return f"Electronic device is {self.device}."

class Pocket_gadget(Electronic_device):

    def __init__(self ,devices, gadget):
        self.device = devices
        self.gadget = gadget

    def printgadget(self):
        return f"Electronic device is {self.device}. Pocket Gadget is {self.gadget}."

class Phone(Pocket_gadget):

    def __init__(self ,devices, gadget, phone):
        self.device = devices
        self.gadget = gadget
        self.phone = phone

    def printphone(self):
        return f"Electronic device is {self.device}. Pocket Gadget is {self.gadget}. Phone is {self.phone}."

device_obj = Electronic_device(["Computer","Laptop"])
gadgte_obj = Pocket_gadget(["Computer","Laptop"],["Mobile","Calculator"])
phone_obj = Phone(["Computer","Laptop"],["Mobile","Calculator"],["Mi A1","LG Magna"])

print(phone_obj.printdev())
print(gadgte_obj.printdev())