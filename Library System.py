import datetime

class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE/SHE RETURNED.\n")
        else:
            issued_date = datetime.date.today()
            due_date = issued_date + datetime.timedelta(days=14)
            track.append({name: [bookname, issued_date, due_date]})
            print(f"BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON OR BEFORE {due_date}.\n")
            self.books.remove(bookname)

    def returnBook(self, name, bookname):
        returned_date = datetime.date.today()
        for entry in track:
            if name in entry:
                issued_date = entry[name][1]
                due_date = entry[name][2]
                if returned_date > due_date:
                    penalty_days = (returned_date - due_date).days
                    penalty = penalty_days * 1  # Assuming a penalty of $1 per day
                    print(f"BOOK RETURNED LATE BY {penalty_days} DAYS. PLEASE PAY A PENALTY OF ${penalty}.\n")
                entry[name][0] = bookname
                entry[name][1] = issued_date
                entry[name][2] = due_date
                break
        else:
            print("YOU HAVE NOT BORROWED THIS BOOK.\n")
        self.books.append(bookname)
        print("BOOK RETURNED : THANK YOU! \n")

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY.\n")
        self.books.append(bookname)

class Student:
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        return name, self.book

    def donateBook(self):
        print("Okay! you want to donate book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":
    Hyderabadlibrary = Library(
        ["graspconcept", "understand", "practice", "consistency", "focus"])
    student = Student()
    track = []

    print("\n\n\n\n\n~~~~~~~~~~~ WELCOME TO THE HYDERABAD LIBRARY ~~~~~~~~~~~~\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books.\n3. Return books\n4. Donate books\n5. Track books\n6. Exit the library\n""")

    while True:
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing books
                Hyderabadlibrary.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                Hyderabadlibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                name, bookname = student.returnBook()
                Hyderabadlibrary.returnBook(name, bookname)
            elif usr_response == 4:  # donate
                Hyderabadlibrary.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for entry in track:
                    for key, value in entry.items():
                        holder = key
                        book, issued_date, due_date = value
                        print(f"{book} book is taken/issued by {holder} from {issued_date} and is due on {due_date}.")
                    print("\n")
                    if len(track) == 0:
                        print("NO BOOKS ARE ISSUED!. \n")
            elif usr_response == 6:  # exit
                print("THANK YOU !\n")
                exit()
            else:
                print("INVALID INPUT! \n")
        except Exception as e:  # catch errors
            print(f"{e}---> INVALID INPUT! \n")