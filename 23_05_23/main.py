import calendar as cl
from datetime import datetime
import re

if __name__ == "__main__":
    # ZAD 1
    print(cl.calendar(2023))

    # ZAD 2
    print(cl.month(2020, 6))

    # ZAD 3
    data1 = datetime(2023, 6, 1)
    data2 = datetime(2023, 7, 18)
    roznca = data2 - data1
    print(roznca)

    # ZAD 4
    string = "Python 3.11"
    wynik = re.findall(r'\d', string)
    print(wynik)

    # ZAD 5
    string_zad5 = '!@#$%^&45ssewerffffwc'
    wynik_zad5 = re.findall(r'\w', string_zad5)
    print(wynik_zad5)
