#interface.py

from additionalPackage.icon import Icon
from customerPackage.customer import Customer
from orderPackage.shoppingCart import ShoppingCart
from orderPackage.order import Order
from staffPackage.staff import Staff

class Interface:
    def __init__(self):
        self.printer = Icon()
        self.show_menu()
        
    def show_menu(self):
        print("=== Menu ===")
        print("1. Staff") # FULLY COMPLETE
        print("2. Customer") 
        print("3. End Session") # FULLY COMPLETE
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    print("\nLoading Staff...\n")
                    return StaffInterface()
                elif (userInput == 2):
                    print("\nLoading Customer...\n")
                    return CustInterface(input("Enter Customer ID: "))
                elif (userInput == 3):
                    print("\nEnding Session...\n\t\tBye Bye!")
                    self.printer.cat()
                    exit()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input. Please type either '1' - Staff, '2' - Customer, '3' - End session.")        

############################################### STAFF INTERFACE SUBCLASS #################################################

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
        print("7. Log Out") #GOOD
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.staffMember.show_products()
                elif (userInput == 2):
                    self.staffMember.add_product(input("Product ID: "), float(input("Price: ")))
                elif (userInput == 3):
                    self.staffMember.modify_product(input("Product ID: "), float(input("Price: ")))
                elif (userInput == 4):
                    self.staffMember.delete_product(input("Product ID to be deleted: "))
                elif (userInput == 5):
                    self.staffMember.show_stock()
                elif (userInput == 6):
                    self.staffMember.add_stock(input("Product[Stock] ID: "), int(input("Quantity: ")), input("Warehouse ID: "))
                elif (userInput == 7):
                    print("\nEnding Staff Session...\t\n")
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

############################################### CUSTOMER INTERFACE SUBCLASS ##############################################

class CustInterface(Interface):
    def __init__(self, user_id):
        self.user_id = user_id
        self.printer = Icon()
        self.custMember = Customer(user_id) # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart(user_id)
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("========== Customer Menu ==========")

    def show_menu(self):
        print("1. ⁺˚⋆｡°✩₊ Shop Products ⁺˚⋆｡°✩₊") # GOOD
        print("2. See Detailed Product Info") # GOOD
        print("3. 🛒 Shopping Cart 🛒") # GOOD
        print("4. Checkout")
        print("5. Manage Credit Cards") # GOOD
        print("6. Manage Addresses") # GOOD
        print("7. View Balance") # GOOD 
        print("8. Log Out") # GOOD
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.show_products()
                elif (userInput == 2):
                    self.custMember.view_prodInfo(input("Look at Product ID: "))
                elif (userInput == 3):
                    return ShopCart(self.user_id)
                elif (userInput == 4):
                    self.shopCart.checkout()
                    self.cart_art()
                elif (userInput == 5):
                    return Card(self.user_id)
                elif (userInput == 6):
                    return Address(self.user_id)
                elif (userInput == 7):
                    self.custMember.view_balance(self.user_id)
                elif (userInput == 8):
                    print("\nEnding Customer Session...\n")
                    self.printer.balloon()
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input.")   
    
    def cart_art(self):
        print("\tOrder Placed!")
        print(sum(self.shopCart.items.values()))
        print(r"""⠀⠀⠀⠀ Shop Again!⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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

########################################## CARD INTERFACE SUBCLASS #################################################

class Card(CustInterface):

    def __init__(self, user_id):
        self.user_id = user_id
        self.custMember = Customer(user_id) # Customer connection to DB from Customer Class
        self.shopCart = ShoppingCart(user_id)
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Manage Cards ===")

    def show_menu(self):
        print("1. View Cards") #GOOD
        print("2. Add Credit Card") #GOOD
        print("3. Modify Credit Card") #GOOD
        print("4. Delete Credit Card") #GOOD
        print("5. Return to Customer Menu") #GOOD
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.view_cards(self.user_id)
                elif (userInput == 2):
                    self.custMember.add_card(input("Nickname for new card: "), input("New Card Numbers (Format: XXXX XXXX XXXX XXXX): "), self.user_id)
                elif (userInput == 3):
                    self.custMember.modify_card(input("Card to be Modified: "), input("New Nickname: "), input("New Card Number: "))
                elif (userInput == 4):
                    self.custMember.delete_card(input("Nickname of Card to be Removed: "))
                elif (userInput == 5):
                    print("\nClosing Card Menu...\n")
                    return CustInterface(self.user_id)
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## ADDRESS INTERFACE SUBCLASS #################################################

class Address(CustInterface):

    def __init__(self, user_id):
        self.user_id = user_id
        self.custMember = Customer(user_id) # Customer connection to DB from Customer Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n")
        print("=== Manage Addresses ===")

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
                    self.custMember.view_address(self.user_id)
                elif (userInput == 2):
                    self.custMember.add_address(input("Address ID/Nickname: "), input("New Address (Format: Street, City): "),
                                                input("Set as Delivery Address? (y/n): ").strip().lower() == 'y', 
                                                input("Set as Payment Address? (y/n): ").strip().lower() == 'y', self.user_id)
                elif (userInput == 3):
                    self.custMember.modify_address(input("Address ID/Nickname: "), input("New Address (Format: Street, City): "),
                                                   input("Set as Delivery Address? (y/n): ").strip().lower() == 'y',
                                                   input("Set as Payment Address? (y/n): ").strip().lower() == 'y', self.user_id)
                elif (userInput == 4):
                    self.custMember.delete_address(input("Address ID/Nickname: "), self.user_id)
                elif (userInput == 5):
                    print("\nClosing Address Menu...\n")
                    return CustInterface(self.user_id)
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   

########################################## SHOPPING CART INTERFACE SUBCLASS #################################################

class ShopCart(CustInterface):

    def __init__(self, user_id):
        self.user_id = user_id
        self.staffMember = Customer(user_id)
        self.shopCart = ShoppingCart(user_id)
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("\n=== Manage Shopping Cart Menu ===")

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
                userInput = int(input("SC Menu Index: "))
                if (userInput == 1):
                    self.shopCart.view_cart()
                elif (userInput == 2):
                    self.shopCart.add_item(input("Product ID: "),input("Add Quantity: "))
                elif (userInput == 3):
                    self.shopCart.remove_item(input("Remove all Product ID: "))
                elif (userInput == 4):
                    self.shopCart.change_quantity(input("Product ID: "), input("Set Quantity: "))
                elif (userInput == 5):
                    print("\nClosing Cart Menu...\n")
                    return CustInterface(self.user_id)
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   
