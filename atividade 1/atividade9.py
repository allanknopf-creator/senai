preco_litro = float(input("Informe o preço do litro da gasolina: R$ "))
valor_pagamento = float(input("Informe o valor do pagamento: R$ "))

quantidade_litros = valor_pagamento / preco_litro

print(f"Com R$ {valor_pagamento:.2f}, você conseguiu colocar {quantidade_litros:.2f} litros de gasolina no tanque")
