"""
student = {"name":"Alice", "age":23, "major":"Computer Science"}

print("\n")


print(student)


print("\n------------\n")


student["GPA"] = 3.8
student["year"] = "Senior"

print(student)


print("\n------------\n")


print(student['name'])
print(student["GPA"])


print("\n------------\n")


if 'email' in student:
    print("Email found!")
else: 
    print("Email not found!")


print("\n------------\n")


try: 
    print(student['email'])
except KeyError:
    print("Key not found!")

print("\n------------\n")


em = student.get('email', "Key not found")
print(em)


print("\n------------\n")


for Key in student.keys():
    print(Key)

print("\n")

for values in student.values():
    print(values)

print("\n")

for Key, value in student.items():
    print(Key, "=", value)


print("\n------------\n")


#help(dict)
#print(dir(student))
"""

print("\n------------\n") 

import json

#Dictionary to store contacts
contacts = {}

#Load JSON back into a dictionary (handle file not existing or empty file)
try:
    with open ("contacts_file.txt", "r") as file:
        contacts = json.load(file) # Load data into contacts dictionary
except (FileNotFoundError, json.JSONDecodeError): 
    print("Initialize empty if file doesn't exist or has invalid JSON\n")
    contacts = {} # Initialize empty if file doesn't exist or has invalid JSON




while True:

    #The options the user can chose
    print("""
Options: 
(1) Add new contact 
(2) Update contact
(3) Delete contact
(4) Display all contacts 
(5) Retrieve contact
(6) exit 
    """)

    #user input 
    user_input = input("choose option: ")

    if user_input in ["1", "2", "3"]:
        #adds a new contact
        if user_input == "1":
            name_input = input("\n\nEnter Name: ").strip()
            if not name_input:
                print("\nName cannot be empty!")
                continue

            phone_number_input = input("\nEnter phone number: ").strip()
            if not phone_number_input:
                print("\nPhone number cannot be empty")
                continue

            email_input = input("\nEnter email: ").strip()
            if not email_input:
                print("\nEmail cannot be empty!")
                continue

            #checks if contact exist
            if name_input in contacts:
                    print(f"\n{name_input} already exist!\n")

            else:
                contacts[name_input] = {"phone": phone_number_input, "email": email_input}
                print(f"\n{name_input} added!\n")

        #Updates/changes contacts phone number 
        elif user_input == "2":
            print("\nAre you sure you want to change a contact?")

            update_yn_input = input("\ny/n: ").lower()
            if update_yn_input == "y":
                update_name_input = input("\n\nName: ").strip()
                if not update_name_input:
                    print("\nName cannot be empty!")
                    continue

                update_phone_input = input("\nNew number: ").strip()
                if not update_phone_input:
                    print("\nNumber cannot be empty!")
                    continue

                update_email_input = input("\n New email: ").strip()
                if not update_email_input:
                    print("\nEmail cannot be empty!")
                    continue
                    
                if update_name_input  in contacts: 
                    contacts[name_input] = {"phone": phone_number_input, "email": email_input}
                    print(f"\n{update_name_input}'s phone number and email updated!\n")
                    
                else:
                    print(f"\n{update_name_input} doesn't exist!\n") 

            elif update_yn_input == "n":
                print("\nUpdate cancelled")

        #Deletes a single contact
        elif user_input == "3":
            print("\nAre you sure?\n")
            delete_name_yn_input = input("\ny/n: ").lower()

            if delete_name_yn_input == "y":
                delete_name_input = input("\nName: ")

                if delete_name_input in contacts:
                    contacts.pop(delete_name_input)
                    print(f"\n{delete_name_input} deleted!\n")
                
                else:               
                    print(f"\n{delete_name_input} doesn't exist!\n")

            elif delete_name_yn_input == "n": 
                print("\nDeletion cancelled.")

        # Save contacts after each modification
        with open("contacts_file.txt", "w") as file: 
            json.dump(contacts, file) #Convert dictionary to JSON and save
            print("contacts saved")
            
    #Display all contacts 
    elif user_input == "4":
        if contacts:
            print("\n\nAll contacts: \n")
            for name, details in contacts.items():
                # make it print(f)
                print(f"""\n
Name: {name}  
Phone number: {details['phone']}, {details[phone_number_input_two]}
Email: {details['email']}
                """)
        else:
            print("\n\nNo contacts found!\n\n")

    #retrives a single contacts number by name
    elif user_input == "5":
        name_input = input("\n\nName: ")  
        contract = contacts.get(name_input)
        print(f"""\n
        Phone: {contract['phone']}
        Email: {contract['email']}
        """)

    #exits the program and aks for a confirmation 
    elif user_input == "6":
        print("\n\nAre you sure you want to exit?\n")
        exit_input = input("y/n: ").lower()

        if exit_input == "y":
            #Saves contacts before exiting
            with open("contacts_file.txt", "w") as file:
                json.dump(contacts, file)
            print("\nContacts saved. Goodbye!\n")
            break

        elif exit_input == "n":
            print("")
            continue
            
    #prints not valid if you type something else than the options        
    else:
        print("\nInvalid option! Please choose a valid number.\n")