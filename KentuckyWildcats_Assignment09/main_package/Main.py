# File Name: main.py
# Student Name: Cam Shinker
# email: shinkecj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to a database and complete some tasks

# Brief Description of what this module does: Contains the code that completes the assignment
# Citations: 

# Anything else that's relevant:

from database_package import database_management

def main():
    products = database_management.fetch_products()
    print(f"Retrieved {len(products)} products.")

    selected = database_management.get_random_product(products)


    description = selected.description
    product_id = selected.product_id
    manufacturer_id = selected.manufacturer_id
    brand_id = selected.brand_id

    print(selected.describe())

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()


