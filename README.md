# Semana 1 – Introdução à Programação com Python

## Desafios realizados:

### 1. Calculadora de 100 anos
O usuário informa seu nome e idade, e o programa calcula em qual ano ele completará 100 anos.

### 2. Verificador de direito ao voto
O programa solicita o nome e a idade do usuário e, com base na idade, informa se ele pode votar, se o voto é opcional ou obrigatório.

---

## Aprendizados da semana:

- Leitura de dados com `input()` e exibição com `print()`
- Conversão de tipos (`str` para `int` e vice-versa)
- Importação e uso de módulos (`datetime`)
- Condicionais (`if`, `elif`, `else`)
- Tratamento de exceções com `try/except`
- Estrutura de repetição com `while`
- Limpeza e validação de strings com `.strip()`, `.replace()` e `.isalpha()`

---

## Destaque da semana:

### Validação de nomes:
Aprendi a validar nomes compostos e impedir números na entrada, usando:

```python
while True:
    nome = input("Qual o seu nome? ").strip()
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido. Use apenas letras.")
