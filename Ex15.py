def inicio():
    print("Você acorda em um lugar escuro e úmido. Você não se lembra de como chegou ali. Você olha ao redor e vê uma porta à sua frente.");
    escolha = input("O que você faz?\n1 - Abre a porta\n2 - Grita por socorro\n3 - Tenta se lembrar de como chegou ali\n");

    if escolha == "1":
        abrir_porta();
    elif escolha == "2":
        gritar();
    elif escolha == "3":
        tentar_se_lembrar();

def abrir_porta():
    print("Você abre a porta e vê um corredor escuro à sua frente. Você ouve um barulho vindo do fim do corredor.");
    escolha = input("O que você faz?\n1 - Anda em direção ao barulho\n2 - Volta para o quarto\n3 - Grita por socorro\n");

    if escolha == "1":
        bad_ending();
    elif escolha == "2":
        volta_para_o_quarto();
    elif escolha == "3":
        gritar();

def volta_para_o_quarto():
    print("Você volta para o quarto e a porta se fecha atrás de você. Você tenta abri-la, mas não consegue.");
    escolha = input("O que você faz?\n1 - Grita por socorro\n2 - Se esconde\n3 - Tenta se lembrar de como chegou ali\n");

    if escolha == "1":
        gritar();
    elif escolha == "2":
        escapou();
    elif escolha == "3":
        tentar_se_lembrar();

def gritar():
    print("Você grita por socorro, mas a resposta é um terror absoluto. Você ouve passos se aproximando da porta.");
    escolha = input("O que você faz?\n1 - Abre a porta\n2 - Se esconde\n3 - Continua gritando\n");

    if escolha == "1" or escolha == "3":
        encontrar_criatura();
    elif escolha == "2":
        escapou();

def tentar_se_lembrar():
    print("Você tenta se lembrar de como chegou ali, mas tudo o que você consegue é um vazio absoluto.");
    escolha = input("O que você faz?\n1 - Abre a porta\n2 - Grita por socorro");

    if escolha == "1":
        abrir_porta();
    elif escolha == "2":
        gritar();

def encontrar_criatura():
    print("Ela te encontra. Você não sabe o que é, mas sabe que é a morte.");
    
    bad_ending();
    

def escapou():
    print("Você escapou do pesadelo! \nAo menos por enquanto...");

def bad_ending():
    print("No final, todos os caminhos levam a isso. \nVocê morreu.");