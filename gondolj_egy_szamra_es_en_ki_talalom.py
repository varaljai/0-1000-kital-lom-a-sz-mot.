def jojatek(szamok):
    return (szamok[0] + szamok[1])//2
szamok = [0,1000]

input('Gondolj egy számra 0 és 1000 közöt,és én megprobálom ki találni.Ha meg vagy akkor nyomj egy entert.')
while True:
    tipp = jojatek(szamok)
    print(tipp)
    print('Ha nagyobb nyomj egy n-t,ha kissebb akkor nyomj egy k-t,ha egyenlő akkor egy e-t.')
    valasz = input()
    if valasz == 'k':
        szamok[1] = tipp
    elif valasz == 'n':
        szamok[0] = tipp
    elif valasz == 'e':
        print('Köszönöm hogy játszotál a játékomal! további szépnapot!')
        break
        






    



