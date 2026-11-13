valor_original = float(input("Informe o valor do ingresso (R$): "))

print('''
TIPOS DE INGRESSO:
1 - Inteira: sem desconto
2 - Meia entrada: 50% de desconto
3 - Promocional: 30% de desconto
''')

desconto = 0
opcao = int(input("Escolha o tipo de ingresso: "))

match opcao:
    case 1:
        print('---- Inteira ----')
        desconto = 0
    case 2:
        print('---- Meia entrada ----')
        desconto = valor_original * 0.50
    case 3:
        print('---- Promocional ----')
        desconto = valor_original * 0.30
    case _:
       print("Opção inválida")

if opcao in [1, 2, 3]:
    valor_final = valor_original - desconto
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
else:
    print('Por favor, escolha uma opção válida.')