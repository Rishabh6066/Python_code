
#create a heterogeneous list and one homogeneous list and print them  and also print length of each?


hetrogenous_list=[4,5,9,77,5,6,44,2]

homogeneous_list= [1,3,5.6,True,'abc','Ram',[4,5,8.9]]

print(f""" length of Homogeneous_list: {len(homogeneous_list)}
 length of Hetrogeneous_list: {len(hetrogenous_list)}""")

'''
l=[1,2,3,4,'d',6,7,'c',9,'a']
	write code to print using slicing 	
	1- 'd'
	2- 'c'
	3- 'a'

'''
l=[1,2,3,4,'d',6,7,'c',9,'a']

#print 'd' using slicing
print(l[4:5]) 

#print 'c' using slicing
print(l[7:8])

#print 'a' using slicing
print(l[9:])

'''
Make a dynamic app where user will input
	Name, Age, Matches, Runs, Avg, fifties, centuries, Batting Best, Overs, Wickets, Bowling Best of a cricketer 
	and create an interesting story of that user using this data of that cricketer .

'''
#user input

name=input("Enter the cricketer's name: ")
age=int(input("Enter age: "))
matches= int(input("Enter the Matches: "))
runs=int(input("Enter the Runs:"))
average=int(input("Enter the Average:"))
fifties=int(input("Enter the Fifties: "))
centuries=int(input("Enter the Centuries: "))
batting_best=int(input("Enter the Best Batting: "))
overs=int(input("Enter the Overs: "))
wickets=int(input("Enter the Wickets:"))
best_bowling=int(input("Enter the Best Bowling: "))

story=f"""f" Meet {name}, a remarkable cricketer aged {age}, who has taken the cricket world by storm. 
With an impressive career spanning {matches} matches, {name} has proven to be a formidable force on the field.

Batting Highlights: 
- Runs Scored: {runs} 
- Batting Average: {average} 
- Fifties: {fifties} 
- Centuries: {centuries} 
- Best Batting Performance: {batting_best}

Bowling Achievements: 
- Overs Bowled: {overs} 
- Wickets Taken: {wickets} 
- Best Bowling Performance: {best_bowling}

{name}'s dedication and hard work have made them a household name in cricket. 
Their ability to score runs and take wickets with ease has earned them a place among the greats. 
Whether smashing records with the bat or delivering crucial breakthroughs with the ball, 
{name} is a true cricketing legend.
" """
print(story)

