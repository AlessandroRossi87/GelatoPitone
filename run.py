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

taste = SHEET.worksheet("taste").col_values(0)
ingredients = SHEET.worksheet("ingredients").col_values(1)
vegan = SHEET.worksheet("vegan").col_values(2)
price = SHEET.worksheet("price").col_values(3)
retail_price = SHEET.worksheet("retail_price").col_values(4)

data = sheet.get_all_values()


def read_or_insert_data(): # I wrote this
    """
    Asks user if they wish to read or insert data.
    They can insert sold data or read any data.
    """
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


def read_data(self):
    """"
    Creating new fuction to read model data
    """
    print(f"taste = {self.taste}\n")
    print(f"ingredients = {self.ingredients}\n")
    print(f"vegan = {self.vegan}\n")
    print(f"price = {self.price}\n")
    print(f"retail-price = {self.retail-price}\n")


# def read_data(): # I wrote this looking at https://docs.gspread.org/
    """
    Asks for which data to be read and returns it
    """
    choose_data = input("Choose K (Stock) S (Sold) P (Price) or R (Revenue)\n")
    if choose_data == "K":
        worksheet = SHEET.worksheet("stock")

        print("The latest Stock data is:")
        stock_data = worksheet.get_all_values()
        stock_data = stock_data[-1]
        for stock_row in stock_data:
            print(stock_row)

    # elif choose_data == "S":
        worksheet = SHEET.worksheet("sold")

        print("The latest Sold data is:")
        sold_data = worksheet.get_all_values()
        sold_data = sold_data[-1]
        for sold_row in sold_data:
            print(sold_row)

    # elif choose_data == "P":
        worksheet = SHEET.worksheet("price")

        print("The latest Price is:")
        price_data = worksheet.get_all_values()
        price_data = price_data[-1]
        for price_row in price_data:
            print(price_row)

    # elif choose_data == "R":
        worksheet = SHEET.worksheet("revenue")

        print("The latest Revenue is:")
        revenue_data = worksheet.get_all_values()
        revenue_data = revenue_data[-1]
        for revenue_row in revenue_data:
           # print(revenue_row)


# def calculate_stock_data()
    """
    Calculates stock data from inserted sold data
    """
#   returns = new_stock

# def calculate_revenue()
    """
    Calculate today's revenue from sold data
    """
#     returns = new_revenue


def main():
    """
    Run all program functions
    """
    read_or_insert_data()
    data = read_data()
#    sold_data = [int(num) for num in "sold"]
    stock_data = [num for num in "stock"]


print("Welcome to Gelato Pitone")
main()
