# 1). Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych indeksach.
# Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
# Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’

Lista1 = []
Lista2 = []

def DodajListy():
    # Lista1 = int(input("Podaj 3 cyfry pierwszej listy "))
    # Lista2 = int(input("Podaj 3 cyfry drugiej listy "))
    Lista1 = [1,2,3]
    Lista2 = [4,5,6]
    NowaLista = Lista1 + Lista2
    # NowaLista = Lista1.append(Lista2)
    print(NowaLista)

if len(Lista1) != len(Lista2):
    print('Podane listy musza byc tej samej dlugosci')
else:
    print('Listy zostały dodane')

DodajListy()