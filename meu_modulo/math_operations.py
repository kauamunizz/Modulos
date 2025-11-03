def soma(x,y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return f"{x / y:.2f}"
    else:
        raise ValueError("Não é permitido divisao por Zero")