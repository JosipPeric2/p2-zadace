import re

regex_uzorak = r"^[Jj](?=.*[0-5])(?=.*\s).*[Pp]$"

testni_stringovi = [
    "J5 p",
    "j-tekst 3 tekst p",
    "Josip",
    "J6 periP"
]

for string in testni_stringovi:
    if re.match(regex_uzorak, string):
        print(f"'{string}' -> OK")
    else:
        print(f"'{string}' -> X")