class Roman(object):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @classmethod
    def roman_to_int(cls, roman):
        res = 0
#       for letter in roman:
        for i in range(len(roman)):
            roman_digit = roman[i]
            if i < len(roman) - 1:
                next_roman_digit = roman[i+1]
                if Roman.rom_val[next_roman_digit] > Roman.rom_val[roman_digit]:
                    # volgende >= huidig
                    res -= Roman.rom_val[roman_digit]
                else:
                   # volgende <= huidige
                    res += Roman.rom_val[roman_digit]
            else:
                res += Roman.rom_val[roman_digit]


        print(roman, res)
        return res


assert Roman.roman_to_int('C') == 100
assert Roman.roman_to_int('XLIX') == 49
assert Roman.roman_to_int('MMMCMLXXXVI') == 3986
