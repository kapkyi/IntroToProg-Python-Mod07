# Pickling And Exception Handling
**Kapkyi Lwai**  
**Foundation Of Programing: Python**  
**Assignment 7: pickling and exception handling**  
**11/29/2022**      
## Introduction 
This assignment introduces the use of pickling and exception handling in python.  According to class text book in Chapter 7, (Michael Dawson, Python Programming, 3rd edition, 2010), pickling means to preserve. It is the process of converting Python object into byte stream and store in a file. Exception handling provides a get around solution to potential errors/crash. This can be done by displaying user the error and guiding them to the right path to the program. This assignment will demonstrate how pickling and exception handling are used in python program. The assignment will then be uploaded to GitHub page and in addition, I will create a webpage for the assignment. 
## Getting Started: 
I created a new sub-folder called Assignment07 inside my PythonClass folder and created a new project on PyCharm. A new Python file ‘FilesAndException.py’ was also created for writing my script. A starter script from module 7 (lab7-1) was added as a guide to create my program. The scripts will be modified and added to create a demo program to demonstrate how pickling and exception error handling are used. My program will interact with user by asking them to input their name, favorite color, and favorite number. The data entered will then be stored in binary file and the program will save as list and read and display back to the user. 
### Headers and Variables: 
After the starter script have been added to the new Python project, I modified the headers by adding my information and declared my variables (Figure 1).  This project also contains many pseudo codes and comments from top to bottom with ‘#’ at beginning followed by comments.  The program is started by declaring variables and constants. (Figure 1)
```
# ------------------------------------------------- #
# Title: Pickling and Exception Handling
# Description: A simple example of storing data in a binary file
#       and demonstrate pickling and exception handling in python
# ChangeLog: (Who, When, What)
# Kapkyi Lwai,<11.30.2022>,Created Script
# ------------------------------------------------- #

# Data -------------------------------------------- #
strFileName = 'MyFavorites.dat'
lstFavorites = []
```
Figure 1: headers and variables with comments #
## Writing The Script: (Load data in file MyFavorites.dat)
The first step for writing the script was to demonstrate pickling by creating a file ‘MyFavorites.dat’ for data to be stored. The data to be pickled are user’s Name, Favorite Color, and Favorite Number. In order to start the pickling, my script began with code to import the pickle module (Figure 2). This code will used ‘load’ and ‘dump’ methods to allow program to save and read data. 
```
import pickle  # This imports code from another code file!
```
Figure 2: script for importing pickle module 
## Writing The Script: (Processing pickle dumb and load data) 
The first part of the scripts used function ‘def’ to create file and open file in append binary mode ‘ab’. This part also includes scripts to read the data from the file created in read binary mode ‘rb’ (Figure 3). This part of the scripts is written to allow the program to save data and read data by utilizing pickle methods ‘dump’ and ‘load’. 
```
# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # Creating file and opening in append binary mode
    file = open(file_name, 'ab')
    pickle.dump(list_of_data, file)
    return list_of_data

def read_data_from_file(file_name):
    # Read the data from file
    file = open(file_name, 'rb')
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data
```
Figure 3: Processing data file 

## Writing The Script: (presentation (get user enter data)
The next part of the script is presentation and a demonstration of exception handling. In this area, the scripts will allow user to enter string data (name and favorite color) and integer data (favorite number). The exception error in this part will be when the user is asked to enter their favorite number (integer). The while loop with ‘try’ and ‘except’ functions were used to allow the program to recognize the user input error (Figure 4). In this case if a user enters the number as a string instead of a numeric integer, the program will display error message and guide the user to enter correct type of data (Figure 6 & Figure 7).  The data entered will then be stored in the file as lists. 
```
# Presentation ------------------------------------ #
# Get Data From user, then store it in a list
strName = str.lower(input('Enter Your Name: '))
strFavColor = str.lower(input('Enter Your Favorite Color: '))
# Get user input their favorite number until a valid (numeric) response is received
while True:
    try:
        intFavNum = int(input('Please Enter Your Favorite Number: '))
    except ValueError:  # inputs other than an integer is returned and prints correction message
        print('\nPlease use numeric for your favorite number')
        continue
    break
lstFavorites = [strName, strFavColor, intFavNum]
```
Figure 4: presentation (get user input data)

## Writing The Script: save to file and read file to display contents 
The last part of the scripts are written to store data as list into binary file and display the contents after reading the list object from the file. As shown in Figure 5 below, the function ‘save_data_to_file(strFileName, lstFavorites)’ allow program to store the list object into a binary file. To display the data, the function ‘print(read_data_from_file(strFileName))’ was called back.  A Few ‘print’ functions with messages and characters were added to make the display window look better (Figure 6 & Figure 7). 
```
# store the list object into a binary file
print(input('\nPress Enter-key To Store The Data...')) # guide user to continue
save_data_to_file(strFileName, lstFavorites)

# Read the data from the file into a new list object and display the contents
print('Your Data On File')
print('-----------------------')
print(read_data_from_file(strFileName))
print('-----------------------')

exit('\nGoodbye!')
```
Figure 5: scripts to send data to file and read data from file and display contents

## Running The Script: 
Lastly, I ran the program in PyCharm as well as on Shell window to double check it is working. The program ran smoothly in PyCharm as shown in screenshots (Figure 6) below as well as on Shell window (Figure 7). The file ‘MyFavorites.dat’ was also created successfully (Figure 8).
![Description](https://github.com/kapkyi/IntroToProg-Python-Mod07/blob/main/Screen%20Shot%2006.png)
Figure 6: Program running successful in PyCharm

![Description](https://github.com/kapkyi/IntroToProg-Python-Mod07/blob/main/Screen%20Shot%2007.png)
Figure 7: program running in Shell window

![Description](https://github.com/kapkyi/IntroToProg-Python-Mod07/blob/main/Screen%20Shot%2008.png)
Figure 8: binary file MyFavorites.dat created 

## Upload to GitHub: 
This project was uploaded to my GitHub account as public. The project was uploaded for others to view and provide comments or edits. In addition, a webpage for my assignment was also created.

### Assignment link: https://github.com/kapkyi/IntroToProg-Python-Mod07 
### Webpage link: (https://kapkyi.github.io/IntroToProg-Python-Mod07/)


## Summary: 
In conclusion, this project was created based on the starter script lab 7-1 and it was modified with added codes to complete the program. The assignment demonstrated how to utilize picking and exception error handling and upload my project to GitHub as well as how to created web page. From reading Chapter 7 of the textbook (Python Programing, 3rd edition, Michael Dawson, 2010), looking at the Module 7 documentation, lecture video and demonstrations, and the starter Python script outlines provided for the modeule, I was able to successfully complete the program. 
