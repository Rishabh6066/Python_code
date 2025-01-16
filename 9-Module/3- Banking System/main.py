'''
Bank System:

1- check balance
2- Deposit money
3- Withdraw money
0- Exit

Default balance is 1000 Rs.
'''

print("---------Welcome to Bank--------")
print(f" 1- Check Balance\n 2- Deposit money\n 3- Withdraw money\n 0- Exit")

import check_balance,deposit_money,withdraw_money
bal=1000.00
ch=int(input("Enter your choice: "))

if ch==1:
    check_balance.check_balance(bal)

elif ch==2:
    deposit_money.deposite(bal)

elif ch==3:
    withdraw_money.withdraw(bal)

else:
    print("Thankyou for using our services")   

