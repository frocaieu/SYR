**DESCRIPTION OF THE APP**
Our app, SYR aims to make your life easier by keeping track and organizing your expenses, this is possible because SYR scan receipts and automatically it organizes them into different folders based on the type of expense.



**FEATURES**
- _Receipt Scanning_: The app allows you to scan receipts using your camera. The scanned receipts are then stored in the app for future reference.
- _Expense Categorization_: The app automatically categorizes your expenses based on the type of purchase. This makes it easy to track specific types of expenses.
- _Expense Tracking_: The app keeps a running total of all your expenses, allowing you to see at a glance how much you're spending.



**FILES**
Files in Repository:

_main.py_: Contains the main code for the app.
_scanner.py_: Handles the receipt scanning functionality.
_categorization.py_: Manages the automatic categorization of expenses.
_tracker.py_: Implements the expense tracking features.
_search.py_: Future implementation for enhanced search capabilities.
_integration.py_: Placeholder for integration with financial platforms.
_monitoring.py_: Placeholder for refined expense monitoring features.
_README.md_: Detailed documentation about the app, including instructions for installation and usage.



**PREREQUISITES AND ENVIRONMENT**
_Libraries Used_:
- **OpenCV**: The app utilizes OpenCV for image processing and receipt scanning.
- **NumPy**: NumPy is used for efficient numerical operations in the app.

_Python Version_:
The app is developed and tested with Python 3.8 or higher. Make sure you have Python installed on your system.
To check your Python version, run the following command in your terminal:

'''bash
python --version



**LOG IN AND HOME PAGE**
<img width="274" alt="Captura de pantalla 2023-11-25 192209" src="https://github.com/frocaieu/SYR/assets/151723296/1eb7c065-0e7a-40f4-b8d0-79619cbf9595">

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



**ARCHITECTURE**
Our app uses a simple search algorithm to organize expenses. This algorithm is designed to recognize 
common types of expenses and categorize them accordingly.using a diverse set of sample data, 
which allows it to accurately categorize a wide range of expenses and allows the app to be highly personalized. 



**FUTURE IMPROVEMENTS**
Enhanced Search Capabilities: We aim to introduce more sophisticated search functionalities
to assist you in locating specific receipts or expenses with ease.

Integration with Financial Platforms: We are considering the integration of our app with widely-used financial tools and services.
This integration would enable you to import your expenses and transactions directly into the app, providing a seamless financial management experience.

Refined Expense Monitoring: We are developing new features that will offer you more in-depth insights into your spending patterns.


