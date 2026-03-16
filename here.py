import random, math

print("== TEBAK ANGKA ==")
answer = random.randint(1,20)
percobaan = 5

while(percobaan != 0):
    tebak = int(input("\ntebak angka 1-20: "))
    percobaan = percobaan-1
    if (tebak == answer):
        print("benar")
        break
    else:
        print(answer)
        print("tidak benar, coba lagi")
        print("sisa percobaan: ", percobaan)