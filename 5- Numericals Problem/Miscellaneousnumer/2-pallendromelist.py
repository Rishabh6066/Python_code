
l=[121,122,123,124,131,141,150,252]
pallendrome=[]
rev=0
for i in range(len(l)):
    temp=i
    rem=l[i]%10
    rev= rev * 10 +rem
    l[i]//=10
    pallendrome.append(l[i])

