while True:
    print('1 - Oblicz średnią arytmetyczną')
    print('2 - Podnieś do potęgi')
    print('3 - Porównaj liczby')
    print('4 - Koniec')
    decyzja = input('Wybierz opcję: ')
    if decyzja == '1':
        liczba_1 = int(input("podaj pierwszą liczbę: "))
        liczba_2 = int(input("podaj drugą liczbę: "))
        print((liczba_1 + liczba_2) / 2)
    elif decyzja == '2':
        liczba_1 = int(input("podaj liczbę: "))
        liczba_2 = int(input("podaj potęgę: "))
        print(liczba_1 ** liczba_2)
    elif decyzja == '3':
        liczba_1 = int(input("podaj pierwszą liczbę: "))
        liczba_2 = int(input("podaj drugą liczbę: "))
        if liczba_1 > liczba_2:
            print("pierwsza liczba jest większa")
        elif liczba_1 < liczba_2:
            print("druga liczba jest większa")
    elif decyzja == '4':
        quit()