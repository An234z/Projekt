import random

võimalikud_valikud = ["kivi", "paber", "käärid"]
mvõit = 0
avõit = 0
while True:
    print("Sinu võidud:", mvõit)
    print("Arvuti võidud:", avõit)
    mängja_valik = input("Sisesta enda valik (kivi, paber, käärid): ").lower()

    if mängja_valik not in ["kivi", "paber", "käärid"]:
        print("Sisesta valikus olev sõna!")
    else:
        arvuti_valik = random.choice(võimalikud_valikud)

        print("Arvuti valis: ", arvuti_valik)

        if mängja_valik == arvuti_valik:
            print("Viik!")
        elif mängja_valik == "kivi" and arvuti_valik == "käärid" or mängja_valik == "paber" and arvuti_valik == "kivi" or mängja_valik == "käärid" and arvuti_valik == "paber":
                print("Sa võitsid!")
                mvõit += 1
                
        else:
               print("Arvuti võitis!")
               avõit += 1
        kas_veel = input("Kas soovid veel mängida? jah/ei ")
        if kas_veel == "ei":
            break
