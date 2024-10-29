preco = int(input("Digite o preço do produto: "));

if preco < 100:
    print("Não é possível aplicar desconto.");
elif preco >= 100 and preco < 200:
    print(f"O preço com desconto é R${(preco * 0.9):.2f}");
elif preco >= 200 and preco < 500:
    print(f"O preço com desconto é R${(preco * 0.85):.2f}");
else:
    print(f"O preço com desconto é R${(preco * 0.75):.2f}");