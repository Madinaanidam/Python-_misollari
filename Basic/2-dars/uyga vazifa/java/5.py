# A va B (A>B) musbat sonlari berilgan.
# A kesmada B kesmani necha marta joylashtirish
# mumkun. A kesmada B kesmaning joylashmagan 
# qismini aniqlovchi programma tuzing.
A=int(input("A kesmani kiriting= "))
B=int(input("B kesmani kiriting= "))
if (A>B):
    print("A kesmada B kesmani necha marta joylashtirish mumkunligi= ", A//B)
    print("A kesmada B kesmaning joylashmagan qismi= ", A%B)
else:
    print("Kiritilgan A kesma B kesmadan kichkina. Qaytadan kiriting!")