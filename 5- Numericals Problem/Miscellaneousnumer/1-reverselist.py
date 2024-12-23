# each element reverse hona chahiye
l=[121,123,124,137,2141,1450,52]
rev_list=[]
for i in range(len(l)-1,-1,-1):
    rev_list.append(l[i])
print(f"Reversed list: {rev_list}")