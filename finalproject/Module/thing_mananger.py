import csv
from .thing import Thing
import os

class ThingManager:
    def __init__(self, filename):
        self.filename = filename
        self.things = []  # List to store Thing objects
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            print(f"Error: File '{self.filename}' not found.")
            return

        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                print("Loading data from CSV file...")
                for row in reader:
                    try:
                        thing = Thing(
                            row['name'],
                            row['type'],
                            row['color'],
                            row['weight'],
                            row['age']
                        )
                        self.things.append(thing)
                    except KeyError as e:
                        print(f"Missing key in CSV data: {e}")
                    except ValueError as e:
                        print(f"Data type conversion error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")

    def save_data(self):
        with open(self.filename, mode='w', newline='') as file:
            if self.things:
                writer = csv.DictWriter(file, fieldnames=self.things[0].to_dict().keys())
                writer.writeheader()
                writer.writerows([thing.to_dict() for thing in self.things])
            else:
                print("No data to save.")

    def display_all(self):
        if not self.things:
            print("No data to display.")
        else:
            for thing in self.things:
                print(thing)

    def display_count(self):
        print(f"Total number of things: {len(self.things)}")

    def get_valid_float(self, value, field_name):
        """Helper function to validate float values (e.g., weight)"""
        try:
            return float(value)
        except ValueError:
            print(f"Invalid {field_name}. Please enter a valid number for {field_name}.")
            return None  # Return None if invalid
    
    def get_valid_int(self, value, field_name):
        """Helper function to validate integer values (e.g., age)"""
        try:
            return int(value)
        except ValueError:
            print(f"Invalid {field_name}. Please enter a valid integer for {field_name}.")
            return None  # Return None if invalid

    def add_thing(self, name, type_, color, weight, age):
        # Validate weight and age inputs
        valid_weight = self.get_valid_float(weight, "Weight")
        valid_age = self.get_valid_int(age, "Age")
        
        # If any input is invalid, do not add the thing or save to CSV
        if valid_weight is None or valid_age is None:
            print("Invalid input. Thing not added.")
            return
        
        # All inputs are valid, create the new Thing and add it to the list
        new_thing = Thing(name, type_, color, valid_weight, valid_age)
        self.things.append(new_thing)
        print("New thing added successfully.")
        
        # Save data to CSV if all inputs are valid
        self.save_data()

    def search_thing(self, search_type, search_value):
        # Validate if the search_type is a valid attribute of Thing
        valid_attributes = ['name', 'type', 'color', 'weight', 'age']
        if search_type not in valid_attributes:
            print(f"Invalid search field: {search_type}. Valid fields are: {', '.join(valid_attributes)}")
            return

        # Clean up the search_value
        search_value = search_value.strip().lower()

        # Perform the search
        results = [
            thing for thing in self.things 
            if getattr(thing, search_type).strip().lower() == search_value
        ]

        # Display results
        if results:
            for result in results:
                print(result)
        else:
            print("No match found.")
    
    def delete_thing(self, name):
        # Store the initial length of the things list
        initial_len = len(self.things)
        
        # Filter out the thing with the given name (case-insensitive)
        self.things = [thing for thing in self.things if thing.name.lower().strip() != name.lower().strip()]
        
        # Check if anything was deleted
        if len(self.things) < initial_len:
            print("Thing deleted successfully.")
            self.save_data()  # Save the updated list to CSV
        else:
            print("No such thing found.")
