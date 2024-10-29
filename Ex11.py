qtd_dados = int(input("Digite a quantidade de dados: "));

def rolagens(qtd_dados):
    import random;
    import math;
    resultados = [];
    for i in range(qtd_dados):
        resultados.append(math.floor(6 * random.random()) + 1);
    return resultados;

def exibir_rolagens(resultados):
    print("\nRolagens:");
    for i in range(len(resultados)):
        print(f"Dado {i+1}: {resultados[i]}");