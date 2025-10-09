#Ve svém repozitáři vytvořte soubor second.py, jako vzor použijte soubor přiložený k tomuto zadání. Upravte funkci

#cislo_text, která bude převádět číslo předané v parametru cislo na textovou reprezentaci daného čísla a tento text vrátí pomocí příkazu return. Příklad fungování funkce:
#"0" -> "nula"
#"1" -> "jedna"
#"15" -> "patnáct"
#"25" -> "dvacet pět"
#"100" -> "sto"
#fungování svého programu můžete vyzkoušet spuštěním "python second.py", nebo kliknutím na symbol "run" vpravo nahoře ve vašem codespace na github.com.
#Termín pro odevzdání úlohy (nahrání do vašeho repozitáře) je Středa 15.10.2025 15:00. Zde na moodlu jako řešení pouze napiště "hotovo", abych vám mohl přidat hodnocení.

def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    return "dvacet pět"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
