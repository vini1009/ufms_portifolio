choice_1, choice_2 = map(int, input().split()) # Obtem a entrada de pedidos. Ex.:3 2

products = {
    1: {
        "name": "Cachorro Quente",
        "price": 4.00 
    },
    2: {
        "name": "X-Salada",
        "price": 4.50
    },
    3: {
        "name": "X-Bacon",
        "price": 5.00
    },
    4: {
        "name": "Torrada Simples",
        "price": 2.00
    },
    5: {
        "name": "Refrigerante",
        "price": 1.50
    }
}

result = products[choice_1]['price'] * choice_2 # Multiplica o Preço pela Quantia

print(f"Total: R$ {result:.2f}")