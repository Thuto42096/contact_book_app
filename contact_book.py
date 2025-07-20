import json
import os


class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()
   
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}
    
    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone}
            self.save_contacts()

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("-" * 45)
            print("Contacts List:")
            for name, details in self.contacts.items():
                
                print("-" * 45)
                print(f"Name: {name}, Phone: {details['phone']}")
                print("-" * 45)

class Contact_bookContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone})"
    
if __name__ == "__main__":
    contact_book = ContactBook()
