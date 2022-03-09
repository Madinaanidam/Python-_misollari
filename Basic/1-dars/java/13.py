from cmath import pi


R1=int(input("Birinchi aylananing radiusini kiriting: "))
R2=int(input("Ikkinchi aylananing radiusini kiriting: "))
if (R1>R2):
    print('S1=', pi*R1)
    print('S2=', pi*R2)
    print('S3=', pi*(R1-R2))
else:
    print("Birinchi aylananing radiusi ikkinchi aylananing radiusidan kichik bo'ldi qaytadan son kiriting!")