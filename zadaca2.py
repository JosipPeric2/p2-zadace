import random

imena = [
    "Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", 
    "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", 
    "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", 
    "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", 
    "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", 
    "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", 
    "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", 
    "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", 
    "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", 
    "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"
]

studenti_ocjene = {}
for ime in imena:
    ocjena = random.randint(1, 5)
    studenti_ocjene[ime] = ocjena

brojac_ocjena = {}
for student in studenti_ocjene:
    ocjena = studenti_ocjene[student]
    if ocjena not in brojac_ocjena:
        brojac_ocjena[ocjena] = 1 
    else:
        brojac_ocjena[ocjena] = brojac_ocjena[ocjena] + 1

print("Broj pojedinih ocjena:", brojac_ocjena)

broj_prošlih = 0
ukupno_studenata = len(studenti_ocjene)

for student in studenti_ocjene:
    if studenti_ocjene[student] > 1:
        broj_prošlih = broj_prošlih + 1

postotak = (broj_prošlih / ukupno_studenata) * 100

