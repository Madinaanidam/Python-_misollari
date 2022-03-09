# Uch xonali son berilgan. 
# Uning o'nliklar xonasidagi raqam bilan 
# yuzliklar xonasidagi raqamni almashtirishdan 
# hosil bo'lgan sonni aniqlovchi programmani tuzing.(Kirish=123, Natija=213)
n=int(input("Uch xonali son kiriting= "))
a=(n//10)%10
b=n//100
c=n%10
d=(a*100)+(b*10)+c
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", d)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")