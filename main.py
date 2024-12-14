from carRent import CarRental
from customer import Customer


def car_rental_interface():
    rental_service = CarRental(stock=10)  # Initialize with 10 cars in stock
    customer = Customer()  # Create a new customer object

    while True:
        print("\nWelcome to the Car Rental Service!")
        print("1. Display available cars")
        print("2. Rent a car hourly (₹100 per hour)")
        print("3. Rent a car daily (₹1000 per day)")
        print("4. Rent a car weekly (₹5000 per week)")
        print("5. Return a car")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                rental_service.display_cars()
            elif choice in [2, 3, 4]:
                car_num = customer.request_cars()  # Customer requests cars
                if car_num:
                    if choice == 2:  # Hourly rental
                        customer.rent_time = rental_service.hourly_rent(car_num)
                        customer.rent_basis = 1
                    elif choice == 3:  # Daily rental
                        customer.rent_time = rental_service.daily_rent(car_num)
                        customer.rent_basis = 2
                    elif choice == 4:  # Weekly rental
                        customer.rent_time = rental_service.weekly_rent(car_num)
                        customer.rent_basis = 3
            elif choice == 5:
                rent_details = customer.return_cars()
                if rent_details:
                    rental_service.return_car(rent_details)
                    # Reset customer data after returning the car
                    customer.cars = 0
                    customer.rent_basis = 0
                    customer.rent_time = None
                else:
                    print("You did not rent any cars.")
            elif choice == 6:
                print("Thank you for using the Car Rental Service!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    car_rental_interface()
