# Gelato Pitone

I took inspiration from the Love Sandwiches walkthrough project to create something similar but in a different setting. I found the connection to the spreadsheet fascinating, as I have extensive experience with big data sets. I decided to create a program with Python for a small fictive ice cream truck company called "Gelato Pitone" where the different icetrucks can check the ice cream tastes available in the central warehouse and receive information about the different choice of tastes available. I have created a Google spreadsheet with all the information about the different tastes.

Here is the link to the deployed Python terminal on [Heroku](https://gelato-pitone-8a25ccdd7e11.herokuapp.com/) 

## Design process

Originally I had imagined how the different users could either read or insert data into the Google spreadsheet. The users would have been able to input how many liters of the different ice creams they have sold under one day and enable the spreadsheet to update showing how much ice cream was left in stock and return the profit for the user.

Here is a flowchart representing the original idea for my project:

![LucidApp](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/flowchart.png)

Nevertheless after speaking with Luke Buchanan I realized that my project would be too similar to the walkthrough project so I decided to have a more complex datasheet where each ice cream taste would have different types of data attached to it, both integers and text.

Here is a simplified flowchart representing how the project evolved:

![LucidApp](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/newflowchart.png)

## The data set from the spreadsheet

![Spreadsheet](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/spreadsheet.png)

## Features

At the beginning of the program the user is greeted by the main menu. It features the name of the ice cream truck company and it is decorated in ASCII language. I created a simple ASCII box with ChatGPT and was then able to modify it and enhance it according to my needs.

![Picture1](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/1mainmenu.png)

The user has then the possibility of seeing which tastes are available and then chose if they want to have more information about a specific taste or go back to the main menu:

![Picture2](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/2tastes.png)

Every input function in the program returns an error message if the input value is not valid. Here is the error message for inserting an ice cream taste not available in the list:

![Picture3](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/3error.png)

For each ice cream taste available the program gives the user the possibility to retreive all information present in the spreadsheet for each specific taste, containing relevant information about its ingredients, its price and the name of the supplier:

![Picture4](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/4tasteinfo.png)

The program gives different lists showing three ice cream tastes according to different statistics, so that the user can always know which ice cream they can offer their customers according to their dietary needs. Here for example the program returns the three tastes with lowest amount of calories:

![Picture5](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/5selection.png)

Please notice that after the program returns information to the user it also enables the user to go back to the main menu or exiting the program.

![Picture6](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/6exit.png)

### Functions

- At first I created the IceCream class with the init function in order to create the show_data method which returns all the data available to a specific ice cream taste.

- user_choice function prints the main menu to the terminal where the user can input one of the options to trigger the other functions and return data to the terminal. It also gives the option to exit the program. Please notice that the letter X has been reserved for the exit function for better user experience.

- tastes_available function creates a list from the values of the first column without the heading, which would be redundant in this case. It returns all the tastes available in the spreadsheet, so if the user wants to know more about a specific taste, they already know the options available.

- taste_choice and inner_menu provide the user the possibility to input a value to move forward or exit. They both return an error message if the imput is invalid.

- read_data is called after the tastes_available function as it gives the user the possibility to input and therefore select an ice cream taste from that list. If the ice cream taste is present in the file it returns an instance of the IceCream class and returns the show_data method to the terminal. If the ice cream taste input is invalid the program will return an error message and restart the function, so that the user can input a valid value.

- low_fat, high_prot, low_carbs and low_calories use the sorted() function using lambda as a key to sort the values in ascending order and creates a float with the values from the respective column in the worksheet. The functions then print the three values relevant to the paramenters the user has requested (lowest or highest). The reverse=True argument was used for reversing the sorting order in the high_prot function.

- icecream_nuts and vegan_icecream functions create a list comprehension which checks if the value of their respective column in the spreadsheet is either "nuts" or "yes" respectively. The if statements then return to the user a list of tastes in accordance to the parameters in the list comprehension when the condition is met.

- exit_pitone asks the user if they are sure to exit the program. The function provides two options for input, one to exit and one to go back to the main menu. The function returns an error message if the input is invalid.

### Discarted Functions

- During the coding process for this project I wanted to create a function which would calculate the revenue for each ice cream. That would have been possible if I created two lists where the program would subtract price from the retail price and give the revenue. It then would have returned to the terminal the three ice cream tastes with highest revenue. After many failed attempts to construct this function I had to discart this idea for time constrigement issues. I would love to work further in that to learn more about the possibilities that Python gives.

## Testing

### PEP8 Validator Testing

- The PEP 8 validator testing showed only warning messages that some of the code lines are longer than 80 characters. Since none of the print statements are longer than 80 characters I ignored these warnings as they were irrelevant for the functionality of the deployed version.

![Validator](XXXXXXXXX)

### Known Bugs

At the moment of deployment there were no known bugs. The deployed website was tested on Google Chrome and Safari.

### Fixed Bugs

- One major bug during my coding was that .col_values method uses a 1 based index instead of 0. Once I was reminded of that I was able to make my model work perfectly.

![col_values](https://github.com/AlessandroRossi87/GelatoPitone/blob/main/assets/colvalues.png)

- I also had troubles with the high_prot function because the terminal was always returning the three tastes with the least amount. I then discovered the reverse=true argument to reverse sorting order.

### User Experience

All users who tested the deployed website on Heroku found the website easy to navigate and logically organized. One user had wished for more decorative graphic features in the terminal but I decided to focus on the back end of the site.

## Deployment

- First I created a list of dependencies for deployment in Heroku by updating the requirements.txt file with the command: Pip3 freeze > requirements.txt
- After creating my Heroku account and getting the Student Pack I was able to create a new app there to deploy my project.
- In the new app on Heroku I added environment variables for Heroku to access the creds.json file and PORT.
- I then added the Python and node.js buildpacks and added them to the app.
- I selected the manual deployment method and linked my Heroku app to the GitHub repository.
- After the deployment was successfully concluded I was able to get the link to the deployed website.

## Credits

- I have been following the Love Sandwiches walkthrough project as a reference to how structure my program. Specifically the connection with Google API was done following the walkthrough project. [Love Sandwiches](https://github.com/AlessandroRossi87/love-sandwiches)
- The dataset was created on [ChatGPT](https://chat.openai.com/auth/login) by requesting 15 ice cream tastes for the headings I provided. I consequently modified the dataset to better fit the purposes of this project as I was moving along.
- The main menu graphics in ASCII was also created partly with [ChatGPT](https://chat.openai.com/auth/login) and then modified by me.
- The code for the read function was created from [docs.gspread.org](https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column)
- The code for the sorted() functions and key=lambda was created from [StackOverflow](https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda)
- The code for the list comprehension with an if statement was created from [StackOverflow](https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension)
- The exit() function was created from [FreeCodeCamp](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/)
- The class IceCream and its model were created from [W3](https://www.w3schools.com/python/python_classes.asp)
- The reverse=true argument was found on [StackOverflow](https://stackoverflow.com/questions/35800325/where-can-i-put-reverse-true-to-reverse-sorting-order)
- The flowchart was created in [LucidArt](https://www.lucidart.com/)

## Acknowledgements
I would like to thank my friends who supported me during this whole process while also giving a special thanks to David Calikes for his support and my mentor Luke Buchanan who provided me with guidance and has enhanced my learning experience.
