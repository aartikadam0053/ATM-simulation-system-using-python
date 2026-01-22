# Store user details in a dictionary
user = {"name": "aarti", "pin": "965739", "balance": 5000.0}


# Function for valid PIN
def valid_pin():
    enter_pin = input("Enter your PIN: ")
    if enter_pin != user["pin"]:
        print("Incorrect PIN.")
        return False
    print(f"Welcome to your account, {user['name']}!")
    return True


# Function to check balance
def check_balance():
    print(f"Your current balance is: ₹{user['balance']}")


# Function to deposit money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        user["balance"] += amount
        print(f"₹{amount} deposited successfully.")
        print(f"New balance is: ₹{user['balance']}")
    else:
        print("Invalid deposit amount.")


# Function to withdraw money
def withdraw_money():
   amount = float(input("Enter amount to withdraw: "))

   if amount <= 0:
      print("Invalid withdrawal amount!")
   elif amount > user["balance"]:
       print("Insufficient balance! Withdrawal denied.")
       print(f"Available balance is: ₹{user['balance']}")
   else:
    user["balance"] -= amount
    print(f"₹{amount} withdrawn successfully.")
    print(f"Available balance is: ₹{user['balance']}")


# Main program
if valid_pin():
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if valid_pin():
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")