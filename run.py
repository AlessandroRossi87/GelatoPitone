import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("icecream_sheet")

stock = SHEET.worksheet("stock")
sold = SHEET.worksheet("stold")
price = SHEET.worksheet("price")
revenue = SHEET.worksheet("revenue")

data = stock.get_all_values()


def read_or_insert_data():
    """
    Asks user if they wish to read or insert data.
    They can insert sold data or read any data.
    """
    print("Do you wish to read or inser data?")
    read_or_insert = input("Enter R for Read or I for insert:\n")
    if read_or_insert == "R":
        read_data
    elif read_or_insert == "I":
        print("Insert Sold data")
        insert_data
    else print("Invaid data")

def read_data():
    """
    Asks for which data to be read and returns it
    """
    print("Enter K for Stock, S for Sold, P for Price or R for Revenue\n")

def insert_data()
    """
    Allows user to insert Sold data to calculate stock
    """

def calculate_stock_data()
    """
    Calculates stock data from inserted sold data
    """
    returns = new_stock

def calculate_revenue()
    """
    Calculate today's revenue from sold data
    """
    returns = new_revenue


def main()
    """
    Run all program functions
    """