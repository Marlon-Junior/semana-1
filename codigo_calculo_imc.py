while True:
    nome = input("Qual o seu nome? ").strip()
    if not nome.replace(" ", "").isalpha():
        print("Nome inválido. Use apenas letras.")
        continue

    try:
        altura = float(input(f"Olá {nome}, qual a sua altura em metros? (Ex: 1.75) "))
        if altura <= 0:
            print("Você tem uma altura negativa? Tente novamente. ")
            continue
    except ValueError:
        print("Por favor, coloque sua altura em metros.")
        continue

    try:
        peso = int(input("E qual o seu peso? "))
        if peso <= 0:
            print("Está precisando comer mais hein... Tente novamente.")
            continue
    except ValueError:
        print("Coloque seu peso seco, sem gramas, por favor.")

    break

imc = peso / (altura * altura)

if imc < 18.5:
    status = "abaixo do peso"
elif imc < 25:
    status = "com peso normal"
elif imc < 30:
    status = "com sobrepeso"
else:
    status = "com obesidade"


print(f"{nome}, seu IMC é aproximadamente {round(imc)} e você está {status}")