from vehicle import SUV, LuxuryCar

class Rental:
    def __init__(self, rental_id, customer, vehicle, rental_days):
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

# storing actual customer object & vehicle object in the rental object
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.actual_days = None
        self.status = "ACTIVE"

# Polymorphism: calling the calculate_rental_cost method of the specific vehicle type
        self.base_cost = vehicle.calculate_rental_cost(rental_days)
        self.late_fee = 0
        self.damage_charge = 0

        self.__paid = False

    def calculate_late_fee(self):
        if self.actual_days is None:
            return 0

        late_days = self.actual_days - self.rental_days

        if late_days <= 0:
            return 0

        daily_late_penalty = self.vehicle.daily_rate * 0.20
        self.late_fee = daily_late_penalty * late_days

        return self.late_fee

    def calculate_total(self):
        return self.base_cost + self.late_fee + self.damage_charge

    def complete_rental(self, actual_days, damage_charge=0):
        if self.status == "COMPLETED":
            raise ValueError("This rental has already been completed.")

        if self.status == "CANCELLED":
            raise ValueError("A cancelled rental cannot be completed.")

        if actual_days <= 0:
            raise ValueError("Actual rental days must be greater than zero.")

        if damage_charge < 0:
            raise ValueError("Damage charge cannot be negative.")

        self.actual_days = actual_days
        self.damage_charge = damage_charge

        self.calculate_late_fee()

        self.status = "COMPLETED"

    def mark_as_paid(self):
        self.__paid = True

    def is_paid(self):
        return self.__paid

    def display_rental_details(self):
        print("\n====================================")
        print("        SAFARIDRIVE RENTALS")
        print("====================================")
        print(f"Rental ID:        {self.rental_id}")
        print(f"Customer:         {self.customer.name}")
        print(f"Vehicle:          {self.vehicle.make} {self.vehicle.model}")
        print(f"Registration:     {self.vehicle.registration_number}")
        print(f"Rental Period:    {self.rental_days} days")
        print(f"Daily Rate:       KSh {self.vehicle.daily_rate:,.2f}")

        print(f"\nRental Charge:    KSh {self.base_cost:,.2f}")
 
        if isinstance(self.vehicle, SUV):
            print("Service Charge:   KSh 2,000.00")

        elif isinstance(self.vehicle, LuxuryCar):
            insurance = self.vehicle.daily_rate * self.rental_days * 0.10
            print(f"Insurance (10%):  KSh {insurance:,.2f}")
    
        if self.late_fee > 0:
            print(f"Late Fee:         KSh {self.late_fee:,.2f}")

        if self.damage_charge > 0:
            print(f"Damage Charge:    KSh {self.damage_charge:,.2f}")

        print("------------------------------------")
        print(f"TOTAL:            KSh {self.calculate_total():,.2f}")
        print(f"Status:           {self.status}")
        print(f"Paid:             {'Yes' if self.is_paid() else 'No'}")
        print("====================================")