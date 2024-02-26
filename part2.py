f=open("/home/xbold7/Downloads/ITCWK2/IT CWK2/preferences.txt",'r')

a = f.readlines(1)
f1 = f.readlines(2)
f2 = f.readlines(3)
f3 = f.readlines(4)
f4 = f.readlines(5)
def strips(x,y=[]):
    for i in x:
        if i.strip():
            y.append(i)
            x=y
    return x


for i in a:
		friends0= i.split(", ")
for i in f1:
		friends1= i.split(", ")
for i in f2:
		friends2= i.split(", ")
for i in f3:
		friends3= i.split(", ")
for i in f4:
		friends4= i.split(", ")




a=(friends0[0])
f1=(friends1[0])
f2=(friends2[0])
f3=(friends3[0])
f4=(friends4[0])
friend1=('Friend 1')
friend2=('Friend 2')
friend3=('Friend 3')
friend4=('Friend 4')
a1=strips(a)



def cal(x,y,z):
    c=0
    for i in x:
        if i in y:
            c+=1
    print(z+' shares '+str(c)+' preferences\n')



cal(a1,f1,friend1)
cal(a1,f2,friend2)
cal(a1,f3,friend3)
cal(a1,f4,friend4)











