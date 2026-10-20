print("Condicional com 3 ou mais respostas")
num = int(input("Número: "))
if(num >0):
    print(f"{num} é positivo.")
elif(num < 0):
    print(f"{num} é negativo.")
else: 
    print(f"{num} é zero (0).")