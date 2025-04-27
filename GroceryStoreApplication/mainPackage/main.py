# main.py

from customerPackage import Customer
from staffPackage import Staff
from userPackage import User, userObject

if __name__ == "__main__":
    print(" | Welcome to CS4092-001 Group 5's Online Shopping Application |\n | Please select by typing 'STAFF' or 'CUSTOMER' for browsing, |\n |          End session by typing 'END' at any time.           |")
    
    user_input = input("Enter your role (STAFF or CUSTOMER): ")
    #user = get_user_object(user_input)

    # needs menu cli implementation, classes are built, customer may need additional 
    # attention with multivalued attributes, reference relational schema for table names & attributes