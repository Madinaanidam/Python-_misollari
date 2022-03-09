A=int(input("A koeffisentning qiymatini kiriting: "))
B=int(input("B koeffisentning qiymatini kiriting: "))
C=int(input("C koeffisentning qiymatini kiriting: "))
D=B**2-4*A*C
if (D>0):
     print("x1= ", (-B+D**(1/2))/2*A)
     print("x1= ", (-B-D**(1/2))/2*A) 
if(D==0):
    print("x1=x2= ", -B/2*A)  
else:
    print("Tenglama yechimga ega emas!")