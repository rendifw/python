class Restaurant:
    def __init__(self, name, profit):
        self.name = name
        self.profit = profit

    def booking(self):
        print("You can book a table in this restaurant.")

# CHILD CLASS
class FastFood(Restaurant):
    def __init__(self, name, profit, employees, drive_thru): # Define child attributes
        super().__init__(name, profit, employees) # Initializes parent's __init__
        self.drive_thru = drive_thru

    # Define child method
    def describe_drive_thru(self):
        if self.drive_thru:
            print(f"Drive-thru available")
        else:
            print(f"Drive-thru not available")
    
    # Overrides the parent's booking method
    def booking(self):
        print("This place cannot take reservations.")


