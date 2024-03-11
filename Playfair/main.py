def init_matrice(cheie):
   matrice = ''
   for char in cheie.upper():
       if char not in matrice and char.isalpha():
           matrice += 'I' if char == 'J' else char
   alfabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
   for char in alfabet:
       if char not in matrice:
           matrice += char
   return [matrice[i:i+5] for i in range(0, 25, 5)]


def preprocess_text(text):
   procesat = ''
   anterior = ''
   for char in text.upper():
       if char.isalpha():
           if char == anterior:
               procesat += 'X'
           procesat += 'I' if char == 'J' else char
           anterior = char
   if len(procesat) % 2 != 0:
       procesat += 'X'
   return procesat


def criptare_perechi(pair, matrice):
   rows, cols = {}, {}
   for i, row in enumerate(matrice):
       for j, litera in enumerate(row):
           rows[litera], cols[litera] = i, j
   a, b = pair
   ra, ca = rows[a], cols[a]
   rb, cb = rows[b], cols[b]
   if ra == rb:
       return matrice[ra][(ca + 1) % 5] + matrice[rb][(cb + 1) % 5]
   elif ca == cb:
       return matrice[(ra + 1) % 5][ca] + matrice[(rb + 1) % 5][cb]
   else:
       return matrice[ra][cb] + matrice[rb][ca]


def criptare_text(text, cheie):
   matrice = init_matrice(cheie)
   text_preparat = preprocess_text(text)
   criptat = ''
   for i in range(0, len(text_preparat), 2):
       criptat += criptare_perechi(text_preparat[i:i + 2], matrice)
   return criptat


def decriptare_perechi(pair, matrice):
   rows, cols = {}, {}
   for i, row in enumerate(matrice):
       for j, litera in enumerate(row):
           rows[litera], cols[litera] = i, j
   a, b = pair
   ra, ca = rows[a], cols[a]
   rb, cb = rows[b], cols[b]
   if ra == rb:
       return matrice[ra][(ca - 1) % 5] + matrice[rb][(cb - 1) % 5]
   elif ca == cb:
       return matrice[(ra - 1) % 5][ca] + matrice[(rb - 1) % 5][cb]
   else:
       return matrice[ra][cb] + matrice[rb][ca]


def decriptare_text(text_criptat, key):
   matrice = init_matrice(key)
   decriptat = ''
   for i in range(0, len(text_criptat), 2):
       decriptat += decriptare_perechi(text_criptat[i:i + 2], matrice)
   return decriptat




key = "SECRET KEY"
text = "THE ART OF PROGRAMMING"
text_criptat = criptare_text(text, key)
print(text_criptat)
text_decriptat = decriptare_text(text_criptat, key)
print(text_decriptat)
