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
        if name in self.contacts:
            print(f"Contact {name} already exists.")
        else:
            self.contacts[name] = {'phone': phone}
            self.save_contacts()
            print(f"Contact {name} added successfully.")

    def get_contact(self, name):
        return self.contacts.get(name, None)
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")
    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)
        print("Contacts saved successfully.")

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

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone})"
    
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.display_contacts()
