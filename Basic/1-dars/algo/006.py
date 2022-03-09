from cmath import pi


a=int(input("G'o'laning birinchi asosini kiriting: "))
b=int(input("G'o'laning ikkinchi asosini kiriting: "))
h=int(input("G'o'laning balandligini kiriting: "))
if ((a>=1) and (b>=1) and (h>=1)) and ((a<=100) and (b<=100) and (h<=100)):
    print("G'o'laning yuzi= ", pi*h*((a/pi**(1/2))+(a/pi**(1/2))))
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")