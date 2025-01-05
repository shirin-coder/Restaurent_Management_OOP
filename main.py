from food_item import FoodItem
from menu import Menu
from users import Customer,Admin,Employee
from restaurent import Restaurent
from orders import Order

mamar_rest = Restaurent("Mamar Restaurent")
# customer interface
def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")

    customer = Customer(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {customer.name}!!")
        print("1.View Menu")
        print("2.Add item to cart")
        print("3.View cart")
        print("4.PayBill")
        print("5.Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            customer.view_menu(mamar_rest)

        elif choice == 2:
            item_name = input("enter item name : ")
            item_quantity = int(input("enter item quantity : "))

            customer.add_to_cart(mamar_rest,item_name,item_quantity)

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break
        else:
            print("Invalid input")

# admin interface

def admin_interface():
    name = input("Enter your name: ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")

    admin = Admin(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {admin.name}!!")
        print("1.Add new item")
        print("2.Add new employee")
        print("3.View employee")
        print("4.View items")
        print("5.Delete items")
        print("6.Exit")


        choice = int(input("Enter your choice : "))

        if choice == 1:
            item_name = input("Enter item name : ")
            item_price = int(input("Enter item price : "))
            item_quantity = int(input("Enter item quantity : "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_rest,item)


        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")
            employee = Employee(name, phone, email, address,age,designation,salary)
            admin.add_employee(mamar_rest,employee)


        elif choice == 3:
            admin.view_employee(mamar_rest)

        elif choice == 4:
            admin.view_menu(mamar_rest)

        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(mamar_rest,item_name)

        elif choice == 6:
            break
        else:
            print("Invalid input")

while True:
    print("WELCOME!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        customer_menu()

    elif choice == 2:
        admin_interface()
    elif choice == 3:
        break
    else:
        print("INVALID INPUT")