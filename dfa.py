f = open("exemplu.txt")
nr_stari = int(f.readline())
stari = [int(x) for x in f.readline().split()]
# print(stari)
nr_litere = int(f.readline())
litere = f.readline().split()
# print(litere)
stare_initiala = f.readline().strip()
nr_stari_finale = int(f.readline())
stari_finale = [x for x in f.readline().split()]
nr_tranzitii = int(f.readline())
tranzitiile = {}
for i in range(nr_tranzitii):
    tranzitie = f.readline().split()
    if tranzitie[0] not in tranzitiile.keys():
        tranzitiile[tranzitie[0]] = [(tranzitie[2], tranzitie[1])]
    else:
        tranzitiile[tranzitie[0]].append((tranzitie[2], tranzitie[1]))

nr_cuvinte = int(f.readline())
cuvinte = [f.readline().strip() for i in range(nr_cuvinte)]
# print(cuvinte)
for cuvant in cuvinte:
    if cuvant == "":
        if stare_initiala in stari_finale:
            print("DA")
        else:
            print("NU")
    else:
        stare_curenta = stare_initiala
        for litera in cuvant:     
            ok = 0
            if stare_curenta in tranzitiile:
                for tranzitie in tranzitiile[stare_curenta]:
                    if tranzitie[1] == litera: 
                        stare_curenta = tranzitie[0]
                        ok = 1
                        break

            if ok == 0:
                break
        if stare_curenta in stari_finale and ok == 1:
            print("DA")
        else:
            print("NU")
