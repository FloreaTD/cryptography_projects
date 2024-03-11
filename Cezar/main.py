def criptare_cezar(text, cheie):
    rezultat = ""
    for caracter in text:
        if caracter.isalpha():
            deplasare = ord('A') if caracter.isupper() else ord('a')
            rezultat += chr((ord(caracter) - deplasare + cheie) % 26 + deplasare)
        else:
            rezultat += caracter
    return rezultat

def decriptare_cheie_cunoscuta(textcriptat, cheie):
    return criptare_cezar(textcriptat, -cheie)

def decriptare_cezar_toate_cheile(textcriptat):
    for cheie in range(26):
        textdecriptat = decriptare_cheie_cunoscuta(textcriptat, cheie)
        print(f"Cheie {cheie}: {textdecriptat}")

if __name__ == "__main__":
    textoriginal = "CALCULATOR"
    cheiecriptare = 9
    textcriptat = criptare_cezar(textoriginal, cheiecriptare)
    print(f"Text criptat (k = {cheiecriptare}): {textcriptat}")

    textdecriptare_cheie = "WIGYVMXEXIMR JSVQEXMSREPE"
    cheiedecriptare = 4
    textdecriptat = decriptare_cheie_cunoscuta(textdecriptare_cheie, cheiedecriptare)
    print(f"Text decriptat cu cheie cunoscuta (k = {cheiedecriptare}): {textdecriptat}")

    textcriptat_toate_cheile = "YZKBKPUHY"
    print("Decriptare text prin forta bruta:")
    decriptare_cezar_toate_cheile(textcriptat_toate_cheile)

