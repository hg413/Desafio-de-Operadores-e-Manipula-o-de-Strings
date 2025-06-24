# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

precos = {
    "preco1": 50,
    "preco2": 100,
    "preco3": 500
}

while True:
    print("\n Bem-vindo a loja do Liminha")

    valor = float(input("Informe o Valor do Produto: ").strip())
    cupom = input("Informe o valor do Desconto. ex DESCONTO10 , DESCONTO20 ou SEM DESCONTO: ").strip().upper()

    if cupom in descontos:
        percentual = descontos[cupom]
        valor_desconto = valor * percentual
        preco_final = valor - valor_desconto
        print(f"Valor final sem Desconto {preco_final: .2f}")

