basic=[[0,'s1',8],[0,'s2',10],[0,'s3',15]]
base=[[2,3,0,1,0,0],[0,2,5,0,1,0],[3,2,4,0,0,1]]
cj=[3,5,4,0,0,0]
ratio=[8,10,15]
#iteration 1
zj=[0,0,0,0,0,0]
cjzj=[0,0,0,0,0,0]
count=1
while(1):
	print("ITERATION ",count)
	for i in range(6):
		t=0
		for j in range(3):
			t+=(base[j][i]*basic[j][0])
		zj[i]=t

	for i in range(6):
		cjzj[i]=cj[i]-zj[i]
 	print("cjzj ",cjzj)
	indr=-1
	indr=cjzj.index(max(cjzj))
	print('max Cj-Zj containing index ',indr)
	temp=[]
	for i in range(3):
		if(base[i][indr]==0):
			t=99999999	
		else:
			t=ratio[i]/float(base[i][indr])
		temp.append(t)
	
	indc=temp.index(min(temp))
	print("Min ratio index ",indc)
	ind=-1
	m=-8978989
	for i in range(3):
		if(base[i][indr]>m):
			m=base[i][indr]
			ind=i
	t=base[ind][indr]				
	for i in range(6):
		if(t==0):
			base[ind][i]=0
		else:
			base[ind][i]=base[ind][i]/float(t)
	if(t==0):
		ratio[ind]=0
	else:		
		ratio[ind]=ratio[ind]/float(t)	
	g=base[ind][indr]
	basic[ind][2]=basic[ind][2]/float(t)
	for j in range(6):
		base[ind][j]=base[ind][j]/g
	for i in range(3):
		if(i==ind):
			continue
		else:
			p=base[i][indr]/base[ind][indr]
		for j in range(6):
			base[i][j]-=(base[ind][j]*p)
		basic[i][2]-=(basic[ind][2]*p)
		ratio[i]-=(ratio[ind]*p)	
	ratio[ind]=99999999
	print("After iteration ",count)
	print("Base table is  ")	
	for i in range(3):
		print(base[i])	
	print("Xb/Xi ",ratio)
	basic[ind][0]=cj[indr]	
	indr+=1
	basic[ind][1]='x'+str(indr)
	print("[Cb B b]",basic)	
	m=max(cjzj)
	if(m<=0):
		break
	count+=1
	print(".............................................................")
res=0
for i in range(3):
	res+=basic[i][0]*basic[i][2]
print("Max result is ",res)	



	
						
