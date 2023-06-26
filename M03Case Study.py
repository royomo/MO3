class Vehicle:
    def __init__(self, vehicle_type):
        """
        Initialize a Vehicle object with a vehicle type.

        Args:
            vehicle_type (str): The type of the vehicle (car, truck, plane, boat, broomstick).
        """
        self.vehicle_type = vehicle_type

    def display_info(self):
        """
        Display the vehicle type.
        """
        print("Vehicle type:", self.vehicle_type)


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        """
        Initialize an Automobile object.

        Args:
            vehicle_type (str): The type of the vehicle (car, truck, plane, boat, broomstick).
            year (str): The year of the vehicle.
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
            doors (str): The number of doors (2 or 4).
            roof (str): The type of roof (solid or sun roof).
        """
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        """
        Display the automobile information.
        """
        super().display_info()
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def collect_car_info():
    """
    Collect car information from the user.

    Returns:
        Automobile: An instance of the Automobile class with the collected information.
    """
    vehicle_type = input("Enter the type of vehicle (car, truck, plane, boat, broomstick): ")
    year = input("Enter the year of the vehicle: ")
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    return Automobile(vehicle_type, year, make, model, doors, roof)


# Collect car information and display it
vehicle = collect_car_info()
vehicle.display_info()

# Storing car info by make, model, and year in the same file
filename = f"{vehicle.make}_{vehicle.model}_{vehicle.year}.txt"
with open(filename, "a") as file:  # Use "a" mode to append to the file
    # Write car information to the file
    file.write(
        f"""Make: {vehicle.make}
Model: {vehicle.model}
Year: {vehicle.year}
Number of doors: {vehicle.doors}
Type of roof: {vehicle.roof}
"""
    )

print("Car information has been stored in", filename)
