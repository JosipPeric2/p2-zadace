def obrtanje_stringa(s):
    if len(s) == 0:
        return s
    else:
        return obrtanje_stringa(s[1:]) + s[0]