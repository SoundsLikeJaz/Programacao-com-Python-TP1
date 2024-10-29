candidatos = [
    {
        "nome": "João",
        "votos": 0
    },
    {
        "nome": "Maria",
        "votos": 0
    },
    {
        "nome": "José",
        "votos": 0
    }
];

def votar(candidato):
    candidatos[candidato]["votos"] += 1;
    
def exibir_resultado():
    candidatos.sort(key=lambda x: x["votos"], reverse=True);
    for candidato in candidatos:
        print(f"{candidato['nome']} - {candidato['votos']} votos");
        
    print(f"{candidatos[0]['nome']} venceu!");
    
def coletar_votos():
    print(f"Candidatos: \n1 - {candidatos[0]['nome']}\n2 - {candidatos[1]['nome']}\n3 - {candidatos[2]['nome']}");
    escolha = -1;
    while escolha != 0:
        escolha = int(input("Escolha seu voto, pressione 0 para sair: "));
        match escolha:
            case 1:
                votar(0);
                print(f"Voto computado para {candidatos[0]['nome']}");
            case 2:
                votar(1);
                print(f"Voto computado para {candidatos[1]['nome']}");
            case 3:
                votar(2);
                print(f"Voto computado para {candidatos[2]['nome']}");
            case 0:
                print("Encerrando votação.");
            case _:
                print("Voto inválido.");
                
coletar_votos();
exibir_resultado();