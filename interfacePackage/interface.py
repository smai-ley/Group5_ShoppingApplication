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
                    cust_id = input("Enter Customer ID: ")
                    print("Loading Customer...")
                    print("\n")
                    return CustInterface(cust_id)
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
        print("\n")
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
    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.custMember = Customer(cust_id) # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Customer Menu ===")

    def show_menu(self):
        print("1. View Products") # GOOD
        print("2. View Single Product Details") 
        print("3. View Cart Menu")
        print("4. Checkout")
        print("5. Manage Credit Cards") #good
        print("6. Manage Addresses") #good
        print("7. View Balance") #good 
        print("8. Logout") #good
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.show_products()
                elif (userInput == 2):
                    prodNo = input("Show details for Product ID: ")
                    self.custMember.view_prodInfo(prodNo)
                elif (userInput == 3):
                    return ShopCart(self.cust_id)
                elif (userInput == 4):
                    return Checkout(self.cust_id)
                elif (userInput == 5):
                    return Card(self.cust_id)
                elif (userInput == 6):
                    return Address(self.cust_id)
                elif (userInput == 7):
                    self.custMember.view_balance()
                elif (userInput == 8):
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

    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.custMember = Customer(cust_id) # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Manage Cards Menu ===")

    def show_menu(self):
        print("1. View Cards") #GOOD
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
                    card_name = input("Nickname for new card: ")
                    card_number = input("New Card Numbers: ")
                    self.custMember.add_card(card_name, card_number, self.cust_id)
                elif (userInput == 3):
                    card_name = input("New Nickname for card: ")
                    card_number = input("New Card Numbers: ")
                    self.custMember.modify_card(card_name, card_number)
                elif (userInput == 4):
                    card_name = input("Nickname of Card to be Removed: ")
                    self.custMember.delete_card(card_name)
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

class Address(CustInterface):

    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.staffMember = Customer(cust_id) # Staff connection to DB from Staff Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
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
                    self.custMember.view_address() ######################### DNE yet
                elif (userInput == 2):
                    self.custMember.add_address()
                elif (userInput == 3):
                    self.custMember.modify_address()
                elif (userInput == 4):
                    self.custMember.delete_address()
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

class ShopCart(CustInterface):

    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.staffMember = Customer(cust_id)
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Manage Shopping Cart Menu ===")

    def show_menu(self):
        print("1. View Cart") #good IT
        print("2. Add Product") #good IT
        print("3. Remove Product") #good IT
        print("4. Change Product Quantity") #good IT
        print("5. Return to Customer Menu") #good IT
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.shopCart.view_cart()
                elif (userInput == 2):
                    prodNo = input("Product ID: ")
                    qty = input("Quantity: ")
                    self.shopCart.add_item(prodNo,qty)
                elif (userInput == 3):
                    prodNo = input("Product ID: ")
                    self.shopCart.remove_item(prodNo)
                elif (userInput == 4):
                    prodNo = input("Product ID: ")
                    qty = input("Quantity: ")
                    self.shopCart.change_quantity(prodNo, qty)
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

    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.shopCart = ShoppingCart()
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Checkout Menu ===")
        self.shopCart.view_cart()
        
    def show_menu(self):
        print("1. Change Delivery Type") 
        print("2. Set Credit Card") 
        print("3. Place Order")
        print("4. Return to Customer Menu") #good IT
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
                    self.shopCart.checkout()
                    self.cart_art()
                elif (userInput == 4):
                    print("\n")
                    print("Closing Checkout Menu...")
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