
def withdraw(balance):
    amount=float(input("Enter the no : "))
    if amount<=balance:
        balance-=amount
        print(f"Balance : {balance} Rs.")
    else:
        print(f"Your balance is only {balance} Rs.")    