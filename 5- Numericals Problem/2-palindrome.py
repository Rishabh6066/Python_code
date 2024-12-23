# revere of any no. or string is same as it given
# 121 = 121

n=int(input("Enter the no."))
temp=n
reverse=0

while n!=0:
    rem=n% 10
    reverse= reverse * 10 + rem
    n//=10
if temp == reverse:
    print("the numer is palendrom")
else:
    print("the no. is not pallendrome")     