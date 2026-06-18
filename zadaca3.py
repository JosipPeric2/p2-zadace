import csv


studenti = []

try:
    with open('rezultati.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        
        
        for red in reader:
            if len(red) >= 3:
                ime = red[0].strip()
                prezime = red[1].strip()
                # Pretvaramo bodove u broj (float ili int) radi kasnijeg uspoređivanja
                bodovi = float(red[2].strip())
                
                studenti.append((ime, prezime, bodovi))
except FileNotFoundError:
    print("Datoteka 'rezultati.csv' nije pronađena. Provjerite putanju.")
    
    studenti = [
        ("Ivan", "Horvat", 45.0),
        ("Ana", "Kovačić", 72.5),
        ("Marko", "Marić", 55.0),
        ("Lucija", "Babić", 88.0),
        ("Josip", "Perić", 95.0),
        ("Petar", "Anić", 49.0)
    ]


print("--- Studenti koji su položili ispit (bodovi > 49) ---")
for ime, prezime, bodovi in studenti:
    if bodovi > 49:
        print(f"{ime} {prezime} - {bodovi} bodova")


studenti_sortirano = sorted(studenti, key=lambda x: x[1])

print("\n--- Lista sortirana po prezimenima ---")
for student in studenti_sortirano:
    print(student)


brojac_ocjena = {
    "Nedovoljan (0-49%)": 0,
    "Dovoljan (50-65%)": 0,
    "Dobar (65-80%)": 0,
    "Vrlodobar (80-90%)": 0,
    "Izvrstan (90-100%)": 0
}


for ime, prezime, bodovi in studenti:
    if bodovi < 50:
        brojac_ocjena["Nedovoljan (0-49%)"] += 1
    elif 50 <= bodovi < 65:
        brojac_ocjena["Dovoljan (50-65%)"] += 1
    elif 65 <= bodovi < 80:
        brojac_ocjena["Dobar (65-80%)"] += 1
    elif 80 <= bodovi < 90:
        brojac_ocjena["Vrlodobar (80-90%)"] += 1
    elif 90 <= bodovi <= 100:
        brojac_ocjena["Izvrstan (90-100%)"] += 1

print("\n--- Broj ostvarenih ocjena po rangovima ---")
for rang, broj in brojac_ocjena.items():
    print(f"{rang}: {broj}")