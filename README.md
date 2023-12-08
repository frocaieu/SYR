**DESCRIPTION OF THE APP**

Our app, SYR aims to make your life easier by keeping track and organizing your expenses, this is possible because SYR scan receipts and automatically it organizes them into different folders based on the type of expense.



**FEATURES**

- _Receipt Scanning_: The app allows you to scan receipts using your camera. The scanned receipts are then stored in the app for future reference.
- _Expense Categorization_: The app automatically categorizes your expenses based on the type of purchase. This makes it easy to track specific types of expenses.
- _Expense Tracking_: The app keeps a running total of all your expenses, allowing you to see at a glance how much you're spending.


**LOG IN AND HOME PAGE**

<img width="316" alt="image" src="https://github.com/frocaieu/SYR/assets/151723296/b08df413-38f6-42c9-ba38-fcf1938d1712">

A screen to see your expenses, to add new receipts and to see all the expenses organize into different categories:

<img width="419" alt="Captura de pantalla 2023-11-25 193319" src="https://github.com/frocaieu/SYR/assets/151723296/718a0610-5d7e-4652-8330-6c8f71e46298">




**USE OF THE APP**

First you log in and you enter into you home page.
you see 3 different buttons:

    1. to add a new ticket and if you click on it a new page opens to scan the new 
    receipt using the camera.
    
    2. button is to see all the expenses of the last 30 days, week...
    
    3. this third button also opens a new page where you see all your expenses 
    organized depending on the type of expense.

    

**INSTALLATION OF SYR!**

STEP BY STEP TO YOUR FUTURE WALLET!

1. Download Python and pycharm (link pycharm) (https://www.python.org/downloads/) into your desktop. 
Once you have done this you are ready download the code!

2. Download the code from the “CODING.py” folder

<img width="289" alt="Captura de pantalla 2023-11-28 a las 14 05 54" src="https://github.com/frocaieu/SYR/assets/151958716/de48f7a5-8c54-4060-81ca-95f694cf00f1">
 
3. Save “CODING.py” in a folder that you choose to be the directory of your project in Pycharm.
   
4. Once you have saved it, open this file in Pycharm by clicking on the directory, then clicking “New” and finally clicking “File” and type in the name of the file, in this case: “CODING.py”.
   
5. Go to the Terminal which is in the bottom left corner of your screen:
   
![image](https://github.com/frocaieu/SYR/assets/151958716/735dd441-db2c-4b63-8058-5d997aaf4219)

6. Type in: pip install PySimpleGUI
   
7. Now, run the code by clicking:

 <img width="36" alt="Captura de pantalla 2023-11-28 a las 14 08 06" src="https://github.com/frocaieu/SYR/assets/151958716/dac11c66-85dc-4128-8ea2-74e44cb9d1d1">

8. Follow what the system tells you to do; log in, write the name of receipts, its value, etc.

9. The password once entered the username chosen is: password
    
10. Dont forget to tell us your feedback and what you think!

    

**ENVIRONMENT**

_Libraries Used_:

- **PySimpleGUI**:is a Python library that simplifies the process of creating Graphical User Interfaces (GUI).
- **datetime**: is a Python module for manipulating dates and times.

_Python Version_:
The app is developed and tested with Python 3.8 or higher
Run the following command in your terminal: pip install PySimpleGUI



**ARCHITECTURE**

Simple Search: When you filter receipts by month in the ‘View Expenses By Month’ feature, it’s like doing a simple search. The code goes through each receipt in the list and checks if its date matches the selected month, which allows it to accurately categorize a wide range of expenses and allows the app to be highly personalized. 

Lists: The receipts in the User class is a list that holds all the receipts. Lists in Python can grow and shrink as needed.

Objects: The Receipt and User classes are used to create objects. Each Receipt object is a receipt with details like name, value, date, and
category. Each User object is a user with a username and a list of receipts.

Insertion: The add_receipt method in the User class is used to add a new receipt to the user’s list. This is an example of adding an item
to a list.

Traversal: The code goes through the list of receipts in several places. For example, when the ‘View Last Receipt’ button is clicked, it
gets the last receipt from the list. When the ‘View All Expenses’ button is clicked, it goes through all the receipts to display them in a
table.



**FUTURE IMPROVEMENTS**

Enhanced Search Capabilities: We aim to introduce more sophisticated search functionalities
to assist you in locating specific receipts or expenses with ease.

Integration with Financial Platforms: We are considering the integration of our app with widely-used financial tools and services.
This integration would enable you to import your expenses and transactions directly into the app, providing a seamless financial management experience.

Refined Expense Monitoring: We are developing new features that will offer you more in-depth insights into your spending patterns.



**CREDITS**

The idea, Strategy and creations of the app has been done by Group 8 during the Algorithm and Data Structure curse:

María Fernández Gomez-Monche
Diana De Lorenzo
María Consolación Fernández Cañavate
Francisco Javier Roca
Joshua Harpoof
María Martínez González

