a=input('enter  password:')

def checkPassword(a):
    c=0
    b=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    d=('abcdefghijklmnopqrstuvwxyz')
    e=('123456789')
    st1=0
    st2=0
    st3=0

#checks character length
    for i in a:
        c+=1
    if c<10:
        pass
 #checks for capital letters  
    for i in a:
        if i in b:
            pass
        else:
            st=False

 #checks for lower cap letters  
    for i in a:
        if i in d:
            pass
        else:
            st2=False
 
#checks for numbers  

    for i in a:
        if i in e:
            pass
        else:
            st3=False

    if st==False and st2==False and st3==False and c<10:
        print('Weak password')
    else:
        print('Strong password')
checkPassword(a)        
    
