V=int(input("Qayiqning tezligini kiriting: "))
U=int(input("Oqimning tezligini kiriting: "))
T1=int(input("Qayiqning oqim bo'yich harakatlanish vaqtini kiriting: "))
T2=int(input("Qayiqning oqimga qarshi harakatlanish vaqtini kiriting: "))
if (V>U):
    print("Qayiqning oqim bo'yicha bosgan masofasi= ", (V+U)*T1)
    print("Qayiqning oqimga qarshi bosgan masofasi= ", (V-U)*T2)
else:
    print("Qayiq oqimga qarshi harakatlana olmatdi")