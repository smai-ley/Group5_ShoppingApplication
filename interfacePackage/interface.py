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
        self.welcome()
        self.show_menu()
        self.staffMember = Staff()

    def welcome(self):
        print("=== Staff Menu ===")

    def show_menu(self):
        print("1. Add Stock and Price")
        print("2. Modify Stock and Price")
        print("3. Delete Stock and Price")
        print("4. Add Stock to Warehouse")
        print("5. End Staff Session")
        self.menu_selection()
 

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.staffMember.add_product(prodNo = input("Product ID: "), price = float(input("Product ID: ")))
                elif (userInput == 2):
                    self.staffMember.modify_product(prodNo = input("Product ID: "), price = float(input("Product ID: ")))
                elif (userInput == 3):
                    self.staffMember.delete_product(prodNo = input("Product ID: "))
                elif (userInput == 4):
                    self.staffMember.add_stock(stockID)
                elif (userInput == 5):
                    print("\n")
                    print("Ending Staff Session...")
                    print("\n")
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input.")   
                self.show_menu()

########################################## CUSTOMER INTERFACE SUBCLASS #################################################

class CustInterface(Interface):
    def __init__(self):
        self.welcome()
        self.show_menu()
        self.custMember = Customer() # Customer connection to DB from Customer Class

    def welcome(self):
        print("=== Customer Menu ===")

    def show_menu(self):
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Manage Payment Cards")
        print("6. Manage Addresses")
        print("7. Logout")
        self.menu_selection()

    def menu_selection(self):
        while True:
            try:
                userInput = int(input("Menu Index: "))
                if (userInput == 1):
                    self.custMember.browse_products()
                elif (userInput == 2):
                    print("2")
                elif (userInput == 3):
                    print("3")
                elif (userInput == 4):
                    print("4")
                elif (userInput == 5):
                    print("5")
                elif (userInput == 6):
                    print("6")
                elif (userInput == 7):
                    print("\n")
                    print("Ending Customer Session...")
                    print("\n")
                    return Interface()
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input.")   