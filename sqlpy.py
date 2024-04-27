import tkinter 
from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox

# establish database connection
db = pymysql.connect(host='localhost', user='root', password='Nida@2004', database='yampa')
cursor = db.cursor()

top = tkinter.Tk()
top.geometry("1920x1080")
top.configure(bg="light blue")

L = Label(top, text="WELCOME TO YAMPA-SJCE", fg='red',height=3, font= 16)
L.grid(row=0, column=2)
L.configure(bg="light blue")


L1 = Label(top, text="Enter your customerid: ", fg='blue', font=14)
L1.grid(row=1, column=1)
L1.configure(bg="light blue")
E1 = Entry(top, bd=5, width=120)
E1.grid(row=1, column=2)

L2 =Label(top,text = "Enter your order_id: ",fg = 'blue', font=14)
L2.grid(row=2,column =1)
L2.configure(bg="light blue")
E2=Entry(top,bd=5,width=120)
E2.grid(row=2,column=2)


def cancel_order():
    # create a cursor object
    customerid = E1.get()
    itemid =E2.get()
    cursor = db.cursor()
    
    # delete the row with given customer_id and item_id from ordertable
    delete_query = "DELETE FROM ordertable WHERE customerid=%s AND itemid=%s"
    cursor.execute(delete_query, (customerid, itemid))
    
    # commit the transaction
    db.commit()
    
    # close the cursor
    cursor.close()
    
    print("Order for customer ID", customerid, "and item ID", itemid, "has been cancelled.")



def search_data():
    # clear previous search results
    for row in table.get_children():
        table.delete(row)

    # get input values
    customerid = E1.get()

    # retrieve data from database
    sql = f"SELECT customer.*, ordertable.itemid, ordertable.totalprice FROM customer JOIN ordertable ON customer.customerid=ordertable.customerid WHERE customer.customerid='{customerid}'"
    cursor.execute(sql)
    data = cursor.fetchall()

    # insert retrieved data into table widget
    for row in data:
        table.insert('', END, values=row)

def add_to_order(itemid):
    # insert a new row into the ordertable
    customerid = E1.get()
    # customerid = int(customerid)
    query = "INSERT INTO ordertable (customerid, itemid) VALUES (%s, %s)"
    values = (customerid, itemid)
    cursor.execute(query, values)
    db.commit()  # commit the transaction


# Define a function to create a product box
def create_product_box(name, price, detail, image_file, row, column, itemid):
    # Create a frame to hold the product information
    product_frame = tkinter.Frame(top, bd=3, relief="raised", padx=13, pady=13)
    product_frame.grid(row=row, column=column, padx=20, pady=20)

    # Create a label to display the product name
    product_name_label = tkinter.Label(product_frame, text=name, font=("Helvetica", 20, "bold"))
    product_name_label.pack()

    # Create a label to display the product price
    product_price_label = tkinter.Label(product_frame, text=price, font=("Helvetica", 14))
    product_price_label.pack()

    # Create a label to display the product details
    product_detail_label = tkinter.Label(product_frame, text=detail, font=("Helvetica", 10), wraplength=300)
    product_detail_label.pack(pady=12)

    # Load the image
    image = tkinter.PhotoImage(file=image_file)

    # Create a label to display the image
    image_label = tkinter.Label(product_frame, image=image)
    image_label.image = image
    image_label.pack(side="top", padx=5)

    # Create a button to buy the product
    # create the buy button and associate it with the add_to_order function
    buy_button = tkinter.Button(product_frame, text="Buy Now", bg="green", fg="white", font=("Helvetica", 14), command=lambda: add_to_order(itemid))
   

    buy_button.pack(pady=15)



# Create 5 product boxes
create_product_box("Burger", "40", "Juicy patty with green veggies", "burger.png", 12, 1,1)
create_product_box("Sandwich", "30", "Rich cheesy layer with creamy veggies", "sandwich.png", 12, 2,2)
create_product_box("Milkshakes", "30", "Yummy thickshakes", "milkshake.png", 12, 3,3)



def update_order():
    customerid = E1.get()
    itemid = E2.get()
    try:
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Update the order table for the given customer id
        update_query = "UPDATE ordertable SET itemid = %s WHERE customerid = %s ORDER BY orderid DESC LIMIT 1"
        cursor.execute(update_query, (itemid, customerid))
        
        # Commit the transaction
        db.commit()
        
        print(f"Order for customer id {customerid} has been updated with item id {itemid}")
        
    except pymysql.Error as e:
        print(f"Error updating order: {e}")
        
    finally:
        # Close the database connection
        db.close()



def myButtonEvent():
    # get input values
    customerid = E1.get()
    itemid = E2.get()

    # retrieve data from database
    sql = f"SELECT * FROM customer WHERE customerid='(int){customerid}'"
    cursor.execute(sql)
    customeriddata = cursor.fetchone()

    sql = f"SELECT * FROM menu WHERE id='(int){itemid}'"
    cursor.execute(sql)
    itemiddata = cursor.fetchone()

    # add order to database
    sql = f"INSERT INTO orders (customerid, itemid, price) VALUES ('{customerid}', '{itemid}', '{itemiddata[2]}')"
    cursor.execute(sql)
    db.commit()

    # show confirmation message
    messagebox.showinfo("Confirmation", f"Order for product {itemiddata[1]} with ID {itemid} has been placed by customer {customeriddata[1]} with ID {customerid}.")



Bcancel = tkinter.Button(text='Cancel order', fg='blue', bg='orange', command=lambda: cancel_order())
Bcancel.grid(row=8, column=3)


Breplace = tkinter.Button(text='Remove from cart', fg='blue', bg='orange', command=lambda: update_order())
Breplace.grid(row=8, column=1)


table = ttk.Treeview(top, padding= 5, columns=('ID', 'Name', 'Contact', 'Itemid'), show='headings')
table.configure(height=3)
table.heading('ID', text='ID')
table.column('ID', width=60)
table.heading('Name', text='Name')
table.column('Name', width=200)
table.heading('Contact', text='Contact')
table.column('Contact', width=100)
table.heading('Itemid', text='Itemid')
table.column('Itemid', width=100)
table.grid(row=4, column=1, columnspan=10)

BSearch = tkinter.Button(text='Search', fg='blue', bg='orange', command=search_data)
BSearch.grid(row=1, column=3)


top.mainloop()