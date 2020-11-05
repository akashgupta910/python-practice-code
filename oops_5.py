# SPEED() AND OVERRIDING

class Junior:
    junior_class1 = ["Akash","Raj"]

    def __init__(self):
        self.senior = ["Golu"]
        self.junior = ["Ranveer_singh"]

class Senior(Junior):
    senior_junior = ["Kashi","Dil Mohammad"]

    def __init__(self):
        super().__init__()
        self.senior = ["Golu"]
        self.junior = ["Ranveer"]


junior = Junior()
senior = Senior()

print(senior.junior)
