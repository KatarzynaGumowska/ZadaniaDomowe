# 2). Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
# Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy

def ZbadajTrojkat():
    print("Podaj długosci trzech ramion trojkata ")
    Bok1 = int(input("Bok 1 "))
    Bok2 = int(input("Bok 2 "))
    Bok3 = int(input("Bok 3 "))

    if Bok1 == Bok2 == Bok3:
        print("Trójkąt równoboczny")
    elif Bok1 == Bok2:
        print("Trójkąt równoramienny")
    elif Bok2 == Bok3:
        print("Trójkąt równoramienny")
    elif Bok1 == Bok3:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt róźnoboczny")

    if Bok1**2 + Bok2**2 == Bok3**2:
        print("Trójkąt prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")
ZbadajTrojkat()
