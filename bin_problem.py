#Alex comentariu
#prima incercare
def sortare(arie,latime,inaltime):
    for i in range(0,n-1):
        for k in range(i+1,n):
            if arie[i] < arie[k]:
                aux1=arie[i]
                aux2=latime[i]
                aux3=inaltime[i]
                arie[i]=arie[k]
                latime[i]=latime[k]
                inaltime[i]=inaltime[k]
                arie[k] = aux1
                latime[k] = aux2
                inaltime[k]= aux3
                return 0
def try_to_put_piece(piesa,latime,inaltime):
    #codul functiei
    return 0
n=int(input("Dati numarul de piese: "))
aria=input("Dati aria container: ")
latime=input("Dati latimea container: ")
inaltime=input("Dati inaltimea container: ")
#citire arii
print("\nobiectul ",0)
a=[int(input("Dati aria  "))]
l=[int(input("Dati latimea  "))]
h=[int(input("Dati inaltimea  "))]
for i in range(1,n):
    print("\nobiectul ",i)
    arie.append(int(input("Dati aria  ")))
    latime.append(int(input("Dati latimea  ")))
    inaltime.append(int(input("Dati inaltimea  ")))
for i in range(n):
    print("[",arie[i],latime[i],inaltime[i],"]")
sortare(arie,latime,inaltime)
print("dupa sortare\n")
for i in range(n):
    print("[",arie[i],latime[i],inaltime[i],"]")
waste=0
w=1
nr_p=n
obj_free_area=a
fit=1
while nr_p>0 :
    #Fill the object until one third of its area is covered
    #Register in memory every piece that does not fit

    #from line 5 pseudocod
    for piesa in arie:
        if obj_free_area-piesa>waste:
            break
        if piesa>obj_free_area or fit==0:
            continue
        try_to_put_piece(piesa,latime,inaltime)
