import math;

numero_secreto = math.ceil(100 * math.random());

print("Adivinhe o número secreto entre 1 e 100");

tentativas = 0;

palpite = int(input("Digite seu palpite: "));

while palpite != numero_secreto:
    tentativas += 1;
    if palpite > numero_secreto:
        print("Muito alto!.");
    elif palpite < numero_secreto:
        print("Muito baixo!.");

    palpite = int(input("Digite seu palpite: "));
    
print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.");