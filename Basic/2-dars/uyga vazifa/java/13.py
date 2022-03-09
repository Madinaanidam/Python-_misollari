#Uch xonali son berilgan. 
# Uning chapdan birinchi raqamini 
# o'chirib o'ng tarafiga yozishdan hosil 
# bo'lgan sonni aniqlovchi programma tuzilsin
n=int(input("Uch xonali son kiriting= "))
a=n//100
b=n%100
d=(b*10)+a
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", d)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")