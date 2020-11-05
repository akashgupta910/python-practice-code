# def funargs(my_argu, *args , **kwargs):
#
#     print(f"{my_argu}\n")
#
#     for item in args:
#         print(item)
#
#     print("\n")
#     for key,value in kwargs.items():
#         print(f"{key} experts in {value}")
#
# programmer_channel = ["Code with Harry","Clever Programmer","CS Dojo","Telusko"]
# programmer_languages = {"code with Harry":"Python", "clever programmer":"Python","cs dojo":"Python","Telusko":"Java"}
#
# my_argu = "My Name is Akash Gupta"
#
# funargs(my_argu, *programmer_channel, **programmer_languages)
#

from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")

    def favicon(self, filename):
        self.wm_iconbitmap(filename)

    def menu(self, *args):
            menu = Menu(self)
            for menu_name in args:
                menu.add_command(label=f"{menu_name}")
            self.config(menu=menu)


if __name__ == '__main__':
    window = GUI()
    window.favicon("file/notepad.ico")
    window.title("Notepad")

    window.menu("File", "Edit", "Navigate", "Code")
    window.mainloop()
