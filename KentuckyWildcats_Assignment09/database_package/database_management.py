# File Name: database_management.py
# Student Name: Cam Shinker, Vanshika Rana
# email: shinkecj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to a database and complete some tasks

# Brief Description of what this module does: Contains classes that complete the assignment
# Citations: 

# Anything else that's relevant:

import pyodbc
import random


class Product:
    def __init__(self, product_id, upc, description, manufacturer_id, brand_id):
        self.product_id = product_id
        self.upc = upc
        self.description = description.strip()
        self.manufacturer_id = manufacturer_id
        self.brand_id = brand_id

    def describe(self):
        return (
            f"The product '{self.description}' (Product ID {self.product_id}) is manufactured "
            f"by company {self.manufacturer_id} and branded under brand {self.brand_id}."
        )


def fetch_products():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'  
        'uid=IS4010Login;'
        'pwd=P@ssword2;'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")

    products = []

    for row in cursor.fetchall():
        product = Product(
            product_id=row.ProductID,
            upc=row[1],
            description=row.Description,
            manufacturer_id=row.ManufacturerID,
            brand_id=row.BrandID
        )
        products.append(product)

    conn.close()
    return products

def get_random_product(products):
    return random.choice(products)

