# Ikki xonali son berilgan. 
# Uning raqamlari yig'indisini aniqlovchi programma tuzilsin. 
n=int(input("Ikki xonali son kiriting= "))
if(n>9) and (n<101):
    print("Uning raqanlari yig'indisi= ", (n//10)+(n%10))
else:
    print("Kiritilgan son ikki xonali son emas. Qaytadan son kiriting!")
