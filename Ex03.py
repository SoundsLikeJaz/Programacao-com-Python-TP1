def combinar_nomes(nome1, nome2):
    metade1 = nome1[:len(nome1)//2]
    metade2 = nome2[:len(nome2)//2]
    fim1 = nome1[len(nome1)//2:]
    fim2 = nome2[len(nome2)//2:]
    
    combinacao1 = metade1 + fim2
    combinacao2 = metade2 + fim1
    combinacao3 = metade1 + metade2.lower() + fim1 + fim2
    
    return combinacao1, combinacao2, combinacao3

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

sugestao1, sugestao2, sugestao3 = combinar_nomes(nome1, nome2);

print(f"\nAqui estão algumas combinações criativas de nomes: \n{sugestao1}\n{sugestao2}\n{sugestao3}");