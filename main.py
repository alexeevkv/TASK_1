# [1] Написать цикл для выведения на экран каждой буквы своего ФИО

# [2]  Написать функцию для перевода рубля в йену c округлением до 2х знаков после запятой


import numpy as np


RUBLES_TO_YEN_RATE = 1.53
CONVERSION_PRECISION = 2


def print_out_fio(fio: str) -> None:
    for letter in fio:
        if letter.isspace():
            continue
        else:
            print(letter)


def rub_to_yen(rubles: float) -> float:
    return np.round(rubles * RUBLES_TO_YEN_RATE, CONVERSION_PRECISION)


if __name__ == '__main__':
    print_out_fio('ALekseev Konstantin Vladimirovich')

    print(rub_to_yen(951.2))
