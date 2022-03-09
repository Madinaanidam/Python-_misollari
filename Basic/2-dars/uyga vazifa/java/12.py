#Uch xonali son berilgan. 
# Uning raqamlarini teskari tartibda yozishdan 
# hosil bo'lgan sonni aniqlovchi programmani tuzing
n=int(input("Uch xonali son kiriting= "))
a=n//100
b=(n//10)%10
c=n%10
d=(c*100)+(b*10)+a
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", d)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")