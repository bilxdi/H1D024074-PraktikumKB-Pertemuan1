import random, math

print("TEBAK ANGKA")
answer = random.randint(1,20) #milih random jawaban antara 1-20
percobaan = 5 #limit percobaan nebak 5 kali
riwayat = [] #list buat contain riwayat tebakan

while(percobaan != 0):
    tebak = int(input("\ntebak angka 1-20: "))
    riwayat.append(tebak) #masukin input tebakan ke list riwayat
    percobaan = percobaan - 1
    jarak = math.fabs(tebak - answer) #hitung jarak tebakan sama jawaban

    if (tebak == answer):
        print("\ntebakan benar")
        print("riwayat tebakan: ", riwayat)
        break #keluar dari loop jika sudah benar
    else:
        if (percobaan == 0):
            print("\npercobaan habis")
            print("angka yang benar: ", answer) #jika percobaan habis
        else:
            if (tebak < answer):
                print("\nterlalu kecil") #clue jika tebakan lebih kecil dari jawaban
            else:
                print("\nterlalu besar") #clue jika tebakan lebih besar dari jawaban
            if (jarak <= 2):
                print("sudah dekat") #clue jika tebakan mendekati dengan jawaban
            print("\nsisa percobaan: ", percobaan)

        print("riwayat tebakan: ", riwayat)