class PhoneBook:
    def __init__(self):
        self.phone_book = {}

    def insert_number(self, first_name, surname, phone_number):
        person = (first_name, surname)
        if person not in self.phone_book:
            self.phone_book[person] = [phone_number]
        else:
            self.phone_book[person].append(phone_number)

    def retrieve_number(self, first_name, surname):
        person = (first_name, surname)
        if person in self.phone_book:
            return self.phone_book[person]
        else:
            return None

    def delete_number(self, first_name, surname, phone_number):
        person = (first_name, surname)
        if person in self.phone_book:
            if phone_number in self.phone_book[person]:
                self.phone_book[person].remove(phone_number)
                if not self.phone_book[person]:
                    del self.phone_book[person]
                return True
        return False

    def print_phone_book(self):
        for person, numbers in self.phone_book.items():
            print(f"{person[0]} {person[1]}:", ', '.join(numbers))

# Example usage with user input:
phone_book = PhoneBook()

while True:
    print("\nOptions:")
    print("1. Add a new phone number")
    print("2. Retrieve phone numbers for a person")
    print("3. Delete a phone number for a person")
    print("4. Print the entire phone book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        phone_number = input("Enter phone number: ")
        phone_book.insert_number(first_name, surname, phone_number)

    elif choice == '2':
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        numbers = phone_book.retrieve_number(first_name, surname)
        if numbers:
            print(f"{first_name} {surname}'s numbers:", ', '.join(numbers))
        else:
            print(f"No numbers found for {first_name} {surname}.")

    elif choice == '3':
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        phone_number = input("Enter phone number to delete: ")
        success = phone_book.delete_number(first_name, surname, phone_number)
        if success:
            print(f"Deleted {phone_number} for {first_name} {surname}.")
        else:
            print(f"No matching record found for {first_name} {surname} with phone number {phone_number}.")

    elif choice == '4':
        if choice == '1':
             phone_book.print_phone_book()
        else:
            print("No Phone Number Yet. Choose OPtion 1 And Add Phone Number!")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
