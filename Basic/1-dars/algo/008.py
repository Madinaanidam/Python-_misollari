v=int(input("Aftamobil tezligini kiriting: "))
S=int(input("Aftomabil bosib o'tgan masofani kiriting: "))
if ((v>=1) and (S>=1)) and ((v<=100) and (S<=100)):
    print("Aftomabilning v tezlik bilan S masofani bosib o'tishda sarflagan vaqti= ", S/v)
else:
    print("Kiritilgan sonlar qo'yilgan chegaradan oshib ketdi!")