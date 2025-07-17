import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CafeDB"
)
cursor = conn.cursor()

def show_menu():
    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()
    print("\n--- Cafe Menu ---")
    for item in menu_items:
        print(f"{item[0]}. {item[1]} - ₹{item[2]}")
    print("-----------------")

def add_menu_item():
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    cursor.execute("INSERT INTO menu (item_name, price) VALUES (%s, %s)", (item_name, price))
    conn.commit()
    print("Item added successfully!")

def delete_menu_item():
    item_id = int(input("Enter item ID to delete: "))
    cursor.execute("DELETE FROM menu WHERE item_id = %s", (item_id,))
    conn.commit()
    print("Item deleted successfully!")

def place_order():
    show_menu()
    item_id = int(input("Enter item ID to order: "))
    quantity = int(input("Enter quantity: "))
    cursor.execute("SELECT price FROM menu WHERE item_id = %s", (item_id,))
    item = cursor.fetchone()
    
    if item:
        total_price = item[0] * quantity
        cursor.execute("INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)", (item_id, quantity, total_price))
        conn.commit()
        print(f"Order placed successfully! Total Bill: ₹{total_price}")
    else:
        print("Invalid item ID!")

while True:
    print("\n1. Admin Panel")
    print("2. Customer Panel")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- Admin Panel ---")
        print("1. Add Menu Item")
        print("2. Delete Menu Item")
        print("3. View Menu")
        admin_choice = input("Choose an option: ")

        if admin_choice == "1":
            add_menu_item()
        elif admin_choice == "2":
            delete_menu_item()
        elif admin_choice == "3":
            show_menu()
        else:
            print("Invalid choice!")

    elif choice == "2":
        print("\n--- Customer Panel ---")
        print("1. View Menu")
        print("2. Place Order")
        customer_choice = input("Choose an option: ")

        if customer_choice == "1":
            show_menu()
        elif customer_choice == "2":
            place_order()
        else:
            print("Invalid choice!")

    elif choice == "3":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")

cursor.close()
conn.close()
