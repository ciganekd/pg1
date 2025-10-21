def je_prvocislo(cislo):
    if cislo < 2:
        return False  # není prvočíslo proto vrať zpět
    for i in range(2, int(cislo ** 0.5) + 1):# dělení čísla z čísly v rangi (+1 je proto, aby nechybělo jedno číslo)
        if cislo % i == 0: #dělení a zjišťování zbytku
            return False # pokud číslo má zbytek není prvočíslo, a proto vyhoď zpět
    return True #pokud odpovídá podmínkám v cyklu for, je to prvočíslo (není dělitel kromě sebe a jedničky)

def vrat_prvocisla(maximum): #vrácení prvočísel do maxima
    maximum = int(maximum) # vstup na cele cislo
    prvocisla = [] #definování listu
    for cislo in range(2, maximum + 1):# pro čísla zadaná v rangi, vynechání jedničky
        if je_prvocislo(cislo):
            prvocisla.append(cislo) #spuštění funkce na rozpoznání prvočísla
    return prvocisla #vrácení seznamu prvočísel

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: ")) # zadání čísla

    # vypis True/False jen pro zadane cislo
    print(f"{cislo} -> {je_prvocislo(cislo)}")

    # vypis seznam vsech prvocisel od 1 do maxima
    prvocisla = vrat_prvocisla(cislo) #toto zpusobí přeměnu cislo na maximum (ve funkci si proměnné "žijí vlastním životem") tím, že jí hodí do funkce vrat_prvocisla
    print("Seznam prvocisel:", prvocisla) # vypsání prvočísel
