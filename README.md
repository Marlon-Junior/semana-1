# Semana 1 – Introdução à Programação com Python

## Desafios realizados:

### 1. Calculadora de 100 anos  
O usuário informa seu nome e idade, e o programa calcula em qual ano ele completará 100 anos.

### 2. Verificador de direito ao voto  
O programa solicita o nome e a idade do usuário e, com base na idade, informa se ele pode votar, se o voto é opcional ou obrigatório.

### 3. Idade no futuro  
O programa pergunta quantos anos no futuro o usuário deseja calcular, e informa quantos anos ele terá nesse ano, com validação de nome, idade e valor positivo.

### 4. Calculadora de IMC  
O usuário informa seu nome, altura (em metros) e peso (em kg). O programa valida as entradas e calcula o Índice de Massa Corporal (IMC), retornando o valor arredondado.

---

## Aprendizados da semana:

- Leitura de dados com `input()` e exibição com `print()`  
- Conversão de tipos (`str` para `int` e `float`)  
- Importação e uso de módulos (`datetime`)  
- Condicionais com `if`, `elif`, `else`  
- Tratamento de exceções com `try/except`  
- Estrutura de repetição com `while`  
- Limpeza e validação de strings com `.strip()`, `.replace()` e `.isalpha()`  
- Uso da função `round()` para arredondamento de números decimais

---

## Destaque da semana:

### Cálculo de IMC
Também desenvolvi minha primeira calculadora com operações matemáticas simples e validações completas, consolidando o que aprendi até aqui.

### Validação de nomes  
Aprendi a validar nomes compostos e impedir números na entrada, usando:

```python
while True:
    nome = input("Qual o seu nome? ").strip()
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido. Use apenas letras.")
