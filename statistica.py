voti = []
print("Inserisci voti")
print("Termina con exit")
riga = input()
while riga.isdigit() :
    voti.append(int(riga))
    riga = input()
for voto in voti :
    print(voto)