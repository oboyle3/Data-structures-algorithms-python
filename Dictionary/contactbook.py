#step 1 initialize the dictionary
contact_book = {}

#function to add contact
def add_contact(name, phone_number):
    #add the contact to the dictionary
    contact_book[name] = phone_number
    print(f"contact {name} added phone {phone_number}")

name = "pat"
phone = "726382"
add_contact(name, phone)
add_contact("test", "9276382")
add_contact("kerry", "072620")
print(contact_book)

def delete_contact(name):
    #check if the contact is in the dictionary
    if name in contact_book:
        print(f"we found {name}")
        del contact_book[name]
    else :
        print(f"we didnt find {name}  so what the heck man?")

delete_contact("pat")
print(contact_book)
