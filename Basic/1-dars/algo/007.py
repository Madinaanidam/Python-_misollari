from cmath import pi


h=int(input("Konusning balandligini kiriting: "))
r=int(input("Konusning radiusini kiriting: "))
if ((h>=1) and (r>=1)) and ((h<=100) and (r<=100)):
    print("Konusning hajmi= ", (pi*h*r**2)/3)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")