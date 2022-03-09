# 999 dan katta bo'lgan son berilgan. 
# Bir marta bo'lib butunni va bo'lib qoldiqni 
# olish operatsiyasidan foydalanib berilgan sonni 
# mingliklar xonasidagi sonni aniqlovchi programma tuzilsin.
n=int(input("999 dan katta bo'lgan sonni kiriting= "))
a=(n%10000)//1000
if(n>999):
    print("Berilgan sonning yuzlar xonasidagi son= ", a)
else:
    print("Kiritilgan son 999 dan kichkina. Qaytadan son kiriting!")