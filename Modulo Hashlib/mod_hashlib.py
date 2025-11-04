import hashlib

# Verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

# Verificar algoritmos de acordo com SO
print(hashlib.algorithms_guaranteed)

# Utilizando SHA256
algoritmo = hashlib.sha256()
print(algoritmo.digest())

messagem = "A melhor forma de prever o futuro é cria-lo".encode()
algoritmo.update(messagem)
print(algoritmo.hexdigest())

# Utilizando MD5
md5 = hashlib.md5()
md5.update(messagem)
print(md5.hexdigest())