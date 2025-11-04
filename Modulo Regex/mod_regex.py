import re

text = "Luffy quer ser o rei dos piratas"

# Indice inicial e final
# O 'r' significa raw strig (string bruta)

match = re.search(r"rei dos piratas", text)

print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

# buscando o ponto
site = "google.com"

match = re.search(r'\.', site)
print(match)

# Buscando uma lista de caracteres de uma frase
pattern = "[l-s]"
match = re.findall(pattern, text)

print(match)