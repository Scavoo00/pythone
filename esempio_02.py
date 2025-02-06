n=int(input("Inserisci un numero qualsiasi: "))
x=input("Inserisci una lettera qualunque: ")

for i in range(1,n): 
    print(" "*(n-i) + x*(1+(i-1)*2))
