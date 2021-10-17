# Przygotować skrypt który pyta użytkownika o dane personalne osoby (np imię, nazwisko, nr tel) i zapisuje je do JSONa.
# Obsłużyć wyjątek (try/except) gdy podany nr tel nie jest prawdziwym nr tel.
# (Przykłady nr tel:
# 123-403-129
# 438 123 398
# 123456789).
# Zróbmy bez kierunkowego dla uproszczenia

import json


def wprowadz_dane():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    phone = input("Podaj numer telefonu: ")

    filepath = 'dane.json'
    with open(filepath, 'a') as f:
        json.dump([name, surname, phone], f)

    if len(phone) != 9:
        try:
            phone = int(input("Podaj 9 cyfr jako numer telefonu: "))
        except ValueError:
            print("Podaj 9 cyfr! Spróbuj jeszcze raz...")


wprowadz_dane()
