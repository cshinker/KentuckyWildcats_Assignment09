# File Name: database_management.py
# Student Name: Cam Shinker, Vanshika Rana
# email: shinkecj@mail.uc.edu, ranava@mail.uc.edu
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

class Database_Man():
    def connect_to_db(self):
        '''
        Connects to a database
        @return conn: The connection object
        '''
        conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'  
        'uid=IS4010Login;'
        'pwd=P@ssword2;'
        )
        return conn
    def fetch_products(self, conn):
        '''
        Makes a list of all of the products
        @param conn: The connection object
        @return products list: A list of all of the products
        '''
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

        #conn.close()
        return products

    def get_random_product(self, products):
        '''
        Chooses a random row from the list of products
        @param products list: A list to choose a random product from
        @return random.choice(products) list: The info about the randomly selected product
        '''
        return random.choice(products)

    def get_manufacturer(self, conn, manufacturerID):
        '''
        Looks up the manufacturer name from its ID
        @param conn: The connection object
        @param ManufacturerID integer: The manufacturer ID to look up
        @return cursor string: The name of the manufacturer
        '''
        cursor = conn.cursor()
        cursor.execute("SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID ="+ str(manufacturerID))
        return cursor

    def get_brand(self, conn, brandID):
        '''
        Looks up the brand name from its ID
        @param conn: The connection object
        @param brandID integer: The brand ID to look up
        @return cursor string: The name of the brand
        '''
        cursor = conn.cursor()
        cursor.execute("SELECT Brand FROM tBrand WHERE BrandID ="+ str(brandID))
        return cursor

    def get_transactions(self, conn, productID):
        '''
        Gets the number of times a specific product was sold
        @param conn: The connection object
        @param productID integer: The product ID to use in the query
        @return cursor string: The number of times a specific product was sold
        '''
        cursor = conn.cursor()
        cursor.execute(
            "SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID ="+ str(productID)+")"
            )
        return cursor
    

