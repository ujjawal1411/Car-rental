class Customer:
    def __init__(self):
        self.cars = 0  # Number of cars rented
        self.rent_basis = 0  # Rental mode: 1=hourly, 2=daily, 3=weekly
        self.rent_time = None  # Time when cars were rented

    def request_cars(self):
        """Request cars to rent."""
        car_num = int(input("How many cars would you like to rent? "))
        if car_num <= 0:
            print("Number of cars should be greater than zero.")
            return None
        else:
            self.cars = car_num
            return self.cars

    def return_cars(self):
        """Return rented cars."""
        if self.rent_time and self.rent_basis and self.cars:
            return self.rent_time, self.rent_basis, self.cars
        else:
            return None, None, None
