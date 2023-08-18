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
       # revenue_data = revenue_data[-1]
       # for revenue_row in revenue_data:
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


    def insert_data(data, worksheet):   # From Love Sandwiches walkthrough project
    """
    Allows user to insert Sold data to calculate stock
    """
    print("Updating Sold worksheet...\n")
    insert_data = SHEET.worksheet("sold")
    insert_data.append_row(data)
    print("Sold data updated successfully!")


           # icecreams = SHEET.worksheet("icecreams")
       # icecream_taste = self.taste
        #for icecream_taste in icecreams(len(first_column)):
         #   print(first_column[0].value)
        

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