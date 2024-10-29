def coletar_dados():
    print("Coletando dados para cálculos de IMC:");
    peso = float(input("Digite seu peso em kg: "));
    altura = float(input("Digite sua altura em metros: "));
    return {"peso": peso, "altura": altura};

def calcular_imc(dados):
    return dados["peso"] / (dados["altura"] ** 2);

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso";
    elif imc >= 18.5 and imc < 25:
        return "Peso normal";
    elif imc >= 25 and imc < 30:
        return "Sobrepeso";
    elif imc >= 30 and imc < 35:
        return "Obesidade Grau I";
    elif imc >= 35 and imc < 40:
        return "Obesidade Grau II";
    else:
        return "Obesidade Grau III";
    
def main():
    dados = coletar_dados();
    imc = calcular_imc(dados);
    classificacao = classificar_imc(imc);
    print(f"Seu IMC é {imc:.2f} e você está classificado como: {classificacao}.");