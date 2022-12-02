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

import pickle  # This imports code from another code file!

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

# store the list object into a binary file
print(input('\nPress Enter-key To Store The Data...')) # guide user to continue
save_data_to_file(strFileName, lstFavorites)

# Read the data from the file into a new list object and display the contents
print('Your Data On File')
print('-----------------------')
print(read_data_from_file(strFileName))
print('-----------------------')

exit('\nGoodbye!')
