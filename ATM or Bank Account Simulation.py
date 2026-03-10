import os
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.file_name= f"{self.account_number}_transactions.txt"
        
        #create transaction file if it doesn't exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                file.write("Transaction History\n")
                
                
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"Deposited ${amount}")
            self.save_transaction(f"Deposited ${amount}")
        except ValueError as e:
            print("Error:", e)
            
            
    def withdraw(self, amount):
        try:
            if amount <=0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            
            self.balance -= amount
            print(f"Withdrew ${amount}")
            self.save_transaction(f"Withdrew ${amount}")
        except ValueError as e:
            print("Error:", e)
            
            
    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        
    def save_transaction(self, message):
        with open(self.file_name, "a") as file:
            file.write(message + "\n")
            
            
    def show_transaction_history(self):
        print("\n Transaction History:")
        try:
            with open(self.file_name, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No transaction history found.")
            
            
def main():
    print("Welcome to ATM simulation")
    
    name = input("Enter your name:")
    account_number = input("Enter your account number:")
    
    account = BankAccount(name, account_number)
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw:"))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            account.check_balance()
            
        elif choice == "4":
            account.show_transaction_history()
            
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":    main()