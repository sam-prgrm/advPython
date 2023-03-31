#   Author: Samara
#   Date: 03-25-2023
#   Description: Name and Email Addresses Program
#                   This program keeps names and email addresses in a dictionary as key-value pairs.
#                       The program should display a menu that:
#                       Lets the user look up a person’s email address
#                       Add a new name and email address
#                       Change an existing email address
#                       Delete an existing name and email address.
#                   Additional Specifications for your program:
#                       Use descriptive variable names. 
#                       Your program must include a comment header listing your name, date, purpose of the program, etc.
#                       The program should pickle the dictionary and save it to a file when the user exits the program.
#                       Each time the program starts, it should retrieve the dictionary from the file and unpickle it.

import pickle as pickle
import os

# The add_name function adds a new entry to the contacts dictionary
def add(contacts):
    # Get name and email
    name = input('Enter name: ')
    name = name.lower().strip()
    email = input('Enter email: ')
    email = email.lower().strip()

    # if the name is not found, add the entry
    if name not in contacts:
        contacts[name] = email
        print('Entry added.')
    else:
        print('That entry already exists.')
        

# The change function changes an existing entry in the contacts dictionary
def change(contacts):
    name = input('Enter name: ')
    name = name.lower().strip()

    # name found, changes the email
    if name in contacts:
        email = input('Enter email: ')
        email = email.lower().strip()
        contacts[name] = email
    else:
        print('That name is not found.')

    print('Entry changed.')
    
# The lookUp function looks up a name in the dictionary contacts
def lookUp(contacts):
    name = input('Enter name: ')
    name = name.lower().strip()
    value = contacts.get(name, 'Entry not found.')
    print('Email: ' + value)
    print('Value found.')
    
# The delete function deletes an entry from the contacts dictionary
def delete(contacts):
    # Get name to look up
    name = input('Enter name: ')
    name = name.lower().strip()

    # If the name is found, delete the entry
    if name in contacts:
        del contacts[name]
    else:
        print('That name is not found.')
    print('Entry deleted.')

# The display function displays the dictionary
def display(contacts):
    print(contacts)
    
def load_contacts():
    try:
        #Open contacts
        if (os.path.getsize('contacts.dat') > 0):
            input_file = open('contacts.dat', 'rb')
            
            # Unpickle dictonary
            contacts = pickle.load(input_file)
            
            # Close file
            input_file.close()
            return contacts
            
        else:
            contacts = dict()
    except IOError:
        # COuld not open the dictionary
        contacts = dict()
        
    return contacts

def save_contacts(contacts):
    # The save_contacts funtion pickles the specified
    # object and saves it to the contacts file.
    # Open the file for writing.
    output_file = open('contacts.dat', 'wb')
    
    # Pickle the dictionary and save it.
    pickle.dump(contacts, output_file)
    
    # Close the file.
    output_file.close()

def main():

    contacts = load_contacts()
        
    print('This program adds name and email to a dictionary of contacts.')
    
    input_option = '1'
    while(input_option != '6'):
        menu = '\n'
        menu += 'Menu: \n'
        menu += '(1) Look up an email.\n'
        menu += '(2) Add new name and email address.\n'
        menu += '(3) Change email address.\n'
        menu += '(4) Delete an existing name and email address.\n'
        menu += '(5) Display dictionary.\n'
        menu += '(6) Exit.\n'
        menu += 'Enter an option: \n'

        input_option = input(menu)
        input_option = input_option.strip()

        match input_option:
            case '1':
                lookUp(contacts)
            case '2':
                add(contacts)
            case '3':
                change(contacts)
            case '4':
                delete(contacts)
            case '5':
                display(contacts)
            case '6':
                break

    save_contacts(contacts)

# run program    
main()
        
        
        
        
