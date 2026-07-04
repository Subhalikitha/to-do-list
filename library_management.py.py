books = []
def login():
    username = "likitha"  
    password = "1234"
    user = input("Enter your name: ")
    pwd = input("Enter password: ")
    
    if user == username and pwd == password:
     print("Login successfull")
     return True
    else:
     print("Enter valid details")
     return False
def add_book():
    id = input("Enter Book id")
author = input("Enter book Author")
title = input("Enter book Title")
quantity = int(input("Enter book Quantity"))

book = {
    "Book ID": id,
        "Title": title,
        "Author": author,
        "Quantity": quantity
    }
books.append(book)
print("book added successfully")
def search_book():
    id = input("Enter book ID")
    found = False
    for book in books:
        if book["Book id"] == id:
            print("Book found")
            print("Book ID :", book["Book ID"])
            print("Title   :", book["Title"])
            print("Author  :", book["Author"])
            print("Quantity:", book["Quantity"])
            found = True
            break

    if not found:
        print("Book not found!")
def issue_book():
    ID = input("Enter book id")
    found = False
    for book in books:
        if book["Book id"] == ID:
           if book["Quantity"]>0:
               book["Quantity"] -= 1
               print("Book issued sucessfully")
           else:
            print("sorry!This book is out of stock")
            break
    
def return_book():
    Book_id = input("Enter book id")
    found = False
    for book in books:
        if book["BOOK ID"] == Book_id:
            book["Quantity"] += 1
            print("Book returned successfully")
        else:
            print("Book is not returned")
def calculate_fine():
    allowed_days = 7
    fine_per_day = 5 
    days = int(input("Enter no of days book was kept"))
    if days<=allowed_days:
        print("No fine")
    else:
        extra_days = days - allowed_days
        fine = extra_days*fine_per_day
        print("Fine Amount = ",fine)           
if login():

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Fine Calculation")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            search_book()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            calculate_fine()

            break

        else:
            print("Invalid Choice!")

