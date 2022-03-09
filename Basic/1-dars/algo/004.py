from cmath import pi


r=int(input("Sharning radiusini kiriting: "))
if ((r>=1)) and ((r<=100)):
    print("Birinchi doiraning yuzi= ", 4*pi*r**2)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")