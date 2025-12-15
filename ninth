def dec_to_bin(cislo):
    # pokud je string tak na int
    cislo_int = int(cislo)
    # Použití bin() která vrací "0b..." a odstraňění "0b" prefix
    return bin(cislo_int)[2:]


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
