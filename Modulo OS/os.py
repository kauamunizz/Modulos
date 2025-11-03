import os

# Retorna a pasta atual
print(os.getcwd())

# Lista arquivos e pastas
print(os.listdir())

# Versao do SO
os.system("ver")

# Configurações da Maquina
os.system("systeminfo")

# Limpar a tela do terminal
os.system('cls')

# Desligar o pc
# os.system("shutdown /s")
# os.system("shutdown /a") #Cancela o desligamento

def desliga_one_hour():
    os.system("shutdown /s /t 3600")
    
def cancelar():
    os.system("shutdown /a")