tekst_naar_nummer = {
    "een": 1,
    "twee": 2,
    "drie": 3,
    "vier": 4,
    "vijf": 5,
    "zes": 6,
    "zeven": 7,
    "acht": 8,
    "negen": 9,
    "tien": 10
}

geheim_getal = 4

while True:
    getal = input('Kies een getal onder de 10 ')
    if (getal in tekst_naar_nummer and tekst_naar_nummer[getal] == geheim_getal):
        print("Goed geraden!")
        break
    else:
        print("Helaas, raad opnieuw")
