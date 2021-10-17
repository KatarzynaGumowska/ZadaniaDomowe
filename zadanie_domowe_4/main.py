# Stworzyć klasę użytkownika, która będzie dziedziczyć po klasie człowiek (imię, nazwisko, etc.)
# oraz będzie miała atrybut wieku automatycznie obliczany na podstawie daty urodzenia.

class Czlowiek:

    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.set_data_urodzenia = int(data_urodzenia)

    def wiek(self):
        return 2021 - self.set_data_urodzenia


Uzytkownik = Czlowiek("Kasia", "Gumowska", 1985)
print(vars(Uzytkownik))
print(Uzytkownik.wiek())
