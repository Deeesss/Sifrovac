sifrovac = ""
print("povodna sprava:", sifrovac)
sprava = ""
posun = 1

for znak in sifrovac:
    i = ord(znak)
    i = i + posun
    if (i > ord("z")):
        i = i - 26
    znak = chr(i)
    sifrovac = sifrovac + znak

print("Zašifrovaná zpráva:", zprava)
input()
