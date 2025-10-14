def cislo_text(cislo):
    cislo = int(cislo) #přetransformování stringu na int
#vytvoření slovníků
    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }

    náct = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct",
        14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct",
        18: "osmnáct", 19: "devatenáct"
    }

    desitky = {
        20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát",
        60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát"
    }
#pokud je číslo menší než deset vybere jen od jednotek
    if cislo < 10:
        return jednotky[cislo]
    # pokud je číslo menší než dvacet vybere od náct
    elif cislo < 20:
        return náct[cislo]
    #pokud je číslo menší než sto vybere jen od desitek
    elif cislo < 100:
        d = cislo // 10 * 10 # // vydělí beze zbytku a zjistí kolik je desítek.
        j = cislo % 10 # to co zbyde po dělení desítkou
        if j == 0:
            return desitky[d]# když je není žádný zbytek, využije se pouze slovník desítky
        else:
            return desitky[d] + " " + jednotky[j]# sečtení počtu desítek a zbytku
    elif cislo == 100:
        return "sto"
    else:
        return "mimo rozsah"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
