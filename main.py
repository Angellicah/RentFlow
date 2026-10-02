from vehicle import EconomyCar, SUV, LuxuryCar
from customer import Customer
from rental_system import CarRentalSystem
from payment import MpesaPayment, CardPayment, CashPayment

#-----------------------------
# CREATE RENTAL SYSTEM
#-----------------------------

system = CarRentalSystem("SafariDrive Rentals")


# -----------------------------
# ADD VEHICLES
# -----------------------------

car1 = EconomyCar(
    "KDK 123A",
    "Toyota",
    "Axio",
    2022,
    4000
)

car2 = SUV(
    "KDJ 456B",
    "Toyota",
    "Prado",
    2023,
    8000
)

car3 = SUV(
    "KDJ 672B",
    "Nissan",
    "X-Trail",
    2021,
    6500
)

car4 = LuxuryCar(
    "KDL 789C",
    "Mercedes-Benz",
    "E-Class",
    2024,
    15000
)

car5 = EconomyCar(
    "KDM 321D",
    "Honda",
    "Fit",
    2023,
    3500
)

for car in [car1, car2, car3, car4, car5]:
    system.add_vehicle(car)


# -----------------------------
# REGISTER CUSTOMERS
# -----------------------------

customer1 = Customer(
    "C001",
    "John Kamau",
    "0712345678",
    "12345678",
    "DL45821"
)

customer2 = Customer(
    "C002",
    "Mary Wanjiku",
    "0723456789",
    "23456789",
    "DL56932"
)

customer3 = Customer(
    "C003",
    "Brian Otieno",
    "0734567890",
    "34567890",
    "DL67143"
)
for customer in [customer1, customer2, customer3]:
    system.register_customer(customer)


#-----------------------------
# SHOW AVAILABLE VEHICLES
#-----------------------------

print("\nAVAILABLE VEHICLES")
print("=" * 50)

system.show_available_vehicles()


# -----------------------------
# RENTAL1 - PRADO
# -----------------------------

rental1 = system.rent_vehicle(
    customer1,
    car2,
    4
)

print("\nRental 1 created successfully.")

# Customer returns after 6 days
system.return_vehicle(
    rental1,
    actual_days=6
)

print("Rental 1 completed.")

rental1.display_rental_details()


# ============================================
# RENTAL 2 - TOYOTA AXIO
# ============================================

rental2 = system.rent_vehicle(
    customer2,
    car1,
    3
)

print("\nRental 2 created successfully.")

# Customer returns on time
system.return_vehicle(
    rental2,
    actual_days=3
)

print("Rental 2 completed.")

rental2.display_rental_details()


# ============================================
# RENTAL 3 - MERCEDES-BENZ
# ============================================

rental3 = system.rent_vehicle(
    customer3,
    car4,
    2
)

print("\nRental 3 created successfully.")

# Customer returns on time
system.return_vehicle(
    rental3,
    actual_days=2
)

print("Rental 3 completed.")

rental3.display_rental_details()


#-----------------------------
# PROCESS PAYMENTS
#-----------------------------

# Rental 1 - M-Pesa
payment1 = MpesaPayment(
    rental1,
    "0712345678"
)

system.process_payment(payment1)


# Rental 2 - Card
payment2 = CardPayment(
    rental2,
    "4582"
)

system.process_payment(payment2)


# Rental 3 - Cash
payment3 = CashPayment(
    rental3,
    35000
)

system.process_payment(payment3)

#-----------------------------
# PAYMENT STATUS
#-----------------------------

print("\nPAYMENT STATUS")
print("=" * 50)

print(f"Rental {rental1.rental_id}: {'Paid' if rental1.is_paid() else 'Not Paid'}")
print(f"Rental {rental2.rental_id}: {'Paid' if rental2.is_paid() else 'Not Paid'}")
print(f"Rental {rental3.rental_id}: {'Paid' if rental3.is_paid() else 'Not Paid'}")

#-----------------------------
# CUSTOMER RENTAL HISTORY
#-----------------------------

customer1.view_rental_history()
customer2.view_rental_history()
customer3.view_rental_history()

#-----------------------------
# MANAGEMENT REPORT
#-----------------------------

system.generate_report()
