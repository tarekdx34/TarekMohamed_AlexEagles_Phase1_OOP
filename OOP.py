# Updated Flight Class with a method to filter flights based on parameters
class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, price, airline, departure_airport, arrival_airport):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.airline = airline
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.available_seats = 100  # Example value

    def is_available(self):
        return self.available_seats > 0

    def get_details(self):
        return {
            "Flight Number": self.flight_number,
            "Departure": self.departure_time,
            "Arrival": self.arrival_time,
            "Price": self.price,
            "Airline": self.airline,
            "Available Seats": self.available_seats
        }

    @staticmethod
    def filter_flights(flights, parameter, value):
        """Filters flights based on a given parameter and value."""
        filtered_flights = []
        for flight in flights:
            if parameter == "time" and flight.departure_time == value:
                filtered_flights.append(flight)
            elif parameter == "price" and flight.price <= value:
                filtered_flights.append(flight)
            elif parameter == "airline" and flight.airline == value:
                filtered_flights.append(flight)
        return filtered_flights


# Airport Class remains the same
class Airport:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} ({self.code}) located in {self.location}"


# Updated Customer Class to collect details
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    @staticmethod
    def input_customer_details():
        """Takes customer details as input and returns a Customer object."""
        name = input("Enter customer name: ")
        contact = input("Enter customer contact information: ")
        return Customer(name, contact)

    def update_contact(self, new_contact):
        self.contact = new_contact


# MealOption and AdditionalService Classes remain the same
class MealOption:
    def __init__(self, option_name, price):
        self.option_name = option_name
        self.price = price


class AdditionalService:
    def __init__(self, service_name, price):
        self.service_name = service_name
        self.price = price


# Updated Booking Class with print functionality
class Booking:
    def __init__(self, customer, flight):
        self.customer = customer
        self.flight = flight
        self.meal_option = None
        self.additional_services = []

    def add_meal_option(self, meal_option):
        self.meal_option = meal_option

    def add_additional_service(self, service):
        self.additional_services.append(service)

    def calculate_total(self):
        total = self.flight.price
        if self.meal_option:
            total += self.meal_option.price
        for service in self.additional_services:
            total += service.price
        return total

    def confirm_booking(self):
        if self.flight.is_available():
            self.flight.available_seats -= 1
            print(f"Booking confirmed for {self.customer.name}")
            print(f"Total cost: ${self.calculate_total()}")
        else:
            print("Flight is not available")

    def print_booking_details(self):
        print("----- Booking Details -----")
        print(f"Customer Name: {self.customer.name}")
        print(f"Contact: {self.customer.contact}")
        print(f"Flight Number: {self.flight.flight_number}")
        print(f"Departure: {self.flight.departure_time}")
        print(f"Arrival: {self.flight.arrival_time}")
        print(f"Airline: {self.flight.airline}")
        print(f"Price: ${self.flight.price}")
        if self.meal_option:
            print(f"Meal Option: {self.meal_option.option_name} (${self.meal_option.price})")
        if self.additional_services:
            for service in self.additional_services:
                print(f"Additional Service: {service.service_name} (${service.price})")
        print(f"Total Cost: ${self.calculate_total()}")
        print("---------------------------")


# Function to print all available flights
def print_available_flights(flights):
    print("\n--- Available Flights ---")
    for index, flight in enumerate(flights):
        details = flight.get_details()
        print(f"{index + 1}. Flight Number: {details['Flight Number']}, Departure: {details['Departure']}, "
              f"Arrival: {details['Arrival']}, Price: ${details['Price']}, Airline: {details['Airline']}")
    print("-------------------------\n")

# Function to take user input and select the desired flight
def select_flight(flights):
    while True:
        try:
            choice = int(input("Enter the number of the desired flight: "))
            if 1 <= choice <= len(flights):
                return flights[choice - 1]
            else:
                print("Invalid choice. Please select a valid flight number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
# Creating some airports
departure_airport = Airport("JFK", "John F. Kennedy International Airport", "New York, USA")
arrival_airport = Airport("LAX", "Los Angeles International Airport", "Los Angeles, USA")

# Creating some flights
flights = [
    Flight("AA101", "08:00 AM", "11:00 AM", 300, "American Airlines", departure_airport, arrival_airport),
    Flight("DL202", "09:00 AM", "12:00 PM", 250, "Delta Airlines", departure_airport, arrival_airport),
    Flight("UA303", "10:00 AM", "01:00 PM", 280, "United Airlines", departure_airport, arrival_airport),
    Flight("AL202", "05:00 AM", "12:00 PM", 220, "Alexandria Airlines", departure_airport, arrival_airport),
    Flight("XL202", "01:00 AM", "12:00 PM", 280, "Borg-ALarab Airlines", departure_airport, arrival_airport),
]

# Filtering flights based on price
filtered_flights = Flight.filter_flights(flights, "price", 500)

# Print available flights
print_available_flights(filtered_flights)

# Collecting customer details
customer = Customer.input_customer_details()

# Selecting a flight from available options
selected_flight = select_flight(filtered_flights)

# Creating a booking
booking = Booking(customer, selected_flight)

# Adding meal and service options
meal = MealOption("Vegetarian Meal", 20)
service = AdditionalService("Extra Legroom", 50)

booking.add_meal_option(meal)
booking.add_additional_service(service)

# Confirming and printing booking details
booking.confirm_booking()
booking.print_booking_details()