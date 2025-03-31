# File Name: main.py
# Student Name: Cam Shinker, Vanshika Rana
# email: shinkecj@mail.uc.edu, ranava@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to a database and complete some tasks

# Brief Description of what this module does: Contains the code that completes the assignment
# Citations: 

# Anything else that's relevant:
import pyodbc
from database_package.database_management import *


def main():
    '''
    Executes the assignment code
    '''
    db = Database_Man()
    conn = db.connect_to_db()
    products = db.fetch_products(conn)
   

    selected = db.get_random_product(products)


    description = selected.description
    product_id = selected.product_id
    manufacturer_id = selected.manufacturer_id
    brand_id = selected.brand_id

    cursor = db.get_manufacturer(conn, manufacturer_id)
    manufacturer = cursor.fetchall()[0]
    manufacturer = manufacturer[0]
    
    cursor = db.get_brand(conn, brand_id)
    brand = cursor.fetchall()[0]
    brand = brand[0]

    cursor = db.get_transactions(conn, product_id)
    transactions = cursor.fetchall()[0]
    transactions = transactions[0]

    print("The product", description, "was produced by", manufacturer, "in the brand", brand+". This product was sold", transactions, "times.")
    # Some products don't have descriptions, so the sentence won't be correct for certain products.
if __name__ == "__main__":
    main()


