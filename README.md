Before going to backend(sql) part install some python library like :

pip install tk pymysql cryptography 

execute above command 

Step 1: Open the MySQL command prompt or any MySQL client of your choice.

Step 2: Create the yampa database using the following command:


CREATE DATABASE yampa;

Step 3: Switch to the yampa database:


USE yampa;

Step 4: Create the menu table using the following command:



CREATE TABLE menu (
    itemid INT PRIMARY KEY, 
    itemname VARCHAR(10), 
    prices INT 
    );


Step 5: Insert the data INTo the menu table using the following command:



INSERT INTO menu (itemid, itemname, prices) VALUES
(1, 'burger', 40), 
(2, 'sandwich', 30), 
(3, 'milkshake', 30);



Step 6: Create the customer table using the following command:


CREATE TABLE customer (
    customerid INT PRIMARY KEY, 
    customername VARCHAR(20), 
    contactno INT
    );



Step 7: Insert the data INTo the customer table using the following command:


INSERT INTO customer VALUES 
(1, 'Alex', 11111111),
(2, 'Barney', 555555555),
(3, 'Haley', 22222222);


You can insert some more values.


Step 8: Create the ordertable using the following command:


CREATE TABLE ordertable (
    orderid INT primary KEY AUTO_INCREMENT,
    customerid INT,
    itemid INT,
    totalprice INT,
    FOREIGN KEY (customerid) REFERENCES customer(customerid),
    FOREIGN KEY (itemid) REFERENCES menu(itemid)
    );


Step 9: Insert the data into the ordertable using the following command:

INSERT INTO ordertable (customerid, itemid, totalprice) VALUES 
(1, 1, 40),
(2, 3, 30),
(3, 2, 30);



That's it! You have successfully created the yampa database with three tables - menu, customer, and ordertable.

Lastly, remember to update the front end code with your host, user, password, database values of mySQL Workbench in this line

db = pymysql.connect(host='localhost', user='root', password='your-password', database='your-database-name')


Note: Usuallly, the host='localhost' and user='root'.

