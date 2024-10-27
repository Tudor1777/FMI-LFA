f = open("exemplu2.txt")

nr_stari1 = int(f.readline())
stari1 = [int(x) for x in f.readline().split()]
# print("stari 1: ", stari1)
nr_litere1 = int(f.readline())
litere = f.readline().split()
# print("litere 1: ", litere)
stare_initiala = int(f.readline().strip())
# print("stare initiala : ", stare_initiala)
nr_stari_finale1 = int(f.readline())
# print("nr stari finale 1: ", nr_stari_finale1)
stari_finale1 = [int(x) for x in f.readline().split()]
# print("stari finale 1: ", stari_finale1)
nr_tranzitii1 = int(f.readline())
# print("nr tranzitii 1: ", nr_tranzitii1)
tranzitiile1 = {}
for i in range(nr_tranzitii1):
    tranzitie = f.readline().split()
    tranzitie[0] = int(tranzitie[0])
    tranzitie[2] = int(tranzitie[2])
    if tranzitie[0] not in tranzitiile1:
        tranzitiile1[tranzitie[0]] = {tranzitie[1] : tranzitie[2]}
    else:
        if tranzitie[1] not in tranzitiile1[tranzitie[0]]:
            tranzitiile1[tranzitie[0]][tranzitie[1]] = tranzitie[2]
        else:
            tranzitiile1[tranzitie[0]][tranzitie[1]].append(tranzitie[2])
# print("tranzitii 1: ", tranzitiile1)
nr_cuvinte1 = int(f.readline())
cuvinte1 = [f.readline().strip() for i in range(nr_cuvinte1)]

#complement

nr_stari2 = nr_stari1 + 1
print(nr_stari2)
stari2 = stari1
stari2.append(0)
print(*stari2)
stari_finale2 = [stare for stare in stari1 if stare not in stari_finale1]
# stari_finale2.append("0")
print(len(stari_finale2))
print(*stari_finale2)
tranzitiile2 = tranzitiile1
nr_tranzitii2 = nr_tranzitii1
for stare in stari2:
    for litera in litere:
        if stare not in tranzitiile2.keys():
            tranzitiile2[stare] = {litera : 0}
            nr_tranzitii2 += 1
        elif litera not in tranzitiile2[stare].keys():
            tranzitiile2[stare][litera] = 0
            nr_tranzitii2 += 1
print(nr_tranzitii2)
for stare in tranzitiile2:
    for litera in tranzitiile2[stare].keys():
        print(stare, " ", litera, " ", tranzitiile2[stare][litera])
# print("tranzitii 2: ", tranzitiile2)


#check void

vazute = set()
vazute.add(stare_initiala)
ok = 0
while ( ok == 0 ):
    stari_noi = False
    for stare in list(vazute):
        for litera in tranzitiile2[stare].keys():
            if tranzitiile2[stare][litera] in stari_finale2:
                ok = 1
                break
            elif tranzitiile2[stare][litera] not in vazute:
                vazute.add(tranzitiile2[stare][litera])
                stari_noi = True
    if ok == 1:
        print("NU") #nu e vid
        break
    elif stari_noi == False:
        print("DA") #e vid
        break


# print("vazute: ", vazute)





