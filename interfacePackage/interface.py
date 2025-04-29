#interface.py

from customerPackage.customer import Customer
from shoppingCartPackage.shoppingCart import ShoppingCart
from staffPackage.staff import Staff
from userPackage import user

class Interface:
    def __init__(self):
        self.show_menu()       

    def bear(self):
        print("ʕᵔᴥᵔʔ")
        
    def show_menu(self):
        print("=== Menu ===")
        print("1. Staff")
        print("2. Customer")
        print("3. End Session")
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    print("\n")
                    print("Loading Staff...")
                    print("\n")
                    return StaffInterface()
                elif (userInput == 2):
                    print("\n")
                    print("Loading Customer...")
                    print("\n")
                    return CustInterface()
                elif (userInput == 3):
                    print("\n")
                    print("Ending Session...")
                    print("Bye Bye!")
                    self.bear()
                    exit()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input. Please type either '1' - Staff, '2' - Customer, '3' - End session.")        

########################################## STAFF INTERFACE SUBCLASS #################################################

class StaffInterface(Interface):

    def __init__(self):
        self.staffMember = Staff() # Staff connection to DB from Staff Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Staff Menu ===")

    def show_menu(self):
        print("1. View Products") #GOOD
        print("2. Add Products and Price") #GOOD
        print("3. Modify Products and Price") #GOOD
        print("4. Delete Products and Price") #GOOD
        print("5. View Stock Inventory") #GOOD
        print("6. Add Stock to Warehouse") #GOOD
        print("7. End Staff Session") #GOOD
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.staffMember.show_products()
                elif (userInput == 2):
                    prodNo = input("Product ID: ")
                    price = float(input("Price: "))
                    self.staffMember.add_product(prodNo, price)
                elif (userInput == 3):
                    prodNo = input("Product ID: ")
                    price = float(input("Price: "))
                    self.staffMember.modify_product(prodNo, price)
                elif (userInput == 4):
                    prodNo = input("Product ID to be deleted: ")
                    self.staffMember.delete_product(prodNo)
                elif (userInput == 5):
                    self.staffMember.show_stock()
                elif (userInput == 6):
                    prodNo = input("Product[Stock] ID: ")
                    qty = int(input("Quantity: "))
                    wh_id = input("Warehouse ID: ")
                    self.staffMember.add_stock(prodNo, qty, wh_id)
                elif (userInput == 7):
                    print("\n")
                    print("Ending Staff Session...")
                    self.bear()
                    print("\n")
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## CUSTOMER INTERFACE SUBCLASS #################################################

class CustInterface(Interface):
    def __init__(self):
        cust_id = input("Enter Customer ID: ")
        self.custMember = Customer() # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Customer Menu ===")

    def show_menu(self):
        print("1. View Products") # good
        print("2. View Cart")
        print("3. Checkout")
        print("4. Manage Credit Cards") #good
        print("5. Manage Addresses") #good
        print("6. View Balance") #good 
        print("7. Logout") #good
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.show_products()
                elif (userInput == 2):
                    return ShopCart()
                elif (userInput == 3):
                    return Checkout()
                elif (userInput == 4):
                    return Card()
                elif (userInput == 5):
                    return Address()
                elif (userInput == 6):
                    self.custMember.view_balance()
                elif (userInput == 7):
                    print("\n")
                    print("Ending Customer Session...")
                    print("\n")
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input.")   

########################################## CARD INTERFACE SUBCLASS #################################################

class Card(CustInterface):

    def __init__(self):
        self.custMember = Customer() # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Manage Cards Menu ===")

    def show_menu(self):
        print("1. View Cards") #good IT
        print("2. Add Credit Card") #good IT
        print("3. Modify Credit Card") #good IT
        print("4. Delete Credit Card") #good IT
        print("5. Return to Customer Menu") #good IT
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.view_cards()
                elif (userInput == 2):
                    self.custMember.add_card()
                elif (userInput == 3):
                    self.custMember.modify_card()
                elif (userInput == 4):
                    self.custMember.delete_card()
                elif (userInput == 5):
                    print("\n")
                    print("Closing Card Menu...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## ADDRESS INTERFACE SUBCLASS #################################################

class Address(Interface):

    def __init__(self):
        self.staffMember = Customer() # Staff connection to DB from Staff Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Manage Address Menu ===")

    def show_menu(self):
        print("1. View Address")
        print("2. Add Address")
        print("3. Modify Address")
        print("4. Delete Address")
        print("5. Return to Customer Menu")
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.view_cards()
                elif (userInput == 2):
                    self.custMember.add_card()
                elif (userInput == 3):
                    self.custMember.modify_card()
                elif (userInput == 4):
                    self.custMember.delete_card()
                elif (userInput == 5):
                    print("\n")
                    print("Closing Address Menu...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## SHOPPING CART INTERFACE SUBCLASS #################################################

class ShopCart(Interface):

    def __init__(self):
        self.staffMember = Customer()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Manage Shopping Cart Menu ===")

    def show_menu(self):
        print("1. View Cart")
        print("2. Add Product") #good IT
        print("2. Remove Product")
        print("3. Change Product Quantity") 
        print("4. Delete Credit Card") #good IT
        print("5. Return to Customer Menu") #good IT
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.view_cards()
                elif (userInput == 2):
                    prodNo = input("Product ID: ")
                    qty = input("Quantity: ")
                    self.shopCart.add_item(prodNo,qty)
                elif (userInput == 3):
                    self.custMember.modify_card()
                elif (userInput == 4):
                    self.custMember.delete_card()
                elif (userInput == 5):
                    print("\n")
                    print("Closing Card Menu...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## CHECKOUT INTERFACE SUBCLASS #################################################

class Checkout(Interface):

    def __init__(self):
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Checkout ===")
        

    def show_menu(self):
        print("1. View Cards") #good IT
        print("2. Add Credit Card") #good IT
        print("3. Modify Credit Card") #good IT
        print("4. Delete Credit Card") #good IT
        print("5. Return to Customer Menu") #good IT
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.view_cards()
                elif (userInput == 2):
                    self.custMember.add_card()
                elif (userInput == 3):
                    self.custMember.modify_card()
                elif (userInput == 4):
                    self.custMember.delete_card()
                elif (userInput == 5):
                    print("\n")
                    print("Closing Card Menu...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   


    def cart_art():
        print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")