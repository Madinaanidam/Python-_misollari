a=int(input("Uchburchakning birinchi tomonini kiriting: "))
b=int(input("Uchburchakning ikkinchi tomonini kiriting: "))
c=int(input("Uchburchakning uchinchi tomonini kiriting: "))
if ((a>=1) and (b>=1) and (c>=1)) and ((a<=100) and (b<=100) and (c<=100)):
    print("Birinchi doiraning yuzi= ", (a+b+c)/2)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")