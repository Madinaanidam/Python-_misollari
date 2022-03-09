#Uch xonali son berilgan. 
# Uning raqamlari yig'indisini 
# aniqlovchi programma tuzing.
n=int(input("Uch xonali son kiriting= "))
a=n%10
b=(n//10)%10
c=n//100
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", a+b+c)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")