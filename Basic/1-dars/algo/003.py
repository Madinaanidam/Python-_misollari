S=int(input("Uchburchakning yuzasini kiriting: "))
h=int(input("Uchburchakning balandligini kiriting: "))
if ((S>=1) and (h>=1)) and ((S<=100) and (h<=100)):
    print("Uchburchakning asosi= ", 2*S/h)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")