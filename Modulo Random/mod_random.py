import random

# Retorna valor aleatorio
list1 = [5, 4, 9, 12, 95, 4]
print(random.choice(list1))

list2 = ["Cara", "Coroa"]
print(random.choice(list2))

# Gera um numero aleatorio em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# seleciona mais de um valor aleatorio
# random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))

# Programa de sorteio

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o numero")
    print("2. Sair")
    
    choice = input(">")
    if choice == "1":
        print("=====================Advinhe um numero de 1 a 10:=====================\n")
        number = int(input("Digite um numero de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabens, você acertou!")
        else:
            print(f"Tente novamente, o numero sorteado foi: {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção invalida. Escolha um numero de 1 a 10")