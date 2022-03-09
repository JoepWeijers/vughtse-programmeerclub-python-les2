# vughtse-programmeerclub-python-les2
Les 2 over Python voor de Vughtse Programmeerclub

Zie de presentatie voor uitleg.
We zijn de les begonnen met een korte herhaling van de types die we geïntroduceerd hebben in Les 1. Daarna hebben we geleerd over de list en de dictionary. Een voorbeeld van een dictionary staat in [tekst_naar_nummer.py](tekst_naar_nummer.py).

## Opdracht 1:
Pas het raadspel van vorige week aan:
Vraag niet om een cijfer als input, maar vraag om tekst (bijvoorbeeld "twee") en zet die met een dictionary om naar een getal.
Let op het type! Een int en een string zijn verschillend. En je kan een variabele gebruiken om iets in een dictionary op te zoeken:
```
tekst_naar_nummer = {
  "een": 1
  "twee": 2
}
ingevuld_getal_tekst = "twee"
print(tekst_naar_nummer[ingevuld_getal_tekst])
```
Dit zal het getal 2 printen.

De uitwerking vindt je in [geheim-getal.py](geheim-getal.py).


Toen kwamen de wiskundige en vergelijkingsoperatoren en `if`, `elif`, `else` aan bod, met als voor beeld [leeftijd.py](leeftijd.py).

## Opdracht 2:
Maak een nieuw programma dat om een nummer vraagt en print of het "even" of "oneven" is. Let weer op het type! Een int en een string zijn verschillend.

De uitwerking vindt je in [if-else.py](if-else.py)


Hierna hebben we naar de `while` en `for` loops gekeken en het `continue` keyword. Met als voorbeeld [forlooplist.py](forlooplist.py)

## Opdracht 3:
Schrijf een programma dat alle getallen van 1 tot 100 print. 
Bij elke veelvoud van 3 moet het programma 'Programmeer' printen in plaats van het getal
Bij elke veelvoud van 5 moet je 'Club' printen. 
Een veelvoud van 3 en 5 print je als 'ProgrammeerClub‘.
Probeer het programma zoveel mogelijk in één keer op te schrijven voordat je het test.

De uitwerking vindt je in [programmeerclub.py](programmeerclub.py).


Je hoeft niet al je code zelf te schrijven. Sommige functies zijn allang door iemand anders geschreven die ze dan kan publiceren zodat iedereen ze kan gebruiken. Dit noemen we libraries. Ze zijn te vinden op https://pypi.org/. Libraries kun je installeren met `pip install <naam van de library>`. Als je Thonny gebruikt, kun je ze installeren door in het menu Hulpmiddelen > Pakketten beheren > de naam van de library in te vullen > Search on Pypi > Klik op de naam van de library > Installeren. In het voorbeeld gebruiken we de library telwoord.

Om een library in je script te gebruiken moet je de functie die je wil gebruiken importeren. Daarna kun je deze functie gebruiken.

## Opdracht 4:
Maak een programma dat een nummer als input vraagt en vervolgens de `telwoord` library gebruikt om het nummer uit te schrijven. Bijvoorbeeld 1 wordt "een", 23 wordt "drieëntwintig".

Let op dat sommige nummers niet volledig uitgeschreven worden, bijvoorbeeld 45. Dit is een functionele keuze van de maker van de library en staat beschreven in de documentatie van de library die te vinden is op https://pypi.org/project/telwoord/. Door `friendly=False` als extra argument aan de `cardinal` functie mee te geven zal de library wel alle nummers volledig uitschrijven.

De uitwerking vindt je in [nummer_naar_tekst.py](nummer_naar_tekst.py).


Een laatste voorbeeld van het gebruik van een library is `pygame`, waarmee je spelletjes in python kan maken. Het voorbeeld heeft maar 30 regels code nodig om een full screen programma te maken met een stuiterende bal. Dit voorbeeld vindt je in [intro_ball.py](intro_ball.py).


Als laatste kwam nog de vraag op hoe je je gemaakte Python applicaties kan delen. Je kan voor simpele programma's, zonder libraries, direct de `.py` file doorsturen. Als de ontvanger Python heeft kan die ze uitvoeren. Heb je wel libraries, dan wil je een pakketje uitleveren dat in een keer werkt. Daarvoor kun je Pyinstaller gebruiken: https://pyinstaller.readthedocs.io/en/stable/

Als voorbeeld heb ik de pygame ook verpakt in een Windows executable, die je direct kan uitvoeren: [intro_ball.exe](intro_ball.exe).

Deze heb ik gemaakt door `pyinstaller --onefile --noconsole intro_ball.py` uit te voeren.
