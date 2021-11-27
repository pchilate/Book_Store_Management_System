from BookStore import *
from databaseconnection import *


def Lets_Execute_this():
    while True:
        print("Enter \'CreateAccount\' to Create an account in this platform")
        print("Enter \'Myaccount\' to get your account details")
        print("Enter \'Login\' to Login in this platform")
        print("Enter \'Logout\' to Logout from this platform")
        print("Enter \'Search\' to Search books")
        print("Enter \'AddToCart\' to add your item to the cart")
        print("Enter \'Show_my_cart\' to get your cart details")
        print("Enter \'Buy\' to purchase/buy item.")
        print("Enter \'Orderdetails\' to get your order details")
        print("Enter \'CancleOrder\' to Cancle your order")
        print("Enter \'Max sold\' to get which book is maximum sold out")
        print("Enter \'Min sold\' to get which book is minimum sold out")
        print("Enter \'delete Account\' to delete your account from this platform\n")

        Press = input("Press any of the above tab to execute: ")

        if Press == 'CreateAccount':
            print("**** PLEASE ENTER YOUR DETAILS ****\n")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            ContactNo = input("Enter your contact number: ")
            Country = input("Enter your country: ")
            city = input("Enter your city: ")
            delivery_address = input("Enter your delivery_address: ")
            pincode = input("Enter your pincode: ")
            Email_ID = input("Enter your Email_ID: ")
            Username = input("Create username: ")
            password = input("set password: ")

            open_account = CreateAccount(first_name, last_name, ContactNo, Country,
                                         city, delivery_address, pincode, Email_ID, Username, password)

            break

        elif Press == 'Myaccount':
            My_account()
            break

        elif Press == 'Login':
            login = LoginAccount()
            break

        elif Press == 'Logout':
            user = print("Enter Username to logout: ")
            Logout(user)
            break

        elif Press == 'Search':
            search = SearchBooks()
            print("\nEnter <nothing>/<empty string> to search all the books.")
            print("Enter <Book_name> to search book by its name.")
            print("Enter <Author_name> to search book by its author_name.")
            print("Enter <Catagory> to search book by its catagory.")
            print("Enter <rating> to search book having rating you enterd and above.")
            print(
                "Enter <Author_name> and <Rating> to search book by author_name and rating.")
            print(
                "Enter <catagory> and <rating> to search book by catagory and rating.\n")

            enter = input("Enter here: ")
            if enter == "":
                search.Search()
            elif enter == "Book_name":
                search.Search(book_name=input("Enter book name: "))
            elif enter == "Author_name":
                search.Search(Author_name=input("Enter Author name: "))
            elif enter == "catagory":
                search.Search(Catagory=input("Enter catagory: "))
            elif enter == "rating":
                search.Search(rating=input("Enter rating: "))
            elif enter == "Author_name and rating":
                search.Search(Author_name=input(
                    "Enter Author name: "), rating=input("Enter rating: "))
            elif enter == "Catagory and rating":
                search.Search(Catagory=input("Enter catagory: "),
                              rating=input("Enter rating: "))
            else:
                print("search again")

            break

        elif Press == 'AddToCart':
            user = input("Enter username: ")
            book_id = int(input("Enter \'book_id\' to add to cart: "))

            add_item = AddToCart(user, book_id)
            break

        elif Press == 'Show_my_cart':
            Show_My_Cart()

            break

        elif Press == 'Buy':
            user = input("Enter username: ")
            book_id = int(input("Enter book_id: "))
            quantity = int(
                input("Enter how many quantities you want to buy: "))

            buy_item = Buy(user, book_id, quantity)

            break

        elif Press == 'Orderdetails':
            user = input("Enter Username: ")
            OrderDetails(user)

            break

        elif Press == 'CancleOrder':
            user = input("Enter Username: ")
            CancelOrder(user)

            break

        elif Press == 'Max sold':
            MaxSoldBooks()

            break

        elif Press == 'Min sold':
            MinSoldBooks()
            break

        elif Press == 'delete Account':
            user = input("Enter username: ")
            DeleteAccount(user)
            break

        else:
            continue


Lets_Execute_this()
