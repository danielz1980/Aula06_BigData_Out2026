# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))
# peso = float(input("Digite seu peso: "))

# dicionario = {"nome": nome, "idade": idade, "altura": altura, "peso": peso}
# print("----- Valores do dicionário -----")

# for chave, valor in dicionario.items():
#     print(f"{chave}: {valor}")

list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['c','o','o','k','i','e']

# list_num.append(11)
# print(list_num)

list_num.insert(0, 11)
print(list_num)

list_char.remove('o') 
print(list_char)

list_char.pop(-2) # Removes the item at the specified position
print(list_char)
