import csv

class Thing:
    def __init__(self, name, type_, color, weight, age):
        self.name = name
        self.type = type_
        self.color = color
        self.weight = float(weight)  # Convert weight to float for consistency
        self.age = int(age)          # Convert age to int for consistency

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "color": self.color,
            "weight": self.weight,
            "age": self.age
        }

    def update(self, type_=None, color=None, weight=None, age=None):
        if type_:
            self.type = type_
        if color:
            self.color = color
        if weight:
            self.weight = float(weight)
        if age:
            self.age = int(age)

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Weight: {self.weight}, Age: {self.age}"


class ThingManager:
    def __init__(self, filename):
        self.filename = filename
        self.things = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                print("Loading data from CSV file...")
                for row in reader:
                    try:
                        # Creating Thing instance after ensuring proper data conversion
                        thing = Thing(
                            row['name'],
                            row['type'],
                            row['color'],
                            row['weight'],
                            row['age']
                        )
                        self.things.append(thing)
                        print(f"Loaded: {thing}")  # Debug output for each loaded row
                    except KeyError as e:
                        print(f"Missing key in CSV data: {e}")
                    except ValueError as e:
                        print(f"Data type conversion error: {e}")
            print(f"Total items loaded: {len(self.things)}")  # Print total items loaded
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty dataset.")

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

    def add_thing(self, name, type_, color, weight, age):
        new_thing = Thing(name, type_, color, weight, age)
        self.things.append(new_thing)
        print("New thing added successfully.")
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
        initial_len = len(self.things)
        self.things = [thing for thing in self.things if thing.name.lower() != name.lower()]
        if len(self.things) < initial_len:
            print("Thing deleted successfully.")
        else:
            print("No such thing found.")

    def update_thing(self, name):
        for thing in self.things:
            if thing.name.lower() == name.lower():
                print("Leave field blank to keep current value.")
                type_ = input(f"Enter new type ({thing.type}): ") or None
                color = input(f"Enter new color ({thing.color}): ") or None
                weight = input(f"Enter new weight ({thing.weight}): ") or None
                age = input(f"Enter new age ({thing.age}): ") or None
                thing.update(type_, color, weight, age)
                print("Thing updated successfully.")
                self.save_data()
                return
        print("No such thing found.")


def main():
    filename = 'things.csv'
    manager = ThingManager(filename)
    
    while True:
        print("\nMain Menu:")
        print("1. Display all thing information")
        print("2. Display total number of things")
        print("3. Add new thing information")
        print("4. Search thing information by Name")
        print("5. Search thing information by Type")
        print("6. Delete thing information")
        print("7. Update/Edit thing information")
        print("8. Exit")
        # print("9. Search thing information by Color")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manager.display_all()
        elif choice == '2':
            manager.display_count()
        elif choice == '3':
            name = input("Enter name: ")
            type_ = input("Enter type: ")
            color = input("Enter color: ")
            weight = input("Enter weight (kg): ")
            age = input("Enter age (years): ")
            manager.add_thing(name, type_, color, weight, age)
        elif choice == '4':
            name = input("Enter name to search: ")
            manager.search_thing('name', name)
        elif choice == '5':
            type_ = input("Enter type to search: ")
            manager.search_thing('type', type_)
        elif choice == '6':
            name = input("Enter name to delete: ")
            manager.delete_thing(name)
        elif choice == '7':
            name = input("Enter name to update: ")
            manager.update_thing(name)
        elif choice == '8':
            manager.save_data()
            print("Exiting the program. Data saved.")
        # elif choice == '9':
        #     type_ = input("Enter color to search: ")
        #     manager.search_thing('color', color)
        #     break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
