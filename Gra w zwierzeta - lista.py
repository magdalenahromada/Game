# Zadanie 5
# Korzystając z modułu random stwórz kolejną prostą grę. Komputer losuje słowo z dostępnego zakresu (posiada listę słów). 
# Następnie litery są mieszane.
# Wymieszane litery pokazywane są graczowi. Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.

# Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem.  dopisać


import random
zwierzeta = ["kot", "pies", "mysz", "królik", "panda", "wiewiórka", "biedronka", "żółw"]

wylosowane = random.randint(0, 7)
zwierze = zwierzeta[wylosowane]
#print(zwierze) #wlasciwe
zwierze_lista = list(zwierze)
przed_potasowaniem = zwierze_lista.copy()
#print(przed_potasowaniem)

random.ssffs