balance = 1000

while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money") 
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        print(f"Current balance: ₹{balance}")
        
    elif choice == '2':
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print(f"₹{deposit} deposited successfully")
        print(f"New balance: ₹{balance}")
        
    elif choice == '3':
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"₹{withdraw} withdrawn successfully")
            print(f"New balance: ₹{balance}")
        else:
            print("Insufficient funds!")
            
    elif choice == '4':
        print("Thank you for using ATM!")
        break
        
    else:
        print("Invalid choice! Please select 1-4.")
