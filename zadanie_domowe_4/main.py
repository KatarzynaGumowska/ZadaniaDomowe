#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime


class Czlowiek:

    def __init__(self, imie, nazwisko, data_urodzenia, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia

        try:
            if len(telefon.split(" ")) == 3 or len(telefon.split("-")) == 3 or (int(telefon) and len(telefon) == 9):
                return 
            raise ValueError()
        except ValueError as e:
            print("Nieprawidłowy format telefonu: " + telefon)

    @property
    def wiek(self):
        born = datetime.datetime.strptime('11 05 2018', "%d %m %Y")
        today = datetime.datetime.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


if __name__ == '__main__':
    Uzytkownik = Czlowiek("Kasia", "Gumowska", "12 05 1990", "203 403 380")
    Uzytkownik = Czlowiek("Kasia", "Gumowska", "12 05 1990", "203-403-380")
    Uzytkownik = Czlowiek("Kasia", "Gumowska", "12 05 1990", "203403380")
    Uzytkownik = Czlowiek("Kasia", "Gumowska", "12 05 1990", "203/403a380")
