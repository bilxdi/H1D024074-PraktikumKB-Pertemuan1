import random

b = random.randint(1,10)
a = 0
while(a != b):
    a = int(input("tebak angka 1-10: "))
    if (a == b):
        print("benar")
        break
    else:
        print("tidak benar, coba lagi\n")