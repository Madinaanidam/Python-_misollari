#Uch xonali son berilgan. 
# Oldin uni birliklar xonasidagi 
# raqamini so'ng o'nliklar xonasidagi 
# raqamini aniqlovchi programma tuzilsin.
n=int(input("Uch xonali son kiriting= "))
if(n>99 and n<1000):
    print("Birliklar xonasidagi raqam= ", n%10)
    print("O'nliklar xonasidagi raqam= ", (n//10)%10)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")