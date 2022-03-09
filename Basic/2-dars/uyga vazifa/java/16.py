# Uch xonali son berilgan. 
# Uning birliklar xonasidagi raqam bilan 
# o'nliklar xonasidagi raqamni almashtirishdan 
# hosil bo'lgan sonni aniqlovchi programmani tuzing.(Kirish=123, Natija=132)
n=int(input("Uch xonali son kiriting= "))
a=(n//10)%10
b=n//100
c=n%10
d=(b*100)+(c*10)+a
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", d)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")