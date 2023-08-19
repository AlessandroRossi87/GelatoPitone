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


class IceCream:
    """
    Class for icecream from the worksheet
    """
    global icecreams

    def __init__(self, icecream_taste):
        for icecream in icecreams:
            if icecream_taste == icecreams[0]:
                self.ingredients = icecreams[1]
                self.vegan = icecreams[2]
                self.price = icecreams[3]
                self.retail_price = icecreams[4]
                self.fat = icecreams[5]
                self.carbs = icecreams[6]
                self.protein = icecreams[7]
                self.calories = icecreams[8]
                self.supplier = icecreams[9]

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
    icecream_taste.pop(0)  # takes away header from list
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
        user_choice()
    else:
        print("Wrong selection!")
        tastes_available()


def read_data():
    """
    Gives the user all the info availabl
    about a specific icecream taste
    """
    icecream_taste = input("Please enter icecream taste: \n")

    if (icecream_taste in SHEET.worksheet("icecreams").col_values(0)):
        my_icecream = Icecream(icecream_taste)
        my_icecream.show_data()
    else:
        print("Icecream not found")


def low_fat():
    """
    Gives the user the 3 ice cream tastes
    with the least amount of fat
    """
    sorted_low = sorted(icecreams[1:], key=lambda x: float(x[5]) if x[5] else 0.0)

    print("Icecream tastes with lowest fat are:\n")
    for icecream in sorted_low[:3]:
        print(icecream[0])


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


def user_choice():   # I wrote this
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
    if select_menu == "a":
        tastes_available()
    elif select_menu == "b":
        low_fat()
    elif select_menu == "c":
        high_prot()
    elif select_menu == "d":
        low_carbs()
    elif select_menu == "e":
        most_profit()
    elif select_menu == "f":
        exit_pitone()
    else:
        print("Error message! Chose A, B, C, D, E or F")
        select_menu()


user_choice()
