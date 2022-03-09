from calendar import c


x1=int(input("Uchburchakning birinchi nuqtaning birinchi kordinatasini kiriting: "))
y1=int(input("Uchburchakning birinchi nuqtaning ikkinchi kordinatasini kiriting: "))
x2=int(input("Uchburchakning ikkinchi nuqtaning birinchi kordinatasini kiriting: "))
y2=int(input("Uchburchakning ikkinchi nuqtaning ikkinchi kordinatasini kiriting: "))
x3=int(input("Uchburchakning uchunchi nuqtaning birinchi kordinatasini kiriting: "))
y3=int(input("Uchburchakning uchunchi nuqtaning ikkinchi kordinatasini kiriting: "))
a=((x2-x1)**2+(y2-y1)**2)**(1/2)
b=((x3-x2)**2+(y3-y2)**2)**(1/2)
c=((x3-x1)**2+(y3-y1)**2)**(1/2)
P=a+b+c
p=P/2
S=(p*(p-a)*(p-b)*(p-c))**(1/2)
print("Uchburchakning peremetri= ", P)
print("Uchpurchakning yuzasi= ", S)