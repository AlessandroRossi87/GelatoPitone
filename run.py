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
supplier = SHEET.worksheet("icecreams").col_values(9)


class Icecream:
    """
    Class for icecream from the worksheet
    """
    global icecreams

    def __init__(self, icecream_taste):
        for icecream in icecreams:
            if icecream_taste == icecream[0]:
                self.ingredients = icecream[1]
                self.vegan = icecream[2]
                self.price = icecream[3]
                self.retail_price = icecream[4]
                self.fat = icecream[5]
                self.carbs = icecream[6]
                self.protein = icecream[7]
                self.calories = icecream[8]
                self.supplier = icecream[9]

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


def tastes_available():
    """
    Displays the tastes available and gives choice
    to get more info for specific taste
    """
    print("The tastes available are:\n")
    icecream_taste = [item for item in SHEET.worksheet("icecreams").col_values(1) if item]
    for item in icecream_taste:
        print(item)
    
    taste_choice()
        

def taste_choice():
    """
    Makes the user decide if they want more info
    about tastes or if they wish to go back to 
    menu
    """
    info_or_menu = input("Type I for info about tastes or X for Menu: \n")    
    if info_or_menu == "I":
        read_data()
    elif info_or_menu == "X":
        select_menu()
    else:
        print("Wrong selection!")
        info_or_menu()


def read_data():
    """
    Gives the user all the info available
    about a specific icecream taste
    """
    icecream_taste = input("Please enter icecream taste: \n")

    if (icecream_taste in SHEET.worksheet("icecreams").col_values(0)):
        my_icecream = Icecream(icecream_taste)
        my_icecream.show_data(self)
    else:
        print("Icecream not found")


# def low_fat()
    """
    Gives the user the 3 ice cream tastes
    with the least amount of fat
    """


# def high_prot()
    """
    Gives the user the 3 ice cream tastes
    with the highest amout of protein
    """

# def low_carbs()
    """
    Gives the user the 3 ice cream tastes
    with the least amount of carbs
    """


# def most_profit()
    """
    Gives the user the 3 ice cream tastes
    that are most profitable
    """


# def exit_pitone()


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


def select_menu():   # I wrote this
    """
    Asks user if they wish to read or insert data.
    They can insert sold data or read any data.
    """

    print("╔════════════════════════════╗")
    print("║  <===GELATO===PITONE===:>- ║")
    print("╠════════════════════════════╣")
    print("║     Select your choice     ║")
    print("║                            ║")
    print("║    A: Tastes available     ║")
    print("║    B: Low fat              ║")
    print("║    C: High protein         ║")
    print("║    D: Low carbs            ║")
    print("║    E: Most profitable      ║")
    print("║    F: Exit                 ║")
    print("╚════════════════════════════╝")
    select_menu = input(" \n")
    if select_menu == "A":
        tastes_available()
    elif select_menu == "B":
        low_fat()
    elif select_menu == "C":
        high_prot()
    elif select_menu == "D":
        low_carbs()
    elif select_menu == "E":
        most_profit()
    elif select_menu == "F":
        exit_pitone()
    else:
        print("Error message! Chose A, B, C, D, E or F")
        select_menu()


select_menu()
