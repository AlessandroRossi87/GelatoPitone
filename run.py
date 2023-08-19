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

taste = SHEET.worksheet("icecreams").col_values(1)
ingredients = SHEET.worksheet("icecreams").col_values(2)
vegan = SHEET.worksheet("icecreams").col_values(3)
price = SHEET.worksheet("icecreams").col_values(4)
retail_price = SHEET.worksheet("icecreams").col_values(5)
fat = SHEET.worksheet("icecreams").col_values(6)
carbs = SHEET.worksheet("icecreams").col_values(7)
protein = SHEET.worksheet("icecreams").col_values(8)
calories = SHEET.worksheet("icecreams").col_values(9)
supplier = SHEET.worksheet("icecreams").col_values(10)


class IceCream:  # DOES IT WORK?
    """
    Class for icecream from the worksheet
    """
    global icecreams

    def __init__(self, icecream_taste):
        for icecream in icecreams:
            if icecream_taste == icecream[0]:
                self.taste = icecream[0]
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
        Gives the user all data about a specific ste
        """
        print("*******************************\n")
        print(f"You selected <<{self.taste}>>\n")
        print("*******************************\n")
        print(f"Ingredients are {self.ingredients}\n")
        print(f"Is it vegan? {self.vegan}\n")
        print(f"The price is {self.price} EUR\n")
        print(f"The retail price is {self.retail_price} EUR\n")
        print(f"There are {self.fat} grams of fat per Kilo\n")
        print(f"There are {self.carbs} grams of carbs per Kilo\n")
        print(f"There are {self.protein} grams of proteins per Kilo\n")
        print(f"There are {self.calories} calories per 100g\n")
        print(f"Producer is {self.supplier}\n")
        taste_choice()


def tastes_available():  # WORKS
    """
    Displays the tastes available and gives choice
    to get more info for specific taste
    """
    print("The tastes available are: \n")
    icecream_taste = [item for item in SHEET.worksheet("icecreams").col_values(1) if item]
    icecream_taste.pop(0)  # takes away header from list
    for item in icecream_taste:
        print(item)
    
    taste_choice()
        

def taste_choice():   # WORKS
    """
    Makes the user decide if they want more info
    about tastes or if they wish to go back to 
    menu
    """
    info_or_menu = input("Type I for info about tastes or M for Menu: \n")
    info_or_menu = info_or_menu.lower()   
    if info_or_menu == "i":
        read_data()
    elif info_or_menu == "m":
        user_choice()
    else:
        print("Wrong selection!")
        tastes_available()


def read_data():  # DOES NOT WORK
    """
    Gives the user all the info availabl
    about a specific icecream taste
    """
    icecream_taste = input("Please enter icecream taste: \n")

    if (icecream_taste in SHEET.worksheet("icecreams").col_values(1)):
        my_icecream = IceCream(icecream_taste)
        my_icecream.show_data()
    else:
        print("Icecream not found")


def inner_menu():   # WORKS
    """
    Gives user possibility to have more info
    about specific taste or go back to main menu
    """
    info_or_menu = input("Type taste for more info, M for menu or X for Exit: \n")
    info_or_menu = info_or_menu.lower()
    if (info_or_menu in SHEET.worksheet("icecreams").col_values(1)):
        my_icecream = IceCream(info_or_menu)
        my_icecream.show_data()
    elif info_or_menu == "m":
        user_choice()
    elif info_or_menu == "x":
        exit_pitone()
    else:
        print("Error message! Choose Taste, M for Menu or X for Exit")
        inner_menu()


def low_fat():  # WORKS
    """
    Gives the user the 3 ice cream tastes
    with the least amount of fat
    """
    sorted_fat = sorted(icecreams[1:], key=lambda x: float(x[5]) if x[5] else 0.0)

    print("Icecream tastes with lowest fat are: \n")
    for icecream in sorted_fat[:3]:
        print(icecream[0])
        
    inner_menu()


def high_prot():  # DOES NOT WORK
    """
    Gives the user the 3 ice cream tastes
    with the highest amout of protein
    """
    sorted_prot = sorted(icecreams[1:], key=lambda x: float(x[7]) if x[7] else 0.0)  #Reverse in order to show highest values

    print("Icecream tastes with highest proteins are:\n")
    for icecream in sorted_prot[:3]:
        print(icecream[0])

    inner_menu()


def low_carbs():   # WORKS
    """
    Gives the user the 3 ice cream tastes
    with the least amount of carbs
    """
    sorted_carb = sorted(icecreams[1:], key=lambda x: float(x[6]) if x[6] else 0.0)

    print("Icecream tastes with lowest carbs are: \n")
    for icecream in sorted_carb[:3]:
        print(icecream[0])

    inner_menu()


def low_calories():  # WORKS
    """
    Gives the user the 3 ice cream tastes
    with the least amout of calories
    """
    sorted_calories = sorted(icecreams[1:], key=lambda x: float(x[8]) if x[8] else 0.0)

    print("Icecream tastes with lowest calories are: \n")
    for icecream in sorted_calories[:3]:
        print(icecream[0])

    inner_menu()  


def most_profit():   # DOES NOT WORK
    """
    Gives the user the 3 ice cream tastes
    that are most profitable
    """
    icecream_profit = retail_price - price
    sorted_profit = sorted(icecream_profit[1:])

    print("Icecream tastes with highest profit are: \n")
    for icecream in sorted_profit[:3]:
        print(icecream_profit[0])

    inner_menu()


def exit_pitone():   # WORKS
    """
    Gives the user the option to exit program or
    start again with main menu
    """
    exit_or_menu = input("Do you wish to exit? Y or N: \n")
    exit_or_menu = exit_or_menu.lower()
    if exit_or_menu == "y":
        exit()
    elif exit_or_menu == "n":
        user_choice()
    else:
        print("Error message! Choose Y or N:")
        exit_pitone()


def user_choice():   # I wrote this WORKS
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
    print("║    E: Low calories         ║")
    print("║    F: Most profitable      ║")
    print("║    X: Exit                 ║")
    print("╚════════════════════════════╝")
    select_menu = input(" \n")
    select_menu = select_menu.lower()
    if select_menu == "a":
        tastes_available()
    elif select_menu == "b":
        low_fat()
    elif select_menu == "c":
        high_prot()
    elif select_menu == "d":
        low_carbs()
    elif select_menu == "e":
        low_calories()
    elif select_menu == "f":
        most_profit()
    elif select_menu == "x":
        exit_pitone()
    else:
        print("Error message! Chose A, B, C, D, E or F")
        user_choice()


user_choice()