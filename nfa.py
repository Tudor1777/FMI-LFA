f = open("exemplu.txt")
nr_stari = int(f.readline())
stari = [int(x) for x in f.readline().split()]
# print(stari)
nr_litere = int(f.readline())
litere = f.readline().split()
# print(litere)
stare_initiala = int(f.readline().strip())
nr_stari_finale = int(f.readline())
stari_finale = [int(x) for x in f.readline().split()]
nr_tranzitii = int(f.readline())
tranzitiile = {}
for i in range(nr_tranzitii):
    tranzitie = f.readline().split()
    tranzitie[0] = int(tranzitie[0])
    tranzitie[2] = int(tranzitie[2])
    if tranzitie[0] not in tranzitiile:
        tranzitiile[tranzitie[0]] = {tranzitie[1] : [tranzitie[2]]}
    else:
        if tranzitie[1] not in tranzitiile[tranzitie[0]]:
            tranzitiile[tranzitie[0]][tranzitie[1]] = [tranzitie[2]]
        else:
            tranzitiile[tranzitie[0]][tranzitie[1]].append(tranzitie[2])

nr_cuvinte = int(f.readline())
cuvinte = [f.readline().strip() for i in range(nr_cuvinte)]
for cuvant in cuvinte:
    if cuvant == "":
        if stare_initiala in stari_finale:
            print("DA")
        else:
            print("NU")
    else:
        stari_curente = [stare_initiala]
        ok = 0
        for litera in cuvant:     
            stari_urmatoare = []
            for stare in stari_curente:
                if stare in tranzitiile and litera in tranzitiile[stare]:
                    stari_urmatoare.extend(tranzitiile[stare][litera])
                stari_curente = stari_urmatoare
        for stare in stari_curente:
            if stare in stari_finale:
                print("DA")
                ok = 1
                break
        if ok == 0:
            print("NU")
