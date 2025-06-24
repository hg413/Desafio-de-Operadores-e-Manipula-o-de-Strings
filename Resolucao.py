# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}


precos_validos = [50, 100 , 500]

while True:
    print("\n Bem-vindo a loja do Liminha")

    valor = float(input("Informe o Valor do Produto: "))
    if valor not in precos_validos:
            print("Opção invalida, escolha os valores certos!!")
            continue
            
    while True:
        cupom = input("Informe o valor do Desconto. ex DESCONTO10 , DESCONTO20 ou SEM DESCONTO: ").strip().upper()
        if cupom not in descontos:
            print("Opção invalida, informe o cupom certo")
            continue

        if cupom in descontos:
            percentual = descontos[cupom]
            valor_desconto = valor * percentual
            preco_final = valor - valor_desconto
            print(f"Valor final sem Desconto {preco_final: .2f}")
            break

