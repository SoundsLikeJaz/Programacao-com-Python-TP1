import random;
import math;

personagens = ["uma princesa", "um principe", "um rei", "um cavaleiro", "um dragao", "um mago", "um elfo", "um anao", "um gigante", "um troll"];
cenarios = ["num castelo", "numa floresta", "numa montanha", "numa caverna", "numa cidade", "numa vila", "numa ilha", "numa planicie", "numa praia", "num deserto"];
acoes = ["beijou", "matou", "salvou", "derrotou", "enfeiticou", "ajudou", "protegeu", "prendeu", "fugiu de", "domou"];
finais = ["felizes para sempre", "tristes para sempre", "em paz", "em guerra", "em harmonia", "em desespero", "em festa", "em luto", "em segredo", "em duvida"];

def index_aleatorio(lista):
    return math.floor(len(lista) * random.random());

historia = f"Era uma vez {personagens[index_aleatorio(personagens)]} que viveu {cenarios[index_aleatorio(cenarios)]}. Um dia, {personagens[index_aleatorio(personagens)]} {acoes[index_aleatorio(acoes)]} {personagens[index_aleatorio(personagens)]}. E viveram {finais[index_aleatorio(finais)]}.";

print(historia);