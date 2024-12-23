#logical operators: and , or ,not

#T and T= T  F and T=F  T and F =F F and F= F

a=4
b=3

print(a>b and b==3) #True
print(a>b and b!=3) #false
print(a<b and b==3) #false
print(a<b and b!=3) #false

# T or T =T  F or T =T  T or F=T F or F=F

print(a>b and b==3)  #True
print(a>b and b!=3) #True
print(a<b and b==3) #True
print(a<b and b!=3) #False

# not T = F  not F= T

print(not a>b) #f
print(not a<b) #T
print(not a!=3) #T

print(not(a>b and b==3)) # n(T and T)= n(t)=f
print(not(a>b or b!=3)) # n(t and f)= n(t)=f
