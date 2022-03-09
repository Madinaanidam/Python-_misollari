from cmath import pi


r1=int(input("Birinchi doiraning radiusini kiriting: "))
r2=int(input("Ikkinchi doiraning radiusini kiriting: "))
r3=int(input("Uchunchi doiraning radiusini kiriting: "))
if ((r1>=1) and (r2>=1) and (r3>=1)) and ((r1<=100) and (r2<=100) and (r3<=100)):
    print("Birinchi doiraning yuzi= ", pi*r1**2)
    print("Ikkinchi doiraning yuzi= ", pi*r2**2)
    print("Uchunchi doiraning yuzi= ", pi*r1**2)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")