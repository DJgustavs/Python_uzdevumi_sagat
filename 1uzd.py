"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) ar kadiem cipariem ikdienā tiek strādāts?  Arābu ...pavisam 10 ...0-9
2) romiešu cipari ... I, V, X, D, C, M
3) KAS IR KLASE? Klase sastāv no konstruktora/destruktora un metodēm (iekšējās funkcijas)
4) kadas datu strukturas zinat
"""


class AAA:


    # definēju konstruktoru
    def __init__(self):
        self.roma_sk={
        1: 'I',
        4: 'IV',
        5: 'V',
        10: 'X', 
        40: 'XL', 
        50: 'L', 
        90: 'XC', 
        100: 'C', 
        400: 'CD', 
        500: 'D', 
        900: 'CM', 
        1000: 'M'

        }
        # tā ir metode tas ir, funkcija, kura veiks parveidošanu 
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result
    

kk=AAA()
skaitlis=21
rom_sk=kk.to_roman(skaitlis)
print(f'{skaitlis}romiešu ciparos ir {rom_sk}.')