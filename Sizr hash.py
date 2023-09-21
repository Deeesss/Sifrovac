retezec = ""
print("Původní zpráva:", retezec)
zprava = ""
posun = 1

for znak in retezec:
    i = ord(znak)
    i = i + posun
    if (i > ord("z")):
        i = i - 26
    znak = chr(i)
    zprava = zprava + znak

print("Zašifrovaná zpráva:", zprava)
input()