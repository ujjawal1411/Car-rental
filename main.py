from carRent import CarRental

def car_rental_interface():
    rental_service = CarRental(stock=10)  # Initializing with 10 cars
    while True:
        print("\nWelcome to the Car Rental Service!")
        print("1. Display available cars")
        print("2. Rent a car hourly (₹100 per hour)")
        print("3. Rent a car daily (₹1000 per day)")
        print("4. Rent a car weekly (₹5000 per week)")
        print("5. Return a car")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            rental_service.display_cars()
        elif choice == 2:
            car_num = int(input("How many cars would you like to rent? "))
            rental_service.hourly_rent(car_num)
        elif choice == 3:
            car_num = int(input("How many cars would you like to rent? "))
            rental_service.daily_rent(car_num)
        elif choice == 4:
            car_num = int(input("How many cars would you like to rent? "))
            rental_service.weekly_rent(car_num)
        elif choice == 5:
            try:
                rent_time = datetime.strptime(
                    input("Enter the rent start time (YYYY-MM-DD HH:MM:SS): "),
                    "%Y-%m-%d %H:%M:%S",
                )
                rent_basis = int(
                    input("Enter the rent basis (1 for hourly, 2 for daily, 3 for weekly): ")
                )
                car_num = int(input("How many cars are you returning? "))
                rental_service.return_car((rent_time, rent_basis, car_num))
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 6:
            print("Thank you for using the Car Rental Service!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    car_rental_interface()
