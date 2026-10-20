print("\n--- DADOS DO FUNCIONÁRIO ---")
nome = input("nome: ")
salario_bruto = float(input("salário: "))
desconto  = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto

print(f"Nome: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de 11%: R$ {desconto:.2f}")
print(f"Novo salário: R$ {salario_liquido:.2f}")