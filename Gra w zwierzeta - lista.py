# Zadanie 5
# Korzystając z modułu random stwórz kolejną prostą grę. Komputer losuje słowo z dostępnego zakresu (posiada listę słów). 
# Następnie litery są mieszane.
# Wymieszane litery pokazywane są graczowi. Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.

# Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem.


import random
zwierzeta = ["kot", "pies", "mysz", "królik", "panda", "wiewiórka", "biedronka", "żółw"]

wylosowane = random.randint(0, 7)
zwierze = zwierzeta[wylosowane]
#print(zwierze) #wlasciwe
zwierze_lista = list(zwierze)
przed_potasowaniem = zwierze_lista.copy()
#print(przed_potasowaniem)

random.shuffle(zwierze_lista) 
print(zwierze_lista) #potasowane w liscie


zwierze_uzytkownika = input("Hej, zgdanij co to za zwierze :")
zwierze_uzytkownika_lista = list(zwierze_uzytkownika)
while zwierze_uzytkownika_lista != przed_potasowaniem:
    print("Zgaduj dalej:")
    zwierze_uzytkownika = input()
    zwierze_uzytkownika_lista = list(zwierze_uzytkownika)
print("Brawno, to jest {}" .format(zwierze))


########

&&&&&&&&&&&&&&&&
