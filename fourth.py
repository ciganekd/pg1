def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.

    :return: True, pokud je tah možný, jinak False.
    """

    typ = figurka["typ"]
    start = figurka["pozice"]
    r1, s1 = start
    r2, s2 = cilova_pozice

    # 1️⃣ Kontrola, že pozice je na šachovnici
    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    # 2️⃣ Kontrola, že cílová pozice není obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # 3️⃣ Určení směru a rozdílu
    dr = r2 - r1 #rozdíl v řádcich
    ds = s2 - s1 # rozdil v sloupcích
    abs_dr, abs_ds = abs(dr), abs(ds) #abs. hodnota nebere ohled na směr.

    # 4️⃣ Implementace pravidel pro jednotlivé figury
    if typ == "pěšec":
        if s1 != s2: #pohyb jen dopředu k většímu číslu řádku
            return False  # nesmí se hýbat do stran
        if r1 == 2:  # pohyb z výchozí pozice o dva kroky vpřed
            if r2 == 3 and (3, s1) not in obsazene_pozice:
                return True
            if r2 == 4 and (3, s1) not in obsazene_pozice and (4, s1) not in obsazene_pozice:
                return True
        # zbylé pohyby na pole která nejsou obsazená
        else:
            if r2 == r1 + 1 and (r2, s1) not in obsazene_pozice:
                return True
        return False

    elif typ == "jezdec":
        # Jezdec – dva dopředu jeden doleva nebo doprava, může přeskakovat --> neřeší překážky
        return (abs_dr, abs_ds) in [(2, 1), (1, 2)]

    elif typ == "věž":
        # Musí být stejny řádek nebo stejný sloupec
        if r1 != r2 and s1 != s2:
            return False
        if r1 == r2:
            step = 1 if s2 > s1 else -1
            # kontorla jestli něco nestojí v cestě
            for s in range(s1 + step, s2, step):
                if (r1, s) in obsazene_pozice:
                    return False
        else:
            step = 1 if r2 > r1 else -1
            for r in range(r1 + step, r2, step):
                if (r, s1) in obsazene_pozice:
                    return False
        return True

    elif typ == "střelec":
        # pohyb našikmo
        if abs_dr != abs_ds:
            return False
        step_r = 1 if r2 > r1 else -1
        step_s = 1 if s2 > s1 else -1
        # kontorla jestli něco nestojí v cestě
        for i in range(1, abs_dr):
            if (r1 + i * step_r, s1 + i * step_s) in obsazene_pozice:
                return False
        return True

    elif typ == "dáma":
        # Kombinace věže a střelce
        if r1 == r2 or s1 == s2:
            # věžový pohyb
            if r1 == r2:
                step = 1 if s2 > s1 else -1
                # kontorla jestli něco nestojí v cestě
                for s in range(s1 + step, s2, step):
                    if (r1, s) in obsazene_pozice:
                        return False
            else:
                step = 1 if r2 > r1 else -1
                for r in range(r1 + step, r2, step):
                    if (r, s1) in obsazene_pozice:
                        return False
            return True
        elif abs_dr == abs_ds:
            # střelcový pohyb
            step_r = 1 if r2 > r1 else -1
            step_s = 1 if s2 > s1 else -1
            for i in range(1, abs_dr):
                if (r1 + i * step_r, s1 + i * step_s) in obsazene_pozice:
                    return False
            return True
        else:
            return False

    elif typ == "král":
        #o jednu jakýmkoliv směrem
        return abs_dr <= 1 and abs_ds <= 1

    return False


# zadání jednotlivých situací a test proveditelnosti
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
