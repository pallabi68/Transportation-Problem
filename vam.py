import sys
import numpy as np
requirement=[25,35,105,20]
availability=[50,70,30,50]
cost=[[4,6,8,13],[13,11,10,8],[14,4,10,13],[9,11,13,8]]

r=4
c=4
total_requirement=0
total_availability=0
def p_cost(cost):
	for i in range(r):
		print(cost[i])
for i in range(0,len(requirement)):
	total_requirement+=requirement[i]
	
for i in range(0,len(availability)):
	total_availability+=availability[i]
	
if(total_requirement <	total_availability):
	for i in range(r):
		cost[i].append(0)
	requirement.append(total_availability-total_requirement)
	c+=1
if(total_requirement > total_availability):
	temp=[0]*c	
	cost.append(temp)
	availability.append(total_requirement-total_availability)
	r+=1
df=np.zeros((r,c))	
print("Updated cost matrix ")
print(cost)
res=0
while(total_requirement >0):
	row=[float('-inf')]*r
	col=[float('-inf')]*c
	
	for i in range(r):
		mi=sys.maxsize
		ma=float('-inf')
		for j in range(c):
			if(cost[i][j]!=sys.maxsize):
				ma=max(ma,cost[i][j])
				mi=min(mi,cost[i][j])
		row[i]=ma-mi
	for j in range(c):
		mi=sys.maxsize
		ma=float('-inf')
		for i in range(r):
			if(cost[i][j]!=sys.maxsize):
				ma=max(ma,cost[i][j])
				mi=min(mi,cost[i][j])
			
		col[j]=ma-mi
	print("Calculated value of diff in max and min element in a row ",row)
	print("Calculated value of diff in max and min element in a col",col)
	ma=max(row)
	ma=max(ma,max(col))
	rind=-1
	cind=-1
	if(ma in row):
		rind=row.index(max(row)) 
		cind=cost[rind].index(min(cost[rind]))		
	else:
		cind=col.index(max(col))
		temp=[]
		for i in range(r):
			temp.append(cost[i][cind])
		rind=temp.index(min(temp))
	print("Index choosen ",rind,cind)
	diff=min(availability[rind],requirement[cind])
	print("Allocated value to the index ",diff)
	res+=(cost[rind][cind]*diff)
	df[rind][cind]=diff
	if(diff==availability[rind]):
		for j in range(c):
			cost[rind][j]=sys.maxsize
	else:
		for i in range(r):
			
			cost[i][cind]=sys.maxsize
					
	total_requirement-=diff
	availability[rind]-=diff
	requirement[cind]-=diff
	#p_cost(cost)
	
	
print("Total cost of transportation is ",res)
print("Initial basic feasible solution is ")
print(df)	
				
			
					
					
		
		
		
		
		
		
		
		
		
		
		
		
			
						
	
				
		
	
