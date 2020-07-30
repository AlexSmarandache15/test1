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
def algoritm1(arie,latime,inaltime,n):
    return 0
def algoritm2(arie,latime,inaltime,n):
    return 0
def algoritm3(arie,latime,inaltime,n):
    return 0
n=int(input("Dati numarul de piese: "))
a=input("Dati aria container: ")
l=input("Dati latimea container: ")
h=input("Dati inaltimea container: ")
#citire arii
print("obiectul ",0)
arie=[int(input("Dati aria"))]
latime=[int(input("Dati latimea"))]
inaltime=[int(input("Dati inaltimea"))]
for i in range(1,n):
    print("obiectul ",i)
    arie.append(int(input("Dati aria")))
    latime.append(int(input("Dati latimea")))
    inaltime.append(int(input("Dati inaltimea")))
for i in range(n):
    print("[",arie[i],latime[i],inaltime[i],"]")
sortare(arie,latime,inaltime)
print("dupa sortare\n")
for i in range(n):
    print("[",arie[i],latime[i],inaltime[i],"]")

