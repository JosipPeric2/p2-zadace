import sys
from types import ModuleType


moj_modul = ModuleType("moj_modul")
sys.modules["moj_modul"] = moj_modul

def obrtanje_stringa(s):
    if len(s) == 0:
        return s
    else:
        return obrtanje_stringa(s[1:]) + s[0]

moj_modul.obrtanje_stringa = obrtanje_stringa


import moj_modul

unos = input()
rezultat = moj_modul.obrtanje_stringa(unos)
print(rezultat)