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

taste = SHEET.worksheet("icecreams").col_values(1)    # col_values start with 1 not 0
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
        Gives the user all information about a specific taste
        """
        print("*******************************\n")
        print(f"You selected <<{self.taste}>>\n")
        print("*******************************\n")
        print(f"It contains {self.ingredients}\n")
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
    to get more info about specific taste
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
        print("xxxxxxxxxxxxxxxxx")
        print("Wrong selection!")
        print("xxxxxxxxxxxxxxxxx\n")
        taste_choice()


def read_data():  # WORKS
    """
    Gives the user all the info available
    about a specific icecream taste
    """
    icecream_taste = input("Please enter icecream taste: \n")

    if (icecream_taste in SHEET.worksheet("icecreams").col_values(1)):
        my_icecream = IceCream(icecream_taste)
        my_icecream.show_data()
    else:
        print("xxxxxxxxxxxxxxxxxxxx")
        print("Icecream not found")
        print("xxxxxxxxxxxxxxxxxxxx\n")

    read_data()


def inner_menu():   # WORKS
    """
    Gives user possibility to have more info
    about specific taste or go back to main menu
    """
    info_or_menu = input("Type T for tastes, M for menu or X for Exit: \n")
    info_or_menu = info_or_menu.lower()
    if info_or_menu == "t":
        read_data()
    elif info_or_menu == "m":
        user_choice()
    elif info_or_menu == "x":
        exit_pitone()
    else:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Error message! Choose Taste, M for Menu or X for Exit")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
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


def high_prot():   # WORKS
    """
    Gives the user the 3 ice cream tastes
    with the highest amout of protein
    """
    sorted_prot = sorted(icecreams[1:], key=lambda x: float(x[7]) if x[7] else 0.0, reverse=True)    # Reverse in order to show highest values

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


def icecream_nuts():    #WORKS
    """
    Gives the user with a list
    of tastes containing nuts or
    without nuts
    """
    nuts_or_not = input("Press N for list with nuts or W for without nuts \n")
    nuts_or_not = nuts_or_not.lower()
    if nuts_or_not == "n":
        contains_nuts = [icecream[0] for icecream in icecreams[1:] if icecream[1].lower() == "nuts"]
        if contains_nuts:
            print("The following tastes contain nuts:")
            for icecream in contains_nuts:
                print(icecream)
        else:
            print("No taste contain nuts")

    elif nuts_or_not == "w":
        without_nuts = [icecream[0] for icecream in icecreams[1:] if icecream[1].lower() != "nuts"]
        if without_nuts:
            print("The following tastes do not contain nuts:")
            for icecream in without_nuts:
                print(icecream)
        else:
            print("All tastes contain nuts")
    else:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Error message! Choose N or W")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        icecream_nuts()

    inner_menu()


def vegan_icecream():  #WORKS
    """
    Provides the user with list
    of vegan tastes
    """
    vegan_tastes = [icecream[0] for icecream in icecreams[1:] if icecream[2].lower() == "yes"]

    if vegan_tastes:
        print("The vegan tastes are:")
        for icecream in vegan_tastes:
            print(icecream)
    else:
        print("No vegan tastes available")

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
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Error message! Choose Y or N:")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        exit_pitone()


def user_choice():   # I wrote this WORKS
    """
    This is the main menu, it gives the user
    the possibility to read different lists
    """
    print("╔════════════════════════════╗")
    print("║   G E L A T O              ║")
    print("║  <=====================:>- ║")
    print("║              P I T O N E   ║")
    print("║////////////////////////////║")
    print("║                            ║")
    print("║     Select your choice:    ║")
    print("║                            ║")
    print("║    A: Tastes available     ║")
    print("║    B: Low fat              ║")
    print("║    C: High protein         ║")
    print("║    D: Low carbs            ║")
    print("║    E: Low calories         ║")
    print("║    F: Contain nuts         ║")
    print("║    G: Vegan options        ║")
    print("║    X: -> Exit ->           ║")
    print("║                            ║")
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
        icecream_nuts()
    elif select_menu == "g":
        vegan_icecream()
    elif select_menu == "x":
        exit_pitone()
    else:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Error message! Chose A, B, C, D, E or F")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        user_choice()


user_choice()    # This function starts the user iteraction 