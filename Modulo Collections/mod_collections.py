from collections import Counter, namedtuple, deque
from operator import itemgetter

# Contagem
frutas = ["maça", "uva", "pera", "banana", "abacaxi", "banana"]

print(frutas)
print(Counter(frutas))

# Tupla nomeada
game = namedtuple('game', ['nome', 'preco', 'nota'])
g1 = game("Fifa 23", 90.60, 8.5)
g2 = game("RE4", 300, 10)
print(g1)
print(g2)

# Ordenando dicionario
estudantes = {"Pedro": 23, "Ana": 22, "Ronaldo": 26, "Mariana": 25}
a = sorted(estudantes.items(), key=itemgetter(1))
print(a)

# Utilizando uma fila em ambas extremidades
deq = deque([20, 30, 40, 50])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)