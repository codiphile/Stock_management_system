import tkinter as tk
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="stock"
)
cursor = mydb.cursor()


def insert_data():
    stock_name_value = stock_name.get()
    quantity_value = quantity.get()
    purchase_price_value = purchase_price.get()
    current_price_value = current_price.get()  # New field

    if (
        not stock_name_value
        or not quantity_value
        or not purchase_price_value
        or not current_price_value
    ):
        print("Please fill in all fields.")
        return

    sql = "INSERT INTO stock (stock_name, quantity, purchase_price, current_price) VALUES (%s, %s, %s, %s)"
    val = (
        stock_name_value,
        quantity_value,
        purchase_price_value,
        current_price_value,
    )  # Include current_price

    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def display_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM stock")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


root = tk.Tk()
root.title("Stock Market Portfolio")

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame_left, text="Stock Name").grid(row=0, column=0, padx=5, pady=5)
stock_name = tk.Entry(frame_left)
stock_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Quantity").grid(row=1, column=0, padx=5, pady=5)
quantity = tk.Entry(frame_left)
quantity.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Purchase Price").grid(row=2, column=0, padx=5, pady=5)
purchase_price = tk.Entry(frame_left)
purchase_price.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Current Price").grid(
    row=3, column=0, padx=5, pady=5
)  # New label
current_price = tk.Entry(frame_left)
current_price.grid(row=3, column=1, padx=5, pady=5)  # New entry field

insert_button = tk.Button(frame_left, text="Insert Data", command=insert_data)
insert_button.grid(row=4, column=1, padx=5, pady=5)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame_right, text="Stock Data").pack(pady=5)
tree = ttk.Treeview(
    frame_right, columns=("Stock Name", "Quantity", "Purchase Price", "Current Price")
)
tree.heading("#1", text="Stock Name")
tree.heading("#2", text="Quantity")
tree.heading("#3", text="Purchase Price")
tree.heading("#4", text="Current Price")
tree.pack()

display_button = tk.Button(frame_right, text="Display Data", command=display_data)
display_button.pack(pady=5)

root.mainloop()
