#vytvořte si účet na https://github.com
#vytvořte projekt pg
#vytvořte svůj první program first.py
#program first.py bude obsahovat jednu funkci sudy_nebo_lichy a bude přebírat jeden parametr cislo, pomocí podmínky otestuje, zda je liché nebo sudé a vypíše text: "Číslo X je sudé" nebo "Číslo X je liché"
#do programu přidejte volání funkce: sudy_nebo_lichy(5) a sudy_nebo_lichy(1000000)
#nahrajte ho do repozitáře
#odkaz na váš repozitář nahrajte zde

cislo= int(input("zadej cislo: "))
def sudy_nebo_lichy(cislo):
	
    if cislo % 2 == 0: # cislo ktere se da vydelit dvemi beze zbytku
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

# Volání funkcí
sudy_nebo_lichy(cislo)
print("")
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)
