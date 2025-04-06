# contact_book

CONTACTS_FILE = "contacts.txt" # This is our mini database for now

def add_contact():
    name = input("Enter name: ").strip() #strip() will remove any accidental spaces
    phone = input("Enter phone number: ").strip()
    
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone}\n") # Adds new contact without deleting previous data
    
    print(f"Contact '{name}' added.")

def search_contact():
    search_name = input("Enter name to search: ").strip().lower() # Ensures name is not case sensitive
    found = False

    with open(CONTACTS_FILE, "r") as file: #Loop through each line and match the name
        for line in file:
            name, phone = line.strip().split(",")
            if name.lower() == search_name:
                print(f" {name}: {phone}")
                found = True
                break

    if not found:
        print("Contact not found.")

def view_contacts():
    print("\n All Contacts:")
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts saved.")
        for line in contacts: # Loop through each line and display the name and number
            name, phone = line.strip().split(",")
            print(f"{name}: {phone}")
    print()

# Creating our Contact Book Menu
def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        # Based on user choice, call the appropriate function
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!") # Exits the loop
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
     main()
