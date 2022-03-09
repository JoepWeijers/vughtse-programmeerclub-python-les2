lijst = [3,6,5,613,7,8,9]

for cijfer in lijst:
    if cijfer % 2 == 0:
        print("even")
    elif cijfer % 3 == 0:
        print("deelbaar door drie")
    else:
        print("oneven")

for nummer in range(0,5):
    print(nummer)

#Schrijf een programma dat alle getallen van 1 tot 100 print. 
#Bij elke veelvoud van 3 moet het programma 'Programmeer' printen 
# in plaats van het getal
#Bij elke veelvoud van 5 moet je 'Club' printen. 
#Een veelvoud van 3 en 5 print je als 'ProgrammeerClub‘.















for cijfer in lijst:
    if cijfer % 2 == 0:
        print("even")
        continue

    print("oneven")
