# -*- coding: utf-8 -*-

"""
 White-box code examples.
"""
import re


def is_even(num):
    """
    Checks if a number is even.
    """
    return num % 2 == 0


def divide(a, b):
    """
    Simple division function.
    """
    result = 0
    if b != 0:
        result = a / b
    return result


def get_grade(score):
    """
    Grade function.
    """
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade


def is_triangle(a, b, c):
    """
    Determines if 3 numbers can form a triangle.
    """
    if a + b > c and a + c > b and b + c > a:
        return "Yes, it's a triangle!"

    return "No, it's not a triangle."


# 1
def check_number_status(number):
    """
    Checks if a given number is positive, negative, or zero.
    """
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


# 2
def validate_password(password):
    """
    Validates user passwords.
    """
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter,
    # one digit, and one special character.
    if (
        not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"\d", password)
        or not re.search(r"[!@#$%&]", password)
    ):
        return False

    return True


# 3
def calculate_total_discount(total_amount):
    """
    Calculates the discount for a customer's purchase based on the total amount.
    """
    if total_amount < 100:
        return 0

    if 100 <= total_amount <= 500:
        return 0.1 * total_amount

    return 0.2 * total_amount


# 4
def calculate_order_total(items):
    """
    Processes user orders in an e-commerce system.
    The function calculates the total price of the items in the order,
    applying different discounts based on the quantity of each item.
    """
    total_price = 0

    for item in items:
        quantity = item["quantity"]
        price_per_item = item["price"]

        # Apply discounts based on quantity
        if 1 <= quantity <= 5:
            total_price += quantity * price_per_item
        elif 6 <= quantity <= 10:
            total_price += 0.95 * quantity * price_per_item  # 5% discount
        else:
            total_price += 0.9 * quantity * price_per_item  # 10% discount

    return total_price


# 5
def calculate_items_shipping_cost(items, shipping_method):
    """
    Calculates shipping costs for an online shopping system.
    The function calculates shipping costs based on the total weight of the
    items in the order and the shipping method chosen by the customer.
    """
    total_weight = sum(item["weight"] for item in items)

    if shipping_method == "standard":
        if total_weight <= 5:
            return 10

        if 5 < total_weight <= 10:
            return 15

        return 20

    if shipping_method == "express":
        if total_weight <= 5:
            return 20

        if 5 < total_weight <= 10:
            return 30

        return 40

    raise ValueError("Invalid shipping method")


# 6
def validate_login(username, password):
    """
    Validates user login credentials.
    """
    if 5 <= len(username) <= 20 and 8 <= len(password) <= 15:
        return "Login Successful"

    return "Login Failed"


# 7
def verify_age(age):
    """
    Determines whether a person is eligible for a certain service based on their age.
    """
    if 18 <= age <= 65:
        return "Eligible"

    return "Not Eligible"


# 8
def categorize_product(price):
    """
    Determines the price category of a product based on its price.
    """
    if 10 <= price <= 50:
        return "Category A"

    if 51 <= price <= 100:
        return "Category B"

    if 101 <= price <= 200:
        return "Category C"

    return "Category D"


# 9
def validate_email(email):
    """
    Validates email addresses.
    """
    if 5 <= len(email) <= 50 and "@" in email and "." in email:
        return "Valid Email"

    return "Invalid Email"


# 10
def celsius_to_fahrenheit(celsius):
    """
    Converts temperatures from Celsius to Fahrenheit.
    """
    if -100 <= celsius <= 100:
        return (celsius * 9 / 5) + 32

    return "Invalid Temperature"


# 11
def validate_credit_card(card_number):
    """
    Validates credit card numbers.
    """
    if 13 <= len(card_number) <= 16 and card_number.isdigit():
        return "Valid Card"

    return "Invalid Card"


# 12
def validate_date(year, month, day):
    """
    Validates dates.
    """
    if 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
        return "Valid Date"

    return "Invalid Date"


# 13
def check_flight_eligibility(age, frequent_flyer):
    """
    Checks the eligibility of a passenger to book a flight.
    """
    if 18 <= age <= 65 or frequent_flyer:
        return "Eligible to Book"

    return "Not Eligible to Book"


# 14
def validate_url(url):
    """
    Validates URLs.
    """
    if len(url) <= 255 and url.startswith("http://") or url.startswith("https://"):
        return "Valid URL"

    return "Invalid URL"


# 15
def calculate_quantity_discount(quantity):
    """
    Calculates discounts based on the quantity of a product.
    """
    if 1 <= quantity <= 5:
        return "No Discount"

    if 6 <= quantity <= 10:
        return "5% Discount"

    return "10% Discount"


# 16
def check_file_size(size_in_bytes):
    """
    Checks if the size is valid for a file.
    """
    if 0 <= size_in_bytes <= 1048576:  # 1 MB in bytes
        return "Valid File Size"

    return "Invalid File Size"


# 17
def check_loan_eligibility(income, credit_score):
    """
    Checks if and which loan can be granted based on the income and credit score.
    """
    if income < 30000:
        return "Not Eligible"

    if 30000 <= income <= 60000:
        if credit_score > 700:
            return "Standard Loan"

        return "Secured Loan"

    if credit_score > 750:
        return "Premium Loan"

    return "Standard Loan"


# 18
def calculate_shipping_cost(weight, length, width, height):
    """
    Calculates the shipping cost based on the package weight and dimensions.
    """
    if weight <= 1 and length <= 10 and width <= 10 and height <= 10:
        return 5

    if (
        1 < weight <= 5
        and 11 <= length <= 30
        and 11 <= width <= 30
        and 11 <= height <= 30
    ):
        return 10

    return 20


# 19
def grade_quiz(correct_answers, incorrect_answers):
    """
    Grades online quizzes based on the number of correct and incorrect answers.
    """
    if correct_answers >= 7 and incorrect_answers <= 2:
        return "Pass"

    if correct_answers >= 5 and incorrect_answers <= 3:
        return "Conditional Pass"

    return "Fail"


# 20
def authenticate_user(username, password):
    """
    Authenticates users based on their username and password.
    """
    if username == "admin" and password == "admin123":
        return "Admin"

    if len(username) >= 5 and len(password) >= 8:
        return "User"

    return "Invalid"


# 21
def get_weather_advisory(temperature, humidity):
    """
    Provides weather advisories based on temperature and humidity.
    """
    if temperature > 30 and humidity > 70:
        return "High Temperature and Humidity. Stay Hydrated."

    if temperature < 0:
        return "Low Temperature. Bundle Up!"

    return "No Specific Advisory"


# 22
class VendingMachine:
    """
    A simple vending machine that dispenses drinks.
    It has two states: "Ready" and "Dispensing."
    """

    def __init__(self):
        """
        Defines the vending machine initial state.
        """
        self.state = "Ready"

    def insert_coin(self):
        """
        Function called when a coin is inserted.
        """
        if self.state == "Ready":
            self.state = "Dispensing"
            return "Coin Inserted. Select your drink."

        return "Invalid operation in current state."

    def select_drink(self):
        """
        Function called after selecting a drink.
        """
        if self.state == "Dispensing":
            self.state = "Ready"
            return "Drink Dispensed. Thank you!"

        return "Invalid operation in current state."


# 23
class TrafficLight:
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """

    def __init__(self):
        """
        Defines the traffic light initial state.
        """
        self.state = "Red"

    def change_state(self):
        """
        Function that changes the traffic light state.
        """
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def get_current_state(self):
        """
        Provides the current traffic light state.
        """
        return self.state


# 24
class UserAuthentication:
    """
    A user authentication system with states "Logged Out" and "Logged In."
    """

    def __init__(self):
        """
        Defines the user initial state.
        """
        self.state = "Logged Out"

    def login(self):
        """
        Function to login a user.
        """
        if self.state == "Logged Out":
            self.state = "Logged In"
            return "Login successful"

        return "Invalid operation in current state"

    def logout(self):
        """
        Function to logout a user.
        """
        if self.state == "Logged In":
            self.state = "Logged Out"
            return "Logout successful"

        return "Invalid operation in current state"


# 25
class DocumentEditingSystem:
    """
    A document editing system with states "Editing" and "Saved."
    """

    def __init__(self):
        """
        Defines the initial state.
        """
        self.state = "Editing"

    def save_document(self):
        """
        Function to save a document.
        """
        if self.state == "Editing":
            self.state = "Saved"
            return "Document saved successfully"

        return "Invalid operation in current state"

    def edit_document(self):
        """
        Function to edit a document.
        """
        if self.state == "Saved":
            self.state = "Editing"
            return "Editing resumed"

        return "Invalid operation in current state"


# 26
class ElevatorSystem:
    """
    An elevator system with states "Idle," "Moving Up," and "Moving Down."
    """

    def __init__(self):
        """
        Defines the elevator initial state.
        """
        self.state = "Idle"

    def move_up(self):
        """
        Function to move up the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Up"
            return "Elevator moving up"

        return "Invalid operation in current state"

    def move_down(self):
        """
        Function to move down the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Down"
            return "Elevator moving down"

        return "Invalid operation in current state"

    def stop(self):
        """
        Function to stop the elevator.
        """
        if self.state in ["Moving Up", "Moving Down"]:
            self.state = "Idle"
            return "Elevator stopped"

        return "Invalid operation in current state"


# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        print(f"The account {self.account_number} has a balance of {self.balance}")


class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True


# 28
class Product:  # pylint: disable=too-few-public-methods
    """
    Product class.
    """

    def __init__(self, name, price):
        """
        Set the product details.
        """
        self.name = name
        self.price = price

    def view_product(self):
        """
        Function to display the product details.
        """
        print(f"The product {self.name} has a price of {self.price}")


class ShoppingCart:
    """
    Shopping cart class.
    """

    def __init__(self):
        """
        Initialize the shopping cart.
        """
        self.items = []

    def add_product(self, product, quantity=1):
        """
        Function to add a product to the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product, quantity=1):
        """
        Function to remove a product from the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.items.remove(item)
                else:
                    item["quantity"] -= quantity
                break

    def view_cart(self):
        """
        Function to display the shopping cart content.
        """
        for item in self.items:
            print(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def checkout(self):
        """
        Function to checkout the items from the shopping cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        print(f"Total: ${total}")
        print("Checkout completed. Thank you for shopping!")
