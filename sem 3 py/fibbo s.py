nterms =int(input("how many no..? "))
n1 ,n2 =0 , 1
if nterms <=0:
    print("positive no..")
elif nterms ==1:
    print(n1)    
else:
    print("fibbo sequence")    
    print(n1,n2)
    for i in range(3,nterms+1):
         nth =n1 +n2
         print(nth)
         n1=n2n2=nth

