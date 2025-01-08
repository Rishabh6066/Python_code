'''
1) l=[1,3,('a','v',[1,9,'Mark',66,(22,"Zakurberg","l"),-3]),[44,7,1,[45,('W'),4,93],77,90]] 

o/p: Mark W Zakurberg	

2) The Treasure Hunt Map

 You’re part of a team searching for a hidden treasure on an island. 

 The map you have is in the form of a list of coordinates (x, y). 

 However, some coordinates are incomplete or contain errors, such as strings instead of integers. 

 Your task is to count how many valid coordinates are provided and which ones are usable for your search.

 coordinates = [(1, 2), (3, "4"), ("5", 6), (7, 8), ("10", "11"), (9, 10)]

3) Find the greatest smallest and the middle from nos given by user

4) Write a lambda function to filter nos. greater than 20 [1,7,30,20,32,60,3,7,19,21,47]

5) data ={'1/1/2024':100,'2/1/2024':200,'3/1/2024':50,'4/1/2024':300,'5/1/2024':400,'6/1/2024':500,'7/1/2024':80}

	write the functions best buying date and best selling date and print max profit
'''
l=[1,3,('a','v',[1,9,'Mark',66,(22,"Zakurberg","l"),-3]),[44,7,1,[45,('W'),4,93],77,90]] 

#o/p: Mark W Zakurberg

#print(f'{l[2][2][2]} {[3][3][0]} {[2][4][1]}')
print(f'{l[2][2][2]} {l[3][3][1][0]} {l[2][2][4][1]}')

numbers = [1, 7, 30, 20, 32, 60, 3, 7, 19, 21, 47]


#4 Write a lambda function to filter nos. greater than 20 [1,7,30,20,32,60,3,7,19,21,47]

numbers=[1,7,30,20,32,60,3,7,19,21,47]
filtered_numbers = list(filter(lambda x: x > 20, numbers))

print(filtered_numbers)

#5 find the greatest smallest and middle  from no. given by user

a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
c=int(input("Enter thrid no: "))

if a >= b and a >= c:
    print(f"a: {a} is greatest")
    if b >= c:
        print(f"b: {b} is middle")
        print(f"c: {c} is smallest")
    else:
        print(f"c: {c} is middle")
        print(f"b: {b} is smallest")
        
elif b >= a and b >= c:
    print(f"b: {b} is greatest")
    if a >= c:
        print(f"a: {a} is middle")
        print(f"c: {c} is smallest")
    else:
        print(f"c: {c} is middle")
        print(f"a: {a} is smallest")
else:
    print(f"c: {c} is greatest")
    if a >= b:
        print(f"a: {a} is middle")
        print(f"b: {b} is smallest")
    else:
        print(f"b: {b} is middle")
        print(f"a: {a} is smallest")


#2 
coordinates = [(1, 2), (3, "4"), ("5", 6), (7, 8), ("10", "11"), (9, 10)] 
valid_co=[]

for c in coordinates:
    if (type(c[0])==int) and (type(c[1])==int):
        valid_co.append(c)

print(f"No. of valid coordinates : {len(valid_co)}")
print(f"Valid coordinates : {valid_co}")        

#5

data = {
    '1/1/2024': 100,
    '2/1/2024': 200,
    '3/1/2024': 50,
    '4/1/2024': 300,
    '5/1/2024': 400,
    '6/1/2024': 500,
    '7/1/2024': 80
}

def buy_sell(data):
    dates = list(data.keys())
    price= list(data.values())
    max_profit=0
    buy_date = None
    sell_date= None
    for i in range(len(price)):
        for j in range(i+1,len(price)):
             profit = price[j] - price[i]
             if profit>max_profit:
                  max_profit=profit
                  buy_date=dates[i]
                  sell_date=dates[j]
        return buy_date,sell_date,max_profit

a,b,c=(buy_sell(data))
print(a,b,c)   
          
       
        
    
'''Extra question'''
data={
    "Match 1": 50,
    "Match 2": 100,
    "Match 3": 15,
    "Match 4": 75,
    "Match 5": 39,
}

# best score ,
# lowest score,
# total score in series,
# best match,
# avg of series,
#total fifties and centuries
# Matches scored 50 or more than 50

'''for x,y in data.items():
    print(x,y)
    for x,y in data'''
#Another method

matches=list(data.keys())
scores=list(data)

# best score, 

best_score=0

for x in range(len(scores)):
        if best_score<scores[x]:
            best_score=scores[x]
print(best_score)

# lowest score, 

lowest_score=data["Match 1"]
for x in range(len(scores)):
        if lowest_score>scores[x]:
            lowest_score=scores[x]
print(lowest_score)

# total score in series,

total_score=0
for x in range(len(scores)):
     total_score += scores[x]
print(total_score)

# best match

for match,score in data.items():
     if score==best_score:
          best_match=match
print(best_match)

# avg of series,

avg_score=total_score/len(data)
print(avg_score)

# Total fifties and centuries,

fifties=0
centuries=0
for x in scores:
    if x>=50 and x<100:
          fifties+=1
    elif x>=100:
         centuries+=1
print("fifties:",fifties,"centuries:",centuries)

 

# Matches scored 50 or more than 50

matches_50_plus=[]
for match,score in data.items():
     if score>=50:
          matches_50_plus.append(match)

print("matches score 50 and more")
for x in matches_50_plus:
   print(x)