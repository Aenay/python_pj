import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Module.thing_mananger import ThingManager


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
    filename = os.path.join(base_dir, 'finalproject', 'Data', 'things.csv')
    
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
            print("Saving data before exiting...")
            print("Goodbye!")
            exit()
            
            

        # elif choice == '9':
        #     type_ = input("Enter color to search: ")
        #     manager.search_thing('color', color)
        #     break
        else:
            print("Invalid choice. Please try again.")
    


if __name__ == "__main__":
    main()
