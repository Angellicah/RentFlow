class Customer:
    def __init__(self, customer_id, name, phone_number, national_id, driving_licence):# create a customer object
        if not driving_licence:
            raise ValueError("Customer must have a driving licence.")# enforce assignment's business rule

        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence
        self.rentals = [] # create empty list to store customer's rental objects

    def display_details(self):
        print("\n================================")
        print("       CUSTOMER DETAILS")
        print("================================")
        print(f"Customer ID:     {self.customer_id}")
        print(f"Name:            {self.name}")
        print(f"Phone Number:    {self.phone_number}")
        print(f"National ID:     {self.national_id}")
        print(f"Driving Licence: {self.driving_licence}")
        print(f"Total Rentals:   {len(self.rentals)}")
        print("================================")

    def add_rental(self, rental):
        self.rentals.append(rental) # add a rental to the customer's rental history

    def view_rental_history(self):
        print(f"\nRental History for {self.name}")
        print("--------------------------------")

        if not self.rentals:
            print("No rental history found.")
            return

        for rental in self.rentals:
            rental.display_rental_details()