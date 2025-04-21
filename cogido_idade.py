from datetime import datetime

ano_atual = datetime.now().year

nome = input("Qual o seu nome? ")

try:
    idade = int(input(f"Olá {nome}! Quantos anos você tem? "))

    if idade < 0:
        print("Hmm... idade negativa? Beijamin Button, é você?")
    elif idade >= 100:
        ano_cem = ano_atual - (idade - 100)
        print(f"Parabéns, {nome}! Você já completou 100 anos em {ano_cem}!")
    else:
        falta_cem = 100 - idade
        ano_cem = ano_atual + falta_cem
        print(f"{nome}, você vai completar 100 anos em {ano_cem}. Faltam {falta_cem} anos!")
except ValueError:
    print("Por favor, apenas digite a idade com números inteiros!")
