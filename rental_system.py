from vehicle import SUV, LuxuryCar, EconomyCar
from rental import Rental


class CarRentalSystem:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []

        self.__revenue = 0

    # -----------------------------
    # VEHICLE MANAGEMENT
    # -----------------------------

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def find_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle

        return None

    def show_available_vehicles(self):
        print(f"\nAVAILABLE VEHICLES")
        print("=" * 50)

        available_vehicles = [
            vehicle for vehicle in self.vehicles
            if vehicle.is_available()
        ]

        if not available_vehicles:
            print("No vehicles are currently available.")
            return

        for vehicle in available_vehicles:
            vehicle.display_details()
            print("-" * 50)

    def search_vehicles(self, vehicle_type=None, max_daily_rate=None):
        results = []

        for vehicle in self.vehicles:

            if not vehicle.is_available():
                continue

            if vehicle_type is not None:
                if vehicle_type.lower() == "suv":
                    if not isinstance(vehicle, SUV):
                        continue

                elif vehicle_type.lower() == "economy":
                    if not isinstance(vehicle, EconomyCar):
                        continue

                elif vehicle_type.lower() == "luxury":
                    if not isinstance(vehicle, LuxuryCar):
                        continue

                else:
                    continue

            if max_daily_rate is not None:
                if vehicle.daily_rate > max_daily_rate:
                    continue

            results.append(vehicle)

        return results

    # -----------------------------
    # CUSTOMER MANAGEMENT
    # -----------------------------

    def register_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    # -----------------------------
    # RENTAL MANAGEMENT
    # -----------------------------

    def rent_vehicle(self, customer, vehicle, days):

        if customer not in self.customers:
            raise ValueError(
                "Customer must be registered before renting."
            )

        if vehicle not in self.vehicles:
            raise ValueError(
                "Vehicle must be in the fleet before it is rented."
            )

        if not vehicle.is_available():
            raise ValueError(
                "Vehicle is currently unavailable."
            )

        if days <= 0:
            raise ValueError(
                "Rental days must be greater than zero."
            )

        rental_id = f"R{len(self.rentals) + 1:03d}"

        rental = Rental(
            rental_id,
            customer,
            vehicle,
            days
        )

        self.rentals.append(rental)
        customer.add_rental(rental)

        vehicle.mark_as_rented()

        return rental

    def return_vehicle(self, rental, actual_days, damage_charge=0):

        if rental not in self.rentals:
            raise ValueError(
                "Rental does not belong to this system."
            )

        if rental.status != "ACTIVE":
            raise ValueError(
                "This rental is not currently active."
            )

        rental.complete_rental(
            actual_days,
            damage_charge
        )

        rental.vehicle.mark_as_available()

    # -----------------------------
    # RENTAL VIEWING
    # -----------------------------

    def show_active_rentals(self):

        print("\nACTIVE RENTALS")
        print("=" * 50)

        active_rentals = [
            rental for rental in self.rentals
            if rental.status == "ACTIVE"
        ]

        if not active_rentals:
            print("No active rentals.")
            return

        for rental in active_rentals:
            rental.display_rental_details()

    def show_completed_rentals(self):

        print("\nCOMPLETED RENTALS")
        print("=" * 50)

        completed_rentals = [
            rental for rental in self.rentals
            if rental.status == "COMPLETED"
        ]

        if not completed_rentals:
            print("No completed rentals.")
            return

        for rental in completed_rentals:
            rental.display_rental_details()

    # -----------------------------
    # PAYMENT MANAGEMENT
    # -----------------------------

    def process_payment(self, payment):

        if payment.rental not in self.rentals:
            raise ValueError(
                "Rental does not belong to this system."
            )

        if payment.rental.status != "COMPLETED":
            raise ValueError(
                "A rental can only be paid after it is completed."
            )

        if payment.rental.is_paid():
            raise ValueError(
                "This rental has already been paid."
            )

        if payment.amount < 0:
            raise ValueError(
                "Payment amount cannot be negative."
            )

        success = payment.process_payment()

        if success:
            payment.rental.mark_as_paid()

            self.payments.append(payment)

            self.__revenue += payment.amount

        return success

    # -----------------------------
    # REVENUE
    # -----------------------------

    @property
    def revenue(self):
        return self.__revenue

    # -----------------------------
    # MANAGEMENT REPORT
    # -----------------------------

    def generate_report(self):

        total_vehicles = len(self.vehicles)

        available_vehicles = sum(
            1 for vehicle in self.vehicles
            if vehicle.is_available()
        )

        rented_vehicles = total_vehicles - available_vehicles

        total_customers = len(self.customers)

        total_rentals = len(self.rentals)

        active_rentals = sum(
            1 for rental in self.rentals
            if rental.status == "ACTIVE"
        )

        completed_rentals = sum(
            1 for rental in self.rentals
            if rental.status == "COMPLETED"
        )

        economy_cars = sum(
            1 for vehicle in self.vehicles
            if isinstance(vehicle, EconomyCar)
        )

        suvs = sum(
            1 for vehicle in self.vehicles
            if isinstance(vehicle, SUV)
        )

        luxury_cars = sum(
            1 for vehicle in self.vehicles
            if isinstance(vehicle, LuxuryCar)
        )

        print("\n=====================================")
        print("    SAFARIDRIVE MANAGEMENT REPORT")
        print("=====================================")

        print(f"Total Vehicles:              {total_vehicles}")
        print(f"Available Vehicles:          {available_vehicles}")
        print(f"Rented Vehicles:             {rented_vehicles}")

        print()

        print(f"Registered Customers:        {total_customers}")

        print()

        print(f"Total Rentals:               {total_rentals}")
        print(f"Active Rentals:              {active_rentals}")
        print(f"Completed Rentals:           {completed_rentals}")

        print()

        print(f"Total Revenue:        KSh {self.__revenue:,.2f}")

        print("-------------------------------------")
        print("VEHICLES BY CATEGORY")

        print(f"Economy Cars:                 {economy_cars}")
        print(f"SUVs:                         {suvs}")
        print(f"Luxury Cars:                  {luxury_cars}")

        print("=====================================")