# Gelato Pitone

I took inspiration from the Love Sandwiches walkthrough project to create something similar but in a different setting. I decided to create a program with Python for a small ice cream truck company called "Gelato Pitone" where the different icetrucks can check the ice cream tastes available in the centralized database and receive information about the different choices available. I have created a Google spreadsheet with all the information about the different tastes.

Here is the link to the deployed Python terminal on [Heroku](xxxxxx) 

## Design process

Originally I had imagined how the different ice cream trucks could either read or insert data into the Google spreadsheet. The individual users would have been able to input how many liters of the different ice creams they have sold under one day and enable the spreadsheet to update showing how much ice cream was left in stock and return the profit for the user.

Here is a flowchart representing the original idea for my project:

![LucidApp](XXXXXXX)

Nevertheless after speaking with Luke Buchanan I realized that my project would be too similar to the walkthrough project so I decided to have a more complex datasheet where each ice cream taste would have different types of data attached to it, both integers and text.

![Spreadsheet](XXXXXX)

## Features

At the beginning of the program the user is greeted by the main menu. It features the name of the ice cream truck company and it is decorated in ASCII language. I created a simple ASCII box with ChatGPT and was then able to modify it and enhance it according to my needs.

![Picture1](XXXXXX)

The user has then the possibility of seeing which tastes are available and then chose if they want to have more information about a specific taste or go back to the main menu:

![Picture2](XXXXXXX)

Every input function in the program returns an error message if the input value is not valid. Here is the error message for inserting an ice cream taste not available in the list:

![Picture3](XXXXXX)

For each ice cream taste available the program gives the user the possibility to retreive all information present in the spreadsheet for each specific taste, containing relevant information about its ingredients, its price and the name of the supplier:

![Picture4](XXXXXX)

The program gives different lists showing three ice cream tastes according to different statistics, so that the user can always know which ice cream they can offer their customers according to their dietary needs. Here for example the program returns the three tastes with lowest amount of calories:

![Picture5](XXXXX)

Please notice that after the program returns information to the user it also enables the user to go back to the main menu or exiting the program.

![Picture6](XXXX)

### Functions

- At first I created the IceCream class with the init function in order to create the show_data method which returns all the data available to a specific ice cream taste.

- user_choice function prints the main menu to the terminal where the user can input one of the options to trigger the other functions and return data to the terminal. It also gives the option to exit the program. Please notice that the letter X has been reserved for the exit function for better user experience.

- tastes_available function creates a list from the values of the first column without the heading, which would be redundant in this case.

- taste_choice and inner_menu provide the user the possibility to input a value to move forward or exit. They both return an error message if the imput is invalid.

- read_data is called after the tastes_available function as it gives the user the possibility to input and therefore select an ice cream taste from that list. If the ice cream taste is present in the file it returns an instance of the IceCream class and returns the show_data method to the terminal. If the ice cream taste input is invalid the program will return an error message and restart the function, so that the user can input a valid value.

- low_fat, high_prot, low_carbs and low_calories use the sorted() function to 

### Discarted Functions

## Testing

## Credits

## Deployment
