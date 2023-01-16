ohjelmistoversio = 1.0

# Käytetyt kirjastot:
import os
from urllib.request import urlopen
from datetime import datetime

clearConsole = lambda: print('\n' * 150)

clearConsole()

# Valuuttojen datan 

sivu = urlopen("https://api.exchangerate-api.com/v4/latest/USD")

sisalto = str(sivu.read())

alkupiste = (sisalto.find('{"USD"'))

data = sisalto[alkupiste+1:-3]

jasen = data.split(",")

def Convert(jasen):
    sanakirja = {jasen[i][1:4]: float(jasen[i][6:]) for i in range(0, len(jasen), 1)}
    return sanakirja

sanakirja1 = (Convert(jasen))

with open("valuutta1.txt") as tiedosto1:
    alkuperainen0 = tiedosto1.readline()


with open("valuutta2.txt") as tiedosto2:
    muunnettava0 = tiedosto2.readline()

alkuperainen = alkuperainen0
muunnettava = muunnettava0

# Määritellään, että jos alkuperäinen yksikkö ei ole dollari, niin 1 jaetaan tutkittavalla valuutan kurssilla.

maara = 1
if sanakirja1[alkuperainen] != 'USD':
    maara = maara / sanakirja1[alkuperainen]


# Menu



def menu():

    clearConsole()

    print("_____________________________________________________")

    print("\nTervetuloa valuuttamuuntimeen!\n")

    print("Valitse tehtävä kirjoittamalla numero.\n")

    print("Valuutan muuntaminen (1)")

    print("Asetukset (2)")

    print("Ohjelmistotiedot (3)")

    print("Sulje ohjelma (4)\n")
    print("_____________________________________________________")
    
    # Komennot

    while True:
        try:
            
            komento = int(input("\nKomento: "))

            if komento == 1:
                
            
                # Valuutan muuntaminen
                print("Käytä luvun erotukseen pistettä")
                muunnettava_maara = float(input(f"Syötä {alkuperainen} määrä: "))

                tulos = maara*(muunnettava_maara*sanakirja1[muunnettava])

                print(f"\n{tulos}{muunnettava}")
                jatko()
                break

            elif komento == 2:
                asetukset()
                break

            elif komento == 3:
                ohjelmistotiedot()
                break


            elif komento == 4:
                break

        except: ValueError
        print("Syötä komennoksi numero!")



# Asetukset valikko

def asetukset():

    clearConsole()

    print("_____________________________________________________")
    print("\nAsetukset: \n")

    print("Valitse tehtävä kirjoittamalla numero.\n")

    print("Vaihda alkuperäisen luvun valuuttaa (1)")
    
    print("Vaihda muunnettavaa valuuttaa (2)")

    print("Palaa takaisin (3)\n")
    print("_____________________________________________________")

    # Komennot
    while True:
        try:
            akomento = int(input("\nKomento: "))

            if akomento == 1:
                tulos1= str(input("Anna valuuttakoodi: "))
                with open("valuutta1.txt", "w") as kirjoitus:
                    kirjoitus.write(tulos1)
                print("Käynnistä sovellus uudestaan!")
                break
                    
                
            elif akomento == 2:
                tulos2= str(input("Anna valuuttakoodi: "))
                with open("valuutta2.txt", "w") as kirjoitus:
                    kirjoitus.write(tulos2)
                print("Käynnistä sovellus uudestaan!")
                break

            elif akomento == 3:
                menu()
                break
        except: ValueError
        print("Syötä komennoksi numero!")

tanaan = datetime.now()

alkupistedate = (sisalto.find('date":"'))
pvuosi = sisalto[alkupistedate+7:alkupistedate+11]
pkuukausi = sisalto[alkupistedate+12:alkupistedate+14]
ppaiva = sisalto[alkupistedate+15:alkupistedate+17]

def ohjelmistotiedot():

    clearConsole()

    print("_____________________________________________________")

    print("\nOhjelmistotietoja:\n")

    print("Valitse tehtävä kirjoittamalla numero.\n")

    print("Valuuttakurssien viimeisin päivitys (1)")

    print("Ohjelmiston tiedot (2)")

    print("Palaa takaisin (3)\n")
    print("_____________________________________________________")

    # Komennot

    while True:
        try:
            
            komento = int(input("\nKomento: "))

            if komento == 1:
                
                # Valuuttakurssien viimeinen päivitys
                print(tanaan.strftime("Päivämäärä: %d.%m.%Y"))
                print(tanaan.strftime("Kellon aika tällä hetkellä: %H:%M"))
                print(f"Kurssi päivitetty: {ppaiva}.{pkuukausi}.{pvuosi}")
                jatko()
                break

            elif komento == 2:
                print(f"Ohjelmistoversio: {ohjelmistoversio}")
                print(f"Tekijät: Niko Itänen ja Akseli Teuho")
                jatko()
                break

            elif komento == 3:
                menu()
                break

        except: ValueError
        print("Syötä komennoksi numero!")


# Funktio sovelluksen jatkamisen varmistukseen.

def jatko():
    komento = input("\nSyötä mitä tahansa jatkaaksesi.")
    
    if komento == "K" or "k":
        menu()


menu()