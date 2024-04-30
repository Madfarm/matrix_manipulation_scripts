import pandas as pd

class PenCollection:
    def __init__(self):
        self.pens = pd.DataFrame({
            'name': ['Gel Pen', 'Ballpoint', 'Fountain', 'Rollerball', 'Marker', 'Highlighter', 'Calligraphy', 'Mechanical', 'Felt-tip', 'Brush Pen'],
            'condition': ['Good', 'Fair', 'Excellent', 'Poor', 'Good', 'Fair', 'Excellent', 'Poor', 'Good', 'Fair'],
            'value': [1.50, 1.00, 10.00, 0.75, 2.00, 1.25, 15.00, 3.50, 2.50, 5.00]
        }, index=range(1, 11))

    def create_pen(self, name, id, condition, value):
        if id in self.pens.index:
            print("Pen with this ID already exists.")
        else:
            new_pen = pd.DataFrame({'name': [name], 'condition': [condition], 'value': [value]}, index=[id])
            self.pens = pd.concat([self.pens, new_pen])
            print("Pen created successfully.")

    def read_pen(self, id):
        if id in self.pens.index:
            return self.pens.loc[id]
        else:
            print("Pen not found.")
            return None

    def update_pen(self, id, name=None, condition=None, value=None):
        if id in self.pens.index:
            if name:
                self.pens.loc[id, 'name'] = name
            if condition:
                self.pens.loc[id, 'condition'] = condition
            if value:
                self.pens.loc[id, 'value'] = value
            print("Pen updated successfully.")
        else:
            print("Pen not found.")

    def delete_pen(self, id):
        if id in self.pens.index:
            self.pens.drop(id, inplace=True)
            print("Pen deleted successfully.")
        else:
            print("Pen not found.")

    def display_pens(self):
        print(self.pens)

def main():
    collection = PenCollection()

    while True:
        print("\n1. Create Pen")
        print("2. Read Pen")
        print("3. Update Pen")
        print("4. Delete Pen")
        print("5. Display Pens")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter pen name: ")
            id = input("Enter pen ID: ")
            condition = input("Enter pen condition: ")
            value = float(input("Enter pen value (in USD): "))
            collection.create_pen(name, id, condition, value)
        elif choice == "2":
            id = input("Enter pen ID: ")
            pen = collection.read_pen(id)
            if pen is not None:
                print(pen)
        elif choice == "3":
            id = input("Enter pen ID: ")
            name = input("Enter new pen name (or press Enter to keep the same): ")
            condition = input("Enter new pen condition (or press Enter to keep the same): ")
            value = input("Enter new pen value (or press Enter to keep the same): ")
            collection.update_pen(id, name or None, condition or None, float(value) if value else None)
        elif choice == "4":
            id = input("Enter pen ID: ")
            collection.delete_pen(id)
        elif choice == "5":
            collection.display_pens()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()