#interface.py

from customerPackage.customer import Customer
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
        print("1. View Products")
        print("2. Add Products and Price")
        print("3. Modify Products and Price")
        print("4. Delete Products and Price")
        print("5. View Stock")
        print("6. Add Stock to Warehouse")
        print("7. End Staff Session")
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
                    prodNo = input("Product[Stock] ID: ")
                    self.staffMember.add_stock(prodNo)
                elif (userInput == 6):
                    self.staffMember.show_products()
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
        self.custMember = Customer() # Customer connection to DB from Customer Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Customer Menu ===")

    def show_menu(self):
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Manage Credit Cards")
        print("6. Manage Addresses")
        print("7. View Balance")
        print("8. Logout")
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.show_products()
                elif (userInput == 2):
                    print("2")
                elif (userInput == 3):
                    print("3")
                elif (userInput == 4):
                    print("4")
                elif (userInput == 5):
                    return Card()
                elif (userInput == 6):
                    return Address()
                elif (userInput == 7):
                    print("7")
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

class Card(Interface):

    def __init__(self):
        #self.staffMember = Customer() # Staff connection to DB from Staff Class
        self.welcome()
        self.show_menu()

    def welcome(self):
        print("=== Manage Cards Menu ===")

    def show_menu(self):
        print("1. View Cards")
        print("2. Add Credit Card")
        print("3. Modify Credit Card")
        print("4. Delete Credit Card")
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
                    print("Ending Staff Session...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   


class Address(Interface):

    def __init__(self):
        #self.staffMember = Customer() # Staff connection to DB from Staff Class
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
                    print("Ending Staff Session...")
                    print("\n")
                    return CustInterface()
                else:
                    print("Invalid input.")
            except ValueError:
                    print("Invalid input or missing numbers.")   