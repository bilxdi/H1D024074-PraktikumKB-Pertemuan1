import random, math

print("TEBAK ANGKA")
answer = random.randint(1,20)
percobaan = 5
riwayat = []

while(percobaan != 0):
    tebak = int(input("\ntebak angka 1-20: "))
    riwayat.append(tebak)
    percobaan = percobaan-1
    jarak = math.fabs(tebak - answer)

    if (tebak == answer):
        print("\ntebakan benar")
        print("riwayat tebakan: ", riwayat)
        break
    else:
        if (percobaan == 0):
            print("\npercobaan habis")
            print("angka yang benar: ", answer)
        else:
            if (tebak < answer):
                print("\nterlalu kecil")
            else:
                print("\nterlalu besar")
            if (jarak <= 2):
                print("sudah dekat")
            print("\nsisa percobaan: ", percobaan)

        print("riwayat tebakan: ", riwayat)