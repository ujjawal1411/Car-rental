from datetime import datetime

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock  # Initialize the stock of cars

    def display_cars(self):
        print(f"We have {self.stock} cars available for rent.")
        return self.stock

    def hourly_rent(self, car_num):
        if car_num <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif car_num > self.stock:
            print(f"We are sorry, currently we have only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= car_num
            print(f"{car_num} car(s) rented on an hourly basis.")
            return now

    def daily_rent(self, car_num):
        if car_num <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif car_num > self.stock:
            print(f"We are sorry, currently we have only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= car_num
            print(f"{car_num} car(s) rented on a daily basis.")
            return now

    def weekly_rent(self, car_num):
        if car_num <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif car_num > self.stock:
            print(f"We are sorry, currently we have only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= car_num
            print(f"{car_num} car(s) rented on a weekly basis.")
            return now

    def return_car(self, request):
        rent_time, rent_basis, car_num = request

        if rent_time and rent_basis and car_num:
            now = datetime.now()
            rent_period = (now - rent_time).total_seconds()

            bill = 0
            if rent_basis == 1:  # Hourly
                bill = round(rent_period / 3600) * 100 * car_num
            elif rent_basis == 2:  # Daily
                bill = round(rent_period / (24 * 3600)) * 1000 * car_num
            elif rent_basis == 3:  # Weekly
                bill = round(rent_period / (7 * 24 * 3600)) * 5000 * car_num
            else:
                print("Invalid rent basis.")
                return None

            self.stock += car_num
            print(f"Thank you for returning the car(s). Your bill is ₹{bill}.")
            return bill
        else:
            print("Invalid request. Please provide all necessary details.")
            return None
