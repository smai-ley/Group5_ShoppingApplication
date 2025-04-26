#userObject.py

from staffPackage import Staff
from customerPackage import Customer

def get_user_object(role_input):
    role = role_input.strip().upper()
    if role == "STAFF":
        return Staff()
    elif role == "CUSTOMER":
        return Customer()
    else:
        raise ValueError("Invalid input. Please type either 'STAFF' or 'CUSTOMER'.")