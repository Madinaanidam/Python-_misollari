from asyncio import log
from cmath import cos, e
from math import log1p, log2


x=int(input("Birinchi sonni kiriting= "))
y=int(input("Ikkinchi sonni kiriting= "))
a=(x+y)**2
b=(abs(y)+2)**(1/2)
c=x-((x*y)/((x**2/2)-5))
d=((1+cos((x+y)*(x+y)))/2)/((x+y)**(1/3))
f=abs(a+b-c)
h=log2(f)/log2(e)
f2=h+d
if(((1<=x)and(1<=y))and((x<=30)and(y<=30))):
    print("Natija= ", f2)
else:
    print("Kiritilgan sonlar qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")