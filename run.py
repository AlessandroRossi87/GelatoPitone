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

icecreams = SHEET.worksheet("icecreams").get_all_values()

ingredients = SHEET.worksheet("icecreams").col_values(1)
vegan = SHEET.worksheet("icecreams").col_values(2)
price = SHEET.worksheet("icecreams").col_values(3)
retail_price = SHEET.worksheet("icecreams").col_values(4)
fat = SHEET.worksheet("icecreams").col_values(5)
carbs = SHEET.worksheet("icecreams").col_values(6)
protein = SHEET.worksheet("icecreams").col_values(7)
calories = SHEET.worksheet("icecreams").col_values(8)
calories = SHEET.worksheet("icecreams").col_values(9)


class Icecream:
    """
    Class for icecream from the worksheet
    """
    global icecreams

    def __init__(self, icecream_taste):
        for icecream in icecreams:
            if icecream_taste == icecream[0]:
                self.ingredients == icecream[1]
                self.vegan == icecream[2]
                self.price == icecream[3]
                self.retail_price == icecream[4]
                self.fat == icecream[5]
                self.carbs == icecream[6]
                self.protein == icecream[7]
                self.calories == icecream[8]
                self.supplier == icecream[9]

    def show_data(self):
        """"
        Creating new fuction to read model data
        """
        print(f"Taste = {self.taste}\n")
        print(f"Ingredients = {self.ingredients}\n")
        print(f"Vegan = {self.vegan}\n")
        print(f"Price = {self.price}\n")
        print(f"Retail Price = {self.retail_price}\n")
        print(f"Fat = {self.fat}\n")
        print(f"Carbs = {self.carbs}\n")
        print(f"Crotein = {self.protein}\n")
        print(f"Calories = {self.calories}\n")
        print(f"Supplier = {self.supplier}\n")


def read_data():
    """
    XXX
    """
    icecream_taste = input("Please enter an icecream taste (ex. Chocolate): \n")

    if(icecream_taste in SHEET.worksheet("icecreams").col_values(0)):
        my_icecream = Icecream(my_icecream)
        my_icecream.display_information()
    else:
        print("Icecream not found")


def validate_data(values):     # From Love Sandwiches walkthrough project
    """
    Validates the date insert
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"You provided {len(values)} instead of 5 values required"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, try again.\n")
        return False

    return True


def insert_data(data, worksheet):   # From Love Sandwiches walkthrough project
    """
    Allows user to insert Sold data to calculate stock
    """
    print("Updating Sold worksheet...\n")
    insert_data = SHEET.worksheet("sold")
    insert_data.append_row(data)
    print("Sold data updated successfully!")

def read_or_insert_data(): # I wrote this
    """
    Asks user if they wish to read or insert data.
    They can insert sold data or read any data.
    """
    print("Welcome to Gelato Pitone")
    print("Do you wish to read or inser data?")
    read_or_insert = input("Enter R for Read or I for Insert:\n")
    if read_or_insert == "R":
        read_data
    elif read_or_insert == "I":
        insert_data = input("Insert Sold data:\n")

        sold_data = insert_data.split(",")
        if validate_data(sold_data):
            print("Data is valid!")
        insert_data

read_or_insert_data()