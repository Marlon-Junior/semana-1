from datetime import datetime

ano_atual = datetime.now().year

# Validação do nome
while True:
    nome = input("Qual o seu nome? ").strip()
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido. Insira apenas letras.")

try:
    idade = int(input(f"Olá {nome}, qual a sua idade? "))

    if idade <= 0:
        print("Idade inválida. Por favor, insira uma idade positiva.")
    
    else:
        numero_anos = int(input(f"Então {nome}, quantos anos no futuro você gostaria de calcular? "))

        if numero_anos < 0:
            print("Por favor, insira um número positivo de anos.")
        
        elif numero_anos == 0:
            print(f"{nome}, você tem {idade} anos e isso não mudaria no tempo!")
        
        else:
            ano_futuro = ano_atual + numero_anos
            idade_futuro = idade + numero_anos

            print(f"{nome}, em {ano_futuro} você terá {idade_futuro} anos!")

except ValueError:
    print("Por favor, insira apenas números inteiros para idade e anos.")
