# RentFlow – Car Rental Management System

## Project Overview

**RentFlow** is a Python-based Car Rental Management System developed for **SafariDrive Rentals** as an Object-Oriented Programming (OOP) capstone project.

The system is designed to automate and manage the main operations of a car rental business, including vehicle management, customer registration, vehicle rentals, vehicle returns, late fee calculation, payment processing, rental history, and revenue tracking.

The project demonstrates the practical application of core Object-Oriented Programming principles in Python while solving a real-world business problem.

---

## Problem Statement

Managing car rentals manually can lead to several challenges, including:

- Difficulty tracking which vehicles are available or rented.
- Errors when assigning vehicles to customers.
- Difficulty maintaining customer rental records.
- Incorrect rental cost calculations.
- Challenges calculating late return penalties.
- Duplicate or invalid payments.
- Difficulty tracking business revenue.
- Lack of proper validation when customers rent or return vehicles.

SafariDrive Rentals requires a system that can organize these operations and enforce business rules consistently.

RentFlow provides a structured solution by using Python classes, objects, inheritance, abstraction, encapsulation, polymorphism, lists, validation, exception handling, and multiple modules.

---

## Project Objectives

The main objectives of RentFlow are to:

1. Manage the company's vehicle fleet.
2. Register customers and maintain their rental history.
3. Allow registered customers to rent available vehicles.
4. Prevent unavailable vehicles from being rented.
5. Calculate rental costs based on vehicle type.
6. Process different payment methods.
7. Calculate late return fees automatically.
8. Track completed and active rentals.
9. Prevent duplicate payments.
10. Track total business revenue.
11. Demonstrate the four major principles of Object-Oriented Programming.
12. Apply Python programming concepts to a realistic business problem.

---

# Key Features

## 1. Vehicle Management

The system allows SafariDrive Rentals to:

- Add vehicles to the fleet.
- Store vehicle registration numbers.
- Store vehicle make and model.
- Store vehicle year.
- Store daily rental rates.
- Track vehicle availability.
- Display vehicle information.
- Search for available vehicles by type.
- Search for vehicles using a maximum daily rate.

The system supports three vehicle categories:

- Economy Cars
- SUVs
- Luxury Cars

Each vehicle category has its own rental pricing rules.

---

## 2. Customer Management

Customers can be registered in the system using:

- Customer ID
- Name
- Phone number
- National ID
- Driving licence

The system validates that a customer has a driving licence before allowing registration.

Each customer also has a rental history that keeps track of the rentals associated with them.

---

## 3. Rental Management

The system allows registered customers to rent available vehicles.

When a rental is created, the system records:

- Rental ID
- Customer
- Vehicle
- Number of rental days
- Rental status
- Base rental cost
- Late fee
- Damage charge
- Payment status

The system automatically generates rental IDs such as:

- R001
- R002
- R003

A vehicle is automatically marked as rented when a rental is created.

---

## 4. Vehicle Returns

Customers can return rented vehicles through the system.

When a vehicle is returned, the system:

1. Checks that the rental belongs to the system.
2. Checks that the rental is currently active.
3. Records the actual number of days rented.
4. Calculates any applicable late fee.
5. Records any damage charge.
6. Marks the rental as completed.
7. Makes the vehicle available again.

This ensures that the vehicle's availability is always updated correctly.

---

# Rental Pricing Rules

RentFlow uses different pricing rules depending on the vehicle category.

## Economy Cars

For an Economy Car:

```text
Rental Cost = Daily Rate × Rental Days
```

For example:
A Toyota Axio costing KSh 4,000 per day rented for 3 days:

```text
4,000 × 3 = KSh 12,000
```

---

## SUVs

SUV rentals include a fixed KSh 2,000 service charge.

```text
Rental Cost = (Daily Rate × Rental Days) + KSh 2,000
```

For example:
A Toyota Prado costing KSh 8,000 per day rented for 4 days:

```text
8,000 × 4 = KSh 32,000
32,000 + 2,000 = KSh 34,000
```

Therefore:

```text
Base Cost = KSh 34,000
```

---

## Luxury Cars

Luxury vehicles include a 10% insurance charge.

```text
Rental Cost = Daily Rate × Rental Days
Insurance = 10% of Rental Cost
Total = Rental Cost + Insurance
```

For example:
A Mercedes-Benz E-Class costing KSh 15,000 per day rented for 2 days:

```text
15,000 × 2 = KSh 30,000
Insurance = 10% × 30,000 = KSh 3,000

Total = KSh 33,000
```

---

# Late Fee Calculation

RentFlow automatically calculates a late fee when a vehicle is returned after the agreed rental period.
The system first calculates the number of late days:

```text
Late Days = Actual Days - Agreed Rental Days
```

The late penalty is 20% of the vehicle's daily rate for every late day.

```text
Daily Late Penalty = Daily Rate × 20%

Late Fee = Daily Late Penalty × Late Days
```

### Example

A Toyota Prado has a daily rate of KSh 8,000.
The customer originally rented it for 4 days but returned it after 6 days.

```text
Agreed Days = 4
Actual Days = 6

Late Days = 6 - 4
          = 2 days

Daily Late Penalty = 8,000 × 20%
                   = KSh 1,600

Late Fee = 1,600 × 2
         = KSh 3,200
```

The original rental cost was:

```text
KSh 34,000
```

Therefore:

```text
Total = 34,000 + 3,200
      = KSh 37,200
```

---

# Payment Management

RentFlow supports multiple payment methods.
The system currently supports:

- M-Pesa
- Card
- Cash

Each payment method is represented by its own class.
Payments can only be processed after a rental has been completed.
The system also prevents the same rental from being paid more than once.

---

# Payment Methods

## M-Pesa Payment

The `MpesaPayment` class processes M-Pesa payments using the customer's phone number.
The system generates a transaction reference for the payment and confirms the transaction.
Example:

```text
Processing M-Pesa payment...
Phone Number: 0712345678
Transaction: XXXXXXXX
Payment of KSh 37,200.00 successful.
```

---

## Card Payment

The `CardPayment` class processes card payments.
Only the last four digits of the card are stored for demonstration purposes.
Example:

```text
Processing card payment...
Card ending 4582 charged KSh 12,000.00
Card payment successful.
```

---

## Cash Payment

The `CashPayment` class checks whether the customer has provided enough money.
If the amount is insufficient, the payment fails.
If the amount is sufficient, the system calculates the customer's change.
Example:

```text
Amount Due:     KSh 33,000
Cash Received:  KSh 35,000
Change Due:     KSh 2,000
```

---

# Object-Oriented Programming Concepts

One of the main objectives of RentFlow is to demonstrate the four major principles of Object-Oriented Programming:

1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

The project also demonstrates classes, objects, constructors, methods, properties, lists of objects, modules, `super()`, exception handling, and validation.

---

# 1. Abstraction

Abstraction means hiding unnecessary implementation details and exposing only the important functionality.
RentFlow demonstrates abstraction using Python's `ABC` and `@abstractmethod`.

The `Vehicle` class is an abstract base class.

```python
class Vehicle(ABC):
```

It contains an abstract method:

```python
@abstractmethod
def calculate_rental_cost(self, days):
    pass
```

This means that the general `Vehicle` class defines what every vehicle must be able to do, but does not define one single rental pricing calculation for all vehicle types.
Each specific vehicle type provides its own implementation.
For example:

```python
class EconomyCar(Vehicle):
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
```

The same principle is used in the payment system.
`Payment` is an abstract base class with:

```python
@abstractmethod
def process_payment(self):
    pass
```

The specific payment classes then implement their own payment processing behavior.

### Why abstraction is useful in RentFlow

Abstraction allows the system to work with general concepts such as:

```text
Vehicle
Payment
```

without requiring the rest of the system to know all the implementation details.
For example, the rental system does not need to know how M-Pesa, card, or cash payments work internally. It simply works with payment objects.

---

# 2. Encapsulation

Encapsulation means keeping data and the methods that operate on that data together while controlling access to important internal data.
RentFlow uses private attributes with double underscores.
Examples include:

```python
self.__available
```

inside the `Vehicle` class.
This attribute controls whether a vehicle is available for rental.
The system changes its value through methods such as `mark_as_rented()` and `mark_as_available()`.

Another example is:

```python
self.__paid
```

inside the `Rental` class.
The payment status is controlled using methods such as `mark_as_paid()` and `is_paid()`.

The system also uses:

```python
self.__revenue
```

inside `CarRentalSystem`.
Revenue is exposed through a read-only property:

```python
@property
def revenue(self):
    return self.__revenue
```

This prevents external code from directly modifying the revenue attribute.

### Why encapsulation is useful in RentFlow

Encapsulation helps protect important business information and ensures that changes happen through controlled methods.
For example, instead of directly changing:

```python
vehicle.__available
```

the system uses:

```python
vehicle.mark_as_rented()
```

This gives the program better control over the state of the vehicle.

---

# 3. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.
RentFlow uses inheritance extensively.
The main vehicle hierarchy is:

```text
Vehicle
├── EconomyCar
├── SUV
└── LuxuryCar
```

The child classes inherit common functionality from the `Vehicle` class.
For example:

```python
class SUV(Vehicle):
```

The child classes use:

```python
super().__init__(
    registration_number,
    make,
    model,
    year,
    daily_rate
)
```

The `super()` function calls the constructor of the parent class.
This avoids repeating common initialization code in every child class.
Similarly, the payment hierarchy is:

```text
Payment
├── MpesaPayment
├── CardPayment
└── CashPayment
```

Each payment type inherits from the abstract `Payment` class.

### Why inheritance is useful in RentFlow

Inheritance allows common functionality to be written once and reused.
For example, all vehicles have:

- Registration number
- Make
- Model
- Year
- Daily rate
- Availability

These common attributes are defined in `Vehicle`.
The individual vehicle classes only need to provide behavior that is different, such as their rental cost calculation.

---

# 4. Polymorphism

Polymorphism means that the same method or interface can behave differently depending on the object using it.
RentFlow demonstrates polymorphism through `calculate_rental_cost()`.

The method exists in the parent `Vehicle` class but behaves differently in each child class.
For example:

### EconomyCar

```python
def calculate_rental_cost(self, days):
    return self.daily_rate * days
```

### SUV

```python
def calculate_rental_cost(self, days):
    return (self.daily_rate * days) + 2000
```

### LuxuryCar

```python
def calculate_rental_cost(self, days):
    rental_charge = self.daily_rate * days
    insurance = rental_charge * 0.10
    return rental_charge + insurance
```

The rental system can simply call:

```python
vehicle.calculate_rental_cost(days)
```

without needing to know which specific type of vehicle it has received.
The correct method is automatically executed based on the object.
Polymorphism is also demonstrated through `process_payment()`.

The same method is implemented differently by:

- `MpesaPayment`
- `CardPayment`
- `CashPayment`

This allows the system to process different payment types using a common interface.

---

# Classes and Objects

RentFlow is built using several classes.

## Main Classes

### Vehicle

An abstract base class representing a general vehicle.

### EconomyCar

Represents economy vehicles.

### SUV

Represents sport utility vehicles.

### LuxuryCar

Represents luxury vehicles.

### Customer

Represents customers registered with SafariDrive Rentals.

### Rental

Represents a vehicle rental transaction.

### Payment

An abstract base class representing a general payment.

### MpesaPayment

Represents M-Pesa payments.

### CardPayment

Represents card payments.

### CashPayment

Represents cash payments.

### CarRentalSystem

Acts as the main management system that coordinates vehicles, customers, rentals, payments, and revenue.

---

# Objects

Objects are instances created from classes.
For example:

```python
car1 = EconomyCar(
    "KDK 123A",
    "Toyota",
    "Axio",
    2022,
    4000
)
```

Here, `car1` is an object of the `EconomyCar` class.
Similarly:

```python
customer1 = Customer(
    "C001",
    "John Kamau",
    "0712345678",
    "12345678",
    "DL45821"
)
```

creates a customer object.
A rental object is created when a customer rents a vehicle:

```python
rental1 = system.rent_vehicle(
    customer1,
    car2,
    4
)
```

This demonstrates how classes and objects work together to model real-world entities and transactions.

---

# Business Rules and Validation

RentFlow includes validation to prevent invalid operations.
The system enforces the following business rules:

1. Daily rental rates cannot be negative.
2. Customers must have a driving licence.
3. Customers must be registered before renting.
4. Vehicles must belong to the fleet before they can be rented.
5. Rental days must be greater than zero.
6. A vehicle that is already rented cannot be rented again.
7. A vehicle cannot be returned unless it is currently rented.
8. A completed rental cannot be completed again.
9. Damage charges cannot be negative.
10. Payment amounts cannot be negative.
11. Payments can only be made after a rental is completed.
12. A rental cannot be paid more than once.
13. Cash payments must contain enough money to cover the rental amount.

These rules help protect the system from inconsistent or invalid data.

---

# Error Handling

The system uses Python's exception handling mechanism through `try` and `except` when testing and handling invalid operations.
The classes also use `raise ValueError()` to stop invalid data from being accepted.
Examples include:

```python
raise ValueError("Daily rate cannot be negative.")
```

```python
raise ValueError("Customer must be registered before renting.")
```

```python
raise ValueError("This rental has already been paid.")
```

This makes the system safer and more reliable.

---

# Project Structure

The project is organized into separate Python modules.

```text
rentflow/
│
├── main.py
├── vehicle.py
├── customer.py
├── rental.py
├── payment.py
├── rental_system.py
└── README.md
```

---

# File Descriptions

## `vehicle.py`

Contains:

- `Vehicle`
- `EconomyCar`
- `SUV`
- `LuxuryCar`

Responsible for vehicle information, availability, pricing, abstraction, inheritance, and polymorphism.

---

## `customer.py`

Contains:

- `Customer`

Responsible for customer registration information and rental history.

---

## `rental.py`

Contains:

- `Rental`

Responsible for rental transactions, rental costs, late fees, damage charges, payment status, and rental completion.

---

## `payment.py`

Contains:

- `Payment`
- `MpesaPayment`
- `CardPayment`
- `CashPayment`

Responsible for payment processing and demonstrates abstraction, inheritance, and polymorphism.

---

## `rental_system.py`

Contains:

- `CarRentalSystem`

Responsible for managing:

- Vehicles
- Customers
- Rentals
- Payments
- Revenue
- Searches
- Management reports

---

## `main.py`

The main program that demonstrates how all the classes and modules work together.
It creates the sample vehicles, customers, rentals, and payments and generates the final management report.

---

## `README.md`

Contains the project documentation, including:

- Project overview
- Problem statement
- Objectives
- Features
- OOP concepts
- Pricing rules
- Business rules
- Project structure
- Testing
- Sample data
- Real-world application
- Future improvements

---

# Sample Data

The final demonstration uses five vehicles, three customers, and three rentals.

## Vehicles

| Registration | Make          | Model   | Type    | Year | Daily Rate |
| ------------ | ------------- | ------- | ------- | ---- | ---------- |
| KDK 123A     | Toyota        | Axio    | Economy | 2022 | KSh 4,000  |
| KDJ 456B     | Toyota        | Prado   | SUV     | 2023 | KSh 8,000  |
| KDJ 672B     | Nissan        | X-Trail | SUV     | 2021 | KSh 6,500  |
| KDL 789C     | Mercedes-Benz | E-Class | Luxury  | 2024 | KSh 15,000 |
| KDM 321D     | Honda         | Fit     | Economy | 2023 | KSh 3,500  |

---

# Sample Customers

| Customer ID | Name         | Phone Number |
| ----------- | ------------ | ------------ |
| C001        | John Kamau   | 0712345678   |
| C002        | Mary Wanjiku | 0723456789   |
| C003        | Brian Otieno | 0734567890   |

All sample customers have valid driving licences.

---

# Sample Rentals

## Rental 1

```text
Customer: John Kamau
Vehicle: Toyota Prado
Rental Period: 4 days
Actual Period: 6 days
Payment Method: M-Pesa
```

Calculation:

```text
Base rental cost = KSh 34,000
Late fee         = KSh 3,200
Total            = KSh 37,200
```

---

## Rental 2

```text
Customer: Mary Wanjiku
Vehicle: Toyota Axio
Rental Period: 3 days
Actual Period: 3 days
Payment Method: Card
```

Calculation:

```text
Total = KSh 12,000
```

---

## Rental 3

```text
Customer: Brian Otieno
Vehicle: Mercedes-Benz E-Class
Rental Period: 2 days
Actual Period: 2 days
Payment Method: Cash
```

Calculation:

```text
Rental charge = KSh 30,000
Insurance     = KSh 3,000
Total         = KSh 33,000
```

The customer pays KSh 35,000 in cash and receives:

```text
Change = KSh 2,000
```

---

# Payment Summary

The demonstration uses three different payment methods:

| Rental | Payment Method | Amount     |
| ------ | -------------- | ---------- |
| R001   | M-Pesa         | KSh 37,200 |
| R002   | Card           | KSh 12,000 |
| R003   | Cash           | KSh 33,000 |

Total successful revenue:

```text
KSh 37,200
+ KSh 12,000
+ KSh 33,000
----------------
KSh 82,200
```

Therefore, the final system revenue is:
**KSh 82,200.00**

---

# Management Report

At the end of the demonstration, the system generates a management report containing:

```text
Total Vehicles
Available Vehicles
Rented Vehicles
Registered Customers
Total Rentals
Active Rentals
Completed Rentals
Total Revenue
Vehicles by Category
```

The final demonstration produces:

```text
Total Vehicles:              5
Available Vehicles:          5
Rented Vehicles:             0

Registered Customers:        3

Total Rentals:               3
Active Rentals:              0
Completed Rentals:           3

Total Revenue:        KSh 82,200.00
```

Vehicle categories:

```text
Economy Cars:  2
SUVs:          2
Luxury Cars:   1
```

---

# Testing Performed

The system was tested against both normal and invalid operations.

## Successful Tests

- Creating an Economy Car.
- Creating an SUV.
- Creating a Luxury Car.
- Displaying vehicle details.
- Checking vehicle availability.
- Registering customers.
- Creating rentals.
- Returning vehicles.
- Calculating normal rental charges.
- Calculating SUV service charges.
- Calculating luxury insurance.
- Calculating late fees.
- Processing M-Pesa payments.
- Processing card payments.
- Processing successful cash payments.
- Calculating cash change.
- Recording revenue.
- Generating management reports.
- Displaying customer rental history.


## Class Diagram

![RentFlow UML Class Diagram](RentFlow_Class_Diagram.png)

## Validation Tests

The following invalid operations were also tested:

- Negative daily rental rate.
- Missing driving licence.
- Renting with an unregistered customer.
- Renting a vehicle that is not in the fleet.
- Renting an unavailable vehicle.
- Rental period of zero days.
- Negative damage charge.
- Returning an invalid rental.
- Completing an already completed rental.
- Paying before returning the vehicle.
- Paying the same rental twice.
- Negative payment amount.
- Insufficient cash payment.

These tests demonstrate that the system does not only handle successful scenarios but also protects against invalid business operations.

---

# Technologies Used

The project was developed using:

- **Python 3**
- **Visual Studio Code**
- **Object-Oriented Programming**
- **Python Abstract Base Classes**
- **Exception Handling**
- **Python Modules**
- **Lists and Objects**

No external Python packages are required to run the core system.

---

# Real-World Problem Solved

RentFlow represents a simplified version of a real car rental management system.
In a real rental company, employees need to know:

- Which vehicles are available.
- Which vehicles are currently rented.
- Who rented each vehicle.
- How long the vehicle was rented.
- How much the customer should pay.
- Whether the customer returned the vehicle late.
- Whether additional charges apply.
- Whether a rental has already been paid.
- How much revenue the business has generated.

RentFlow models these processes using Python classes and objects.
The project therefore demonstrates how Object-Oriented Programming can be used to represent real-world entities such as:

```text
Vehicles
Customers
Rentals
Payments
```

and how these entities can interact with one another within a business system.

---

# Why Object-Oriented Programming Fits This System

Car rental businesses involve many entities that have their own information and behaviors.
For example:
A vehicle has:

```text
Registration
Make
Model
Year
Daily Rate
Availability
```

and can:

```text
Calculate Rental Cost
Be Rented
Become Available
Display Details
```

A customer has:

```text
Customer ID
Name
Phone Number
National ID
Driving Licence
Rental History
```

A rental has:

```text
Rental ID
Customer
Vehicle
Rental Days
Actual Days
Late Fee
Damage Charge
Payment Status
```

A payment has:

```text
Rental
Amount
Payment Method
```

Using classes makes it easier to represent these real-world concepts in code and organize their behavior.

---

# Future Improvements

The current system focuses on demonstrating the required OOP concepts. Possible future improvements include:

1. Interactive command-line menus.
2. Automatic date and time tracking.
3. Vehicle maintenance records.
4. Damage assessment.
5. Customer discounts.
6. Rental cancellation functionality.
7. Rental extensions.
8. Search by vehicle model.
9. Persistent storage using JSON or SQLite.
10. Database integration.
11. User authentication.
12. Administrative dashboards.
13. Printable invoices and receipts.
14. Automated reporting.
15. Graphical user interface.
16. Web-based version of the system.

---

# Conclusion

RentFlow demonstrates how Python Object-Oriented Programming can be applied to solve a practical business problem.
The project implements the four major OOP principles:

```text
Abstraction
Encapsulation
Inheritance
Polymorphism
```

It also demonstrates:

- Classes and objects
- Constructors
- Methods
- Abstract classes
- Abstract methods
- `super()`
- Private attributes
- Properties
- Lists of objects
- Multiple Python modules
- Validation
- Exception handling
- Business rules

The system successfully manages vehicles, customers, rentals, returns, payments, late fees, rental history, and revenue.
The completed demonstration uses:

```text
5 Vehicles
3 Customers
3 Rentals
3 Payment Methods
KSh 82,200 Total Revenue
```

Overall, RentFlow provides a structured example of how Object-Oriented Programming can be used to build a maintainable and realistic business management application.

---

# Author
Angellicah.W.M

Developed as an Object-Oriented Programming project using Python.

**Project:** RentFlow – Car Rental Management System
**Company:** SafariDrive Rentals