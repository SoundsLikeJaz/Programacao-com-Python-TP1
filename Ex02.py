from datetime import timedelta

def coletar_tempo():
    return float(input("Digite o tempo a ser convertido: "));

def definir_minutos(tempo):
    return timedelta(minutes = tempo);

def definir_horas(tempo):
    return timedelta(hours = tempo);

def horas_para_minutos(tempo):
    return tempo.total_seconds() / 60;

def minutos_para_horas(tempo):
    return tempo.total_seconds() / 3600;

def main():
    tempo = coletar_tempo();
    opcao = input("Deseja armazenar como minutos ou horas? (Digite 'm' para minutos e 'h' para horas): ");
    
    if 'm' in opcao.lower():
        tempo_timedelta = definir_minutos(tempo);
        print(f"Armazenado como {tempo} minutos (equivalente a {minutos_para_horas(tempo_timedelta):.1f} horas).");
    elif 'h' in opcao.lower():
        tempo_timedelta = definir_horas(tempo);
        print(f"Armazenado como {tempo} horas (equivalente a {horas_para_minutos(tempo_timedelta):.1f} minutos).");
    else:
        print("Entrada inválida.");
        
main();