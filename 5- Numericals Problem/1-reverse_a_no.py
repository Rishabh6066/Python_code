n=int(input("Enter the no."))
temp=n
reverse=0

while n!=0:
    rem= n % 10
    reverse= reverse * 10 + rem
    n=n//10

print(f"the reverse of {temp} is {reverse}")