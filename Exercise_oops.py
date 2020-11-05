class Library:

    def __init__(self, listofbooks, lend_book):
        self.available_books = listofbooks
        self.lend_book = lend_book

    # Display Book Method

    def display_available_books(self):
        print("<-- All Availabe Book are: -->")
        num = 1
        for books in self.available_books:
            print(f"{num}. {books}")
            num = num + 1

    # Lend Book Method

    def lend_books(self):
        lend_book_inp = str(input("Enter the Name of Book which you want to Lend: "))
        if lend_book_inp in self.available_books:
            print("The Book now has been lended which you requested.")
            self.available_books.remove(lend_book_inp)
            self.lend_book.append(lend_book_inp)

        else:
            print("Sorry! This Book is not available in OUR LIBRARY which you requested.")

    # Add Book Method

    def add_book(self):
        add_book = str(input("Enter the Name of Book which you want to add in OUR LIBRARY: "))
        if add_book not in self.available_books:
            self.available_books.append(add_book)
            print(f"Your '{add_book}' name Book successfully added in OUR LIBRARY")
        else:
            print("This book is already added in OUR LIBRARY. so you can not add this book.")

    # Return Book Method

    def return_book(self):
        if not self.lend_book:
            print("You do not Lend any Book yet.")

        elif not self.lend_book == False:
            return_book = input("Enter the Name of book you want to return: ")
            if return_book in self.lend_book:
                print("Thanks to returns the Book which you Lended.")
                self.lend_book.remove(return_book)
                self.available_books.append(return_book)
            else:
                print("You Enter Wrong Book Name, Please Enter correct Name.")


# Main Function -->

def main():
    library = Library(["Rich dad Poor Dad","Think and Grow rich","The One Thing"],[])

    while True:
        print("\n---> OUR LIBRARY <---")
        print("What do you want? \n \t1. Display All Books. \n \t2. Lend a Book. \n \t3. Add a Book. \n \t4. Return a Book.")

        user_inp = int(input("\nEnter your Choice: \n"))

        if user_inp == 1:
            library.display_available_books()

        elif user_inp == 2:
            library.lend_books()

        elif user_inp == 3:
            library.add_book()

        elif user_inp == 4:
            library.return_book()


main()

#  I completed the challenge﻿