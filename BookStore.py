# Packages And Modules I Have Imported In This Project

from typing import Tuple
from databaseconnection import *
import re
import random
import string
from datetime import date


# Some "User Defined Exeception class" Have been Created

class IncorrectPassword(Exception):
    def __init__(self, arg):
        self.msg = arg


class UsernameExist(Exception):
    def __init__(self, arg):
        self.msg = arg


class Username_not_Exist(Exception):
    def __init__(self, arg):
        self.msg = arg


class InvalidPassword(Exception):
    def __init__(self, arg):
        self.msg = arg


class Notloggedin(Exception):
    def __init__(self, arg):
        self.msg = arg


class AlreadyLoggedin(Exception):
    def __init__(self, arg):
        self.msg = arg


class BookNotPresent(Exception):
    def __init__(self, arg):
        self.msg = arg


class DeniedConfirmation(Exception):
    def __init__(self, arg):
        self.msg = arg


# Registration class for creating account,login account for user
# In This Class Single Level Inheritance Implemented

class Registration:
    def __init__(self, EmailID):
        self.EmailID = EmailID


class CreateAccount(Registration):

    def __init__(self, FirstName, LastName, ContactNo, Country, City, DeliveryAddress, Pincode, EmailID, Username, Password):
        self.ValidUser(Username)
        self.ValidPass(Password)
        self.FirstName = FirstName
        self.LastName = LastName
        self.ContactNo = ContactNo
        self.Country = Country
        self.City = City
        self.DeliveryAddress = DeliveryAddress
        self.Pincode = Pincode
        super().__init__(EmailID)
        self.Username = Username
        self.Password = Password

        self.ID = self.GenrateCustomerID()

        sql = "insert into customerdetails (Customer_ID,First_Name,Last_Name,ContactNo,Country,\
            City,DeliveryAddress,pincode,EmailID,Username) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (self.ID, self.FirstName, self.LastName,
                  self.ContactNo, self.Country, self.City, self.DeliveryAddress, self.Pincode, self.EmailID, self.Username)

        mycursor.execute(sql, values)
        mydatabase.commit()

        sql = "insert into logininfo (Customer_ID,Username,Password) values(%s,%s,%s)"
        values = (self.ID, self.Username, self.Password)

        mycursor.execute(sql, values)
        mydatabase.commit()

        print("Hey \'{}\' Welcome To This BookStore, your Account has been created Successfully".format(
            Username))

    def GenrateCustomerID(self):
        total = string.ascii_uppercase + string.digits
        length = 8
        CustomerID = "".join(random.sample(total, length))
        return CustomerID

    def ValidUser(self, user):
        mycursor.execute('select username from logininfo')
        check = mycursor.fetchall()
        for i in check:
            if re.fullmatch(user, i[0]) != None:
                raise UsernameExist('Username already taken')
            else:
                continue
        else:
            return True

    def ValidPass(self, Pass):
        if len(Pass) < 8:
            raise IncorrectPassword(
                'Make sure your password contain 8-16 characters')
        elif re.search('[0-9]', Pass) is None:
            raise IncorrectPassword(
                "Make sure your password contains digit(0-9)")
        elif re.search('[A-Z]', Pass) is None:
            raise IncorrectPassword(
                'Make sure your password contains atleast one capital letter')
        elif re.search('\W', Pass) is None:
            raise IncorrectPassword(
                'Make sure your password contains atleast one special character')
        else:
            return True


class LoginAccount(CreateAccount):
    def __init__(self):
        self.Enter_Login_Credential()
        self.IsusernameExist(self.username)
        self.ValidPass(self.password)
        self.PassCheck(self.username, self.password)
        self.loggedin(self.username)
        print('login successfull')

    def Enter_Login_Credential(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")

    def IsusernameExist(self, user):
        mycursor.execute('select username from logininfo')
        check = mycursor.fetchall()
        for i in check:
            if re.fullmatch(user, i[0]) != None:
                return True
            else:
                continue
        else:
            raise Username_not_Exist('Sorry! invalid Account')

    def PassCheck(self, user, Pass):
        mycursor.execute('select username,password from logininfo')
        check = mycursor.fetchall()
        for i in check:
            if re.fullmatch(user, i[0]) != None and re.fullmatch(Pass, i[1]) != None:
                return True
            else:
                continue
        else:
            raise InvalidPassword('Please Enter Valid Password!')

    def loggedin(self, user):
        mycursor.execute('select customer_ID,username from logininfo')
        check1 = mycursor.fetchall()
        for i in check1:
            if re.fullmatch(user, i[1]) != None:
                mycursor.execute('select username from loginstatus')
                check2 = mycursor.fetchall()
                for j in check2:
                    if re.fullmatch(user, j[0]) != None:
                        raise AlreadyLoggedin(
                            f'This user {user} is already loggedin')
                    else:
                        value = (i[0], i[1])
                        query = (
                            'insert into loginstatus(customer_ID,username) values(%s,%s)')
                        mycursor.execute(query, value)
                        mydatabase.commit()
                        break
                else:
                    value = (i[0], i[1])
                    query = (
                        'insert into loginstatus(customer_ID,username) values(%s,%s)')
                    mycursor.execute(query, value)
                    mydatabase.commit()


def My_account():
    user = input("Enter your username: ")
    query = "select * from customerdetails where username = %s"
    value = user
    mycursor.execute(query, (value,))
    result = mycursor.fetchall()
    for i in result:
        print("Customer_ID = ", i[0])
        print("First_name = ", i[1])
        print("Last_name = ", i[2])
        print("ContactNo = ", i[3])
        print("Country = ", i[4])
        print("City = ", i[5])
        print("delivry_address = ", i[6])
        print("pincode = ", i[7])
        print("Email_ID = ", i[8])
        print("Username = ", i[9])


# Logout() Function if user wants to logout from platform


def Logout(user):
    mycursor.execute('select customer_ID,username from loginstatus')
    check = mycursor.fetchall()
    for i in check:
        if re.fullmatch(user, i[1]) != None:
            value = i[1]
            query = "delete from loginstatus where username = (%s)"
            mycursor.execute(query, (value,))
            mydatabase.commit()
            print("**** LOGED OUT SUCCESSFULLY ****")
            break
        else:
            continue


# SearchBooks class is used to Search books based on some parameter from books table
# In This Class Method Overloadig is implemented

class SearchBooks:
    def Search(self, book_name=0, Author_name=0, Catagory=0, rating=0):
        if book_name == 0 and Author_name == 0 and Catagory == 0 and rating == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                print('\nbook_id = ', row[0])
                print('book_name = ', row[1])
                print('Author_name = ', row[2])
                print('Catagory = ', row[3])
                print('language = ', row[4])
                print('formats_edition = ', row[5])
                print('rating = ', row[6])
                print('seller = ', row[7])
                print('price = ', row[8], "\n")
        elif Author_name == 0 and Catagory == 0 and rating == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if re.fullmatch(book_name, row[1]) != None:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')

        elif book_name == 0 and Catagory == 0 and rating == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if re.fullmatch(Author_name, row[2]) != None:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')

        elif book_name == 0 and Author_name == 0 and rating == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if re.fullmatch(Catagory, row[3]) != None:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')

        elif book_name == 0 and Author_name == 0 and Catagory == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if rating <= row[6]:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')

        elif book_name == 0 and Catagory == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if re.fullmatch(Author_name, row[2]) != None and rating <= row[6]:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')

        elif book_name == 0 and Author_name == 0:
            mycursor.execute(
                'select book_id,book_name,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result = mycursor.fetchall()
            for row in result:
                if re.fullmatch(Catagory, row[3]) != None and rating <= row[6]:
                    print('\nbook_id = ', row[0])
                    print('book_name = ', row[1])
                    print('Author_name = ', row[2])
                    print('Catagory = ', row[3])
                    print('language = ', row[4])
                    print('formats_edition = ', row[5])
                    print('rating = ', row[6])
                    print('seller = ', row[7])
                    print('price = ', row[8], "\n")
                else:
                    raise BookNotPresent('Sorry! Search Not Found... ')


# Purchase Class to purchase books
# In This Class Single Level Inheritance Is Implemented
# User can purchase books Directly by using 'Buy' Class OR User can also first Add items to the cart and then can purchase

class Purchase:
    def __init__(self, username, book_ID):
        self.username = username
        self.book_ID = book_ID


class AddToCart(Purchase):
    def __init__(self, username, book_ID):
        self.Cust_Id = self.isuserloggedin(username)
        self.Tuple = self.GetBook_data(book_ID)
        self.ID = self.GenrateCartID()
        super().__init__(username, book_ID)

        query = "insert into cart(cart_ID,Customer_ID,Username,book_ID,book_name,price) values(%s,%s,%s,%s,%s,%s)"
        values = (self.ID, self.Cust_Id, self.username,
                  self.book_ID, self.Tuple[0], self.Tuple[1])
        mycursor.execute(query, values)
        mydatabase.commit()

        print("******* Item Added to cart succesfully *******")

    def GenrateCartID(self):
        total = string.ascii_uppercase + string.digits
        length = 8
        cart_ID = "".join(random.sample(total, length))
        return cart_ID

    def GetBook_data(self, book_Id):
        mycursor.execute(
            'select book_id,book_name,price,stock_quantity,sold_quantity from books')
        result = mycursor.fetchall()
        for i in result:
            if book_Id == i[0]:
                return i[1], i[2], i[3], i[4]
            else:
                continue

    def isuserloggedin(self, user):
        mycursor.execute('select * from loginstatus')
        check = mycursor.fetchall()
        for i in check:
            if re.fullmatch(user, i[1]) != None:
                return i[0]
            else:
                continue
        else:
            raise Notloggedin('Please Login before buy anything!')


def Show_My_Cart():
    user = input("Enter your username: ")
    query = "select * from cart where username = %s"
    value = user
    mycursor.execute(query, (value,))
    result = mycursor.fetchall()
    for i in result:
        print("\nCart_ID = ", i[0])
        print("Customer_ID = ", i[1])
        print("Username = ", i[2])
        print("book_ID = ", i[3])
        print("book_name = ", i[4])
        print("price = ", i[5])


class Buy(AddToCart):
    payment_mode = 'Cash On Delivery'

    def __init__(self, username, book_ID, Quantity):
        self.Cust_ID = self.isuserloggedin(username)
        self.cart_ID = self.GetCartID(username, book_ID)
        self.Tuple = self.GetBook_data(book_ID)
        self.ID = self.GenrateOrderID()
        Purchase.__init__(self, username, book_ID)
        self.Quantity = Quantity
        self.Total_Price = Quantity * self.Tuple[1]
        self.OrderStatus = 'Order_Confirmed'
        self.order_date = date.today()
        self.OrderConfirmation()

    def OrderConfirmation(self):
        Ans = input("Do You Want To Confirm This Order? YES OR NO ?: ")
        if Ans == 'YES':
            self.updated_Stock_Quantity = self.Tuple[2] - self.Quantity
            if self.Tuple[3] != None:
                self.updated_Sold_Quantity = self.Tuple[3] + self.Quantity
            else:
                sold_quantity = 0
                self.updated_Sold_Quantity = sold_quantity + self.Quantity

            mycursor.execute(
                f"update books set stock_quantity = {self.updated_Stock_Quantity} where book_id = {self.book_ID} ")
            mycursor.execute(
                f"update books set sold_quantity = {self.updated_Sold_Quantity} where book_id = {self.book_ID} ")
            mydatabase.commit()
            self.UpdateCart()
            self.UpdateMyOrder()

            print(
                f"HELLO \'{self.username}\' YOUR ORDER_ID - {self.ID} , YOUR ORDER IS PLACED! THANK YOU FOR SHOPPING WITH US ")
        else:
            raise DeniedConfirmation('You Have Denied Your Order Confirmation')

    def UpdateMyOrder(self):
        query = "insert into myorder(Order_ID,cart_ID,Customer_ID,Username,book_ID,\
        book_name,Order_Quantity,Total_Price,Payment_mode,Order_status,Order_date) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        value = (self.ID, self.cart_ID, self.Cust_ID, self.username, self.book_ID, self.Tuple[0],
                 self.Quantity, self.Total_Price, Buy.payment_mode, self.OrderStatus, self.order_date)

        mycursor.execute(query, value)
        mydatabase.commit()

    def UpdateCart(self):
        query = "delete from cart where cart_ID = %s"
        value = self.cart_ID
        mycursor.execute(query, (value,))
        mydatabase.commit()

    def GenrateOrderID(self):
        total = string.ascii_uppercase + string.digits
        length = 8
        Order_ID = "".join(random.sample(total, length))
        return Order_ID

    def GetCartID(self, user, book_ID):
        mycursor.execute('select cart_id,username,book_id from cart')
        result = mycursor.fetchall()
        for i in result:
            if re.fullmatch(user, i[1]) != None and book_ID == i[2]:
                return i[0]
            else:
                continue
        else:
            return self.GenrateCartID()


# To get order_details ,here is the function  OrderDetails()

def OrderDetails(username):
    mycursor.execute('select * from myorder')
    result1 = mycursor.fetchall()
    for i in result1:
        if re.fullmatch(username, i[3]) != None:
            print("\n**** ORDER DETAILS ****\n")
            print('Order_ID = ', i[0])
            print('cart_ID = ', i[1])
            print('Customer_ID = ', i[2])
            print('Username = ', i[3], '\n')
            print("**** BOOK DETAILS ****\n")
            print('Book_ID = ', i[4])
            print('Book_name = ', i[5])
            mycursor.execute(
                'select book_ID,Author_name,catagory,language,formats_edition,rating,seller,price from books')
            result2 = mycursor.fetchall()
            for j in result2:
                if i[4] == j[0]:
                    print('Author_name = ', j[1])
                    print('Catagory = ', j[2])
                    print('Language = ', j[3])
                    print('Formats_Edition = ', j[4])
                    print('Rating = ', j[5])
                    print('Seller = ', j[6], '\n')
                    print("**** PRICE DETAILS ****\n")
                    print('Price\\Unit = ', j[7])
                    print('Order_Quantity = ', i[6])
                    print('Total_Bill_Amount = ', i[7])
                    print('Mode_of_Payment = ', i[8])
                    print('Order_Status = ', i[9], '\n')
                    print("**** SHIPPING DETAILS ****\n")
                    mycursor.execute('select *  from customerdetails')
                    result3 = mycursor.fetchall()
                    for k in result3:
                        if re.fullmatch(i[2], k[0]) != None:
                            print('First_name = ', k[1])
                            print('Last_name = ', k[2])
                            print('Contact_No = ', k[3])
                            print('Delivery_Address = ', k[6])
                            print('City = ', k[5])
                            print('Country = ', k[4])
                            print('Pincode = ', k[7])
                            print('EmailID = ', k[8])
                            print('Order_date = ', i[10])
                            print('Estimate_Delivery = 7 days from Order_date \n')


# TO cancle Order before Delivery ,here is the fucntion cancleOrder()

def CancelOrder(username):
    OrderDetails(username)
    print("Please enter Order_ID and Book_ID to cancle your order \n")
    Order_ID = input("Order_ID = ")
    Book_ID = int(input("Book_ID = "))
    mycursor.execute('select Order_ID,book_ID,Order_Quantity from myorder')
    result1 = mycursor.fetchall()
    for i in result1:
        if re.fullmatch(Order_ID, i[0]) != None and Book_ID == i[1]:
            Quantity = i[2]
            mycursor.execute(
                'select book_id,stock_quantity,sold_quantity from books')
            result2 = mycursor.fetchall()
            for j in result2:
                if Book_ID == j[0]:
                    Update_stock_quantity = j[1] + Quantity
                    Update_sold_quantity = j[2] - Quantity
                    mycursor.execute(
                        f"update books set stock_quantity = {Update_stock_quantity} where book_id = {Book_ID}")
                    mycursor.execute(
                        f"update books set sold_quantity = {Update_sold_quantity} where book_id = {Book_ID}")
                    mydatabase.commit()
                    query = "delete from myorder where Order_ID = %s"
                    value = Order_ID
                    mycursor.execute(query, (value,))
                    mydatabase.commit()
                    print(
                        f"\"YOU HAVE CANCLED YOUR ORDER_ID - {Order_ID},THANK YOU FOR VISITING\"")
                    break


# To find Which book is maximum sold ,here is the function MaxSoldBooks()

def MaxSoldBooks():
    mycursor.execute(
        "select * from books where sold_quantity = (select max(sold_quantity) from books)")
    result = mycursor.fetchall()
    for i in result:
        print("******* THIS BOOK IS MAXIMUM SOLD OUT *******\n")
        print("\nBook_ID = ", i[0])
        print("Book_name = ", i[1])
        print("Author_name = ", i[2])
        print("Catagory = ", i[3])
        print("Languge = ", i[4])
        print("Formats_Edition = ", i[5])
        print("Rating = ", i[6])
        print("Seller = ", i[7])
        print("Price = ", i[8])
        print("Stock_quantity = ", i[9])
        print("Sold_quantity = ", i[10], '\n')


# To find Which book is minimum sold ,here is the fucntion MinSoldBooks()


def MinSoldBooks():
    mycursor.execute(
        "select * from books where sold_quantity = (select min(sold_quantity) from books)")
    result = mycursor.fetchall()
    for i in result:
        print("******* THIS BOOK IS MINMUM SOLD OUT *******\n")
        print("\nBook_ID = ", i[0])
        print("Book_name = ", i[1])
        print("Author_name = ", i[2])
        print("Catagory = ", i[3])
        print("Languge = ", i[4])
        print("Formats_Edition = ", i[5])
        print("Rating = ", i[6])
        print("Seller = ", i[7])
        print("Price = ", i[8])
        print("Stock_quantity = ", i[9])
        print("Sold_quantity = ", i[10], '\n')


# If user wants to delete their account from the platform, here is the function DeleteAccount()

def DeleteAccount(username):
    query = "Delete from customerdetails where username = %s"
    value = username
    mycursor.execute(query, (value,))
    mydatabase.commit()
    print("**** ACCOUNT DELETED SUCCESSFULLY ****")
