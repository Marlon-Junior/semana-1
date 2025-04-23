# Validação do nome
while True:
    nome = input("Qual o seu nome? ").strip()
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido. Use apenas letras.")

# Pergunta a idade
try:
    idade = int(input(f"Olá {nome}, qual a sua idade? "))

    if idade < 0:
        print("Tem certeza que é essa sua idade?")
    elif idade < 16:
        print("Você não pode votar!")
    elif 16 <= idade < 18 or idade > 70:
        print("Voto opcional!")
    else:
        print("Voto obrigatório!")

except ValueError:
    print("Por favor, digite apenas idades inteiras.")