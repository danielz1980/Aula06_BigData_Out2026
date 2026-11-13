valor_original = float(input("Informe o valor da venda (R$): "))

print('''
FORMAS DE PAGAMENTO:
1 - PIX: 12% de desconto
2 - DÉBITO: 8% de desconto
3 - CRÉDITO: 5% de desconto
4 - DINHEIRO: 15% de desconto
''')

desconto = 0
# operacao = True
opcao = int(input("Escolha a forma de pagamento: "))

match opcao:
    case 1:
        print('---- PIX ----')
        desconto = valor_original * 0.12
    case 2:
        print('---- DÉBITO ----')
        desconto = valor_original * 0.08
    case 3:
        print('---- CRÉDITO ----')
        desconto = valor_original * 0.05
    case 4:
        print('---- DINHEIRO ----')
        desconto = valor_original * 0.15
    case _:
        # operacao = False
        print("Opção inválida")

if opcao in [1, 2, 3, 4]:
# if desconto != 0:
# if operacao == True:
    valor_final = valor_original - desconto
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
else:
    print('Por favor, escolha uma opção válida.')