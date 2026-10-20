nome = input("Digite seu nome: ")
salario_bruto = float(input("Digite seu salário bruto: R$ "))
if salario_bruto >= 3000:
    inss = salario_bruto * 0.11
elif salario_bruto >= 2000:
    inss = salario_bruto * 0.09
else:
    inss = salario_bruto * 0.08
if salario_bruto >= 2000:
    vale_transporte = salario_bruto * 0.06
else:
    vale_transporte = salario_bruto * 0.05
if salario_bruto >= 3000:
    bonus = 300
else:
    bonus = 200
if salario_bruto >= 3000:
    cargo = "Acionista"
elif salario_bruto >= 2000:
    cargo = "Gerente"
else:
    cargo = "Vendedor"
salario_liquido = salario_bruto - (inss + vale_transporte) + bonus
print("\n===== RESULTADO =====")
print("Nome:", nome)
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Vale-transporte: R$ {vale_transporte:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print("Cargo:", cargo)
print(f"Salário líquido: R$ {salario_liquido:.2f}")