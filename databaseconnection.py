import mysql.connector


# Connection Done with Msql
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pratik@19066"
)


mycursor = mydatabase.cursor()

#mycursor.execute("create database project")

mycursor.execute("use project")


# Tables Created For Maintaining Data of Books,Customer,login information, login status,cart,orders

# mycursor.execute("create table books(book_id int primary key auto_increment, \
#                 book_name varchar(50),Author_name varchar(50),catagory varchar(50),\
#                 language varchar(20),formats_edition varchar(20),rating float,seller varchar(50),\
#                 price double,stock_quantity int,sold_quantity int)")

# The details of books in books table are taken from amazon e-commerce website.
# Stock Quantities are dummy for perfoming operation.

# mycursor.execute("insert into books values(1,'Harry potter and philosophers stone',\
#     'J.K Rowling','Action & Adventure','English','Hardcover',4.7,'PeacockBooks','1256',150,null);")
# mydatabase.commit()

# query = "insert into books(book_name,Author_name,catagory,language,formats_edition,\
#          rating,seller,price,stock_quantity) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# values = [('Harry Potter and the chamber of Secrets', 'J.K Rowling', 'Action & Adventure', 'English', 'Hadrcover', 4.7, 'Sunrise book store', 1316, 155),
#           ('Harry Potter and order of phoeinx', 'J.k Rowling', 'Action & Adventure',
#            'English', 'Paperback', 4.5, 'GoodRead Bookstore', 583, 100),
#           ('Harry Potter and the half blood prince', 'J.K Rowling',
#            'Action & Adventure', 'English', 'Paperback', 4.8, 'u-read store', 462, 120),
#           ('The Complete novels of sherlock Holmes', 'Artur canon doyle',
#            'Action and adventure', 'English', 'Hardcover', 4.5, 'Cloud tail india', 402, 100),
#           ('The Silent Patient', 'Alex Michaelides', 'Action & Adventure',
#            'English', 'Paperback', 4.6, 'cloud tail india', 263, 150),
#           ('The Maidens', 'Alex Michaelides', 'Action & Adventure',
#            'English', 'Hardcover', 4.0, 'Excellent Book Serivce', 719, 100),
#           ('Run and Hide', 'Alan McDermott', 'Action & Adventure', 'English',
#            'Paperback', 4.4, 'university bookstores boston india', 10007, 50),
#           ('Grey Retribution', 'Alan McDermott', 'Action & Adventure', 'English',
#            'Paperback', 4.5, 'university bookstroes boston india', 9304, 60),
#           ('Grey Justice', 'Alan McDermott', 'Action & Adventure',
#            'English', 'Paperback', 4.0, 'Western shop', 9087, 50),
#           ('Verbal and non-verbal reasoning', 'R.S Aggarwal', 'Exam Preparation',
#            'English', 'Paperback', 4.4, 'cloud tail india', 538, 150),
#           ('Quantitative Aptitude for Competitive Examinations', 'R.S Aggarwal',
#            'Exam Preparation', 'English', 'Paperback', 4.4, 'cloud tail india', 452, 150),
#           ('A Modern Approach To Logical Reasoning', 'R.S Aggarwal', 'Exam Preparation',
#            'English', 'Paperback', 4.3, 'cloud tail india', 211, 150),
#           ('Objective General English Book', 'S.P Bakshi',
#            'Exam Preparation', 'English', 'Paperback', 4.3, 'Repro-Books', 285, 100),
#           ('The Psychology of Money', 'Morgan Housel', 'Business & Economics',
#            'English', 'Hardcover', 4.6, 'cloud tail india', 470, 100),
#           ('Rich Dad Poor Dad', 'Robert T. Kiyosaki', 'Business & Economics',
#            'English', 'paperback', 4.6, 'uread-store', 331, 120),
#           ('The Intelligent Investor ', 'Benjamin Graham', 'Business & Economics',
#            'English', 'Paperback', 4.5, 'Book mentor', 470, 50),
#           ('Zero To One', 'Peter Thiel', 'business & Econonmics',
#            'English', 'Paperback', 4.5, 'uread-store', 379, 50),
#           (' BEGINNER’S GUIDE TO LEARN PYTHON', 'Ramsey Hamilton',
#            'Programming', 'English', 'Paperback', 4, 'smart global', 1520, 100),
#           ('Advanced Guide To Learn Python', 'Maurice J. Thompson', 'Programming',
#            'English', 'Paperback', 4, 'cloud tail india', 1064, 100),
#           ('Java: A Beginners Guide', 'Herbert Schildt', 'Programming',
#            'English', 'Paperback', 4.6, 'fast media 2', 3722, 100),
#           ('Java - The Complete Reference', 'Herbert Schildt', 'Programming',
#            'English', 'Paperback', 4, 'cloud tail india', 946, 110),
#           ('The C Programming Language', 'Brain W.Kernighan',
#            'Programmig', 'English', 'Paperback', 4.5, 'spectral', 430, 50),
#           ('Beginners Guide to Learn C Programming', 'Darrel L. Graham', 'Programming',
#            'English', 'Paperback', 4, 'atlantic publishers and distributors', 773, 80),
#           (' Let Us C++', 'yashvant kanetkar', 'Programming',
#            'English', 'Paperback', 4.5, 'Guruji books', 320, 120),
#           ('Mans Search For Meaning', 'Viktor E Frankl', 'History',
#            'English', 'Hardcover', 4.3, 'cloud tail india', 580, 35),
#           ('Mossad', 'Michael bar-zohar', 'History', 'English',
#            'Hardcover', 4.3, 'sunrise book store', 1761, 40),
#           ('A Brief History of Humankind', 'Yuval Noah Harari', 'History',
#            'English', 'Hardcover', 4.3, 'cloud tail india', 2323, 25)
#           ]
# mycursor.executemany(query, values)
# mydatabase.commit()

# mycursor.execute("create table CustomerDetails(Customer_ID  varchar(30) primary key,First_name varchar(30),\
#     Last_name varchar(30),ContactNo Bigint,Country varchar(20),city varchar(20),\
#     DeliveryAddress varchar(50),Pincode Bigint,EmailID varchar(50),Username varchar(50))")


# mycursor.execute(
#     "create table LoginInfo(Customer_ID varchar(30) Primary key,Username varchar(50),\
#     Password varchar(50),foreign key (Customer_ID) references CustomerDetails(Customer_ID)on delete cascade)")


# mycursor.execute(
#     "create table LoginStatus(Customer_ID varchar(30) Primary key,Username varchar(50),\
#     foreign key (Customer_ID) references CustomerDetails(Customer_ID)on delete cascade)")


# mycursor.execute(
#     "create table cart(cart_ID varchar(30) primary key,Customer_ID varchar(30),Username varchar(50),book_ID int,book_name varchar(50),price double)")

# mycursor.execute(
#     "create table MyOrder(Order_ID varchar(30) primary key, cart_ID varchar(30),\
#     Customer_ID varchar(30),Username varchar(50),book_ID int,book_name varchar(50),\
#     Order_Quantity int,Total_Price double,Payment_mode varchar(20),Order_status varchar(20),Order_date date)")
