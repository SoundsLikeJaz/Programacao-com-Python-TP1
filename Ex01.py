def coletar_numeros():
    numeros = []
    num1 = int(input("Digite o primeiro número: "));
    num2 = int(input("Digite o segundo número: "));
    
    numeros.append(num1);
    numeros.append(num2);
    
    return numeros

def somar_numeros(numeros):
    return sum(numeros);

def subtrair_numeros(numeros):
    return numeros[0] - numeros[1];

def multiplicar_numeros(numeros):
    return numeros[0] * numeros[1];

def dividir_numeros(numeros):
    return numeros[0] / numeros[1];

def divisao_inteira(numeros):
    return numeros[0] // numeros[1];


def main():
    numeros = coletar_numeros();
    print(f"A soma de {numeros[0]} e {numeros[1]} é: {somar_numeros(numeros)}");
    print(f"A subtração de {numeros[0]} e {numeros[1]} é: {subtrair_numeros(numeros)}");
    print(f"A multiplicação de {numeros[0]} e {numeros[1]} é: {multiplicar_numeros(numeros)}");
    print(f"A divisão de {numeros[0]} por {numeros[1]} é: {dividir_numeros(numeros)}");
    print(f"A divisão inteira de {numeros[0]} por {numeros[1]} é: {divisao_inteira(numeros)}");
    
main();