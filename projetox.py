def imprimir_ordem_istalacao(dependencias):
#defini a funcao imprimir_ordem instalacao e coloquei a lista 'dependencias' como parâmetro
    mapa_de_dependencias = {} # criei um dicionario vazio p/guardar as dependencias

    # recursão pra preencher o dicionario com as dependencias fornecidas
    for dependencia in dependencias: # 'dependencia' eh uma variavel local pra representar cada elemento na lista 'dependencias'
        tarefa, lista_dependencias = dependencia.split(": ") # a str 'dependencia' esta sendo dividida em duas partes baseado no caractere ": " resultando em uma lista com as duas partes. na primeira parte eh atribuida à variavel 'tarefa' e na segunda parte eh atribuida à variavel 'lista_dependencias'
        lista_dependencias = lista_dependencias.split(", ") # a variavel 'lista_dependencias' eh dividida de novo baseado no caractere ", " resultando em uma lista de dependencias individuais, que é atribuida novamente à variavel 'lista_dependencias' e substitui o valor anterior
        mapa_de_dependencias[tarefa] = lista_dependencias # 'lista_dependencias' eh atribuida ao dicionario, sendo 'tarefa' a chave e 'lista_dependencias' eh o valor
        # a chave 'tarefa' perminte acessar as dependencias

    #criar uma lista p/ordem de instalacao das dependencias
    ordem_de_instalacao = []

    #criar conjunto p/verificar as tarefas
    tarefa_verificada = set()

#recursividade
    def dep(tarefa): #defini a funcao dep com 'tarefa' como parametro; a funcao dep ira percorrer as dependencias de uma tarefa e adicionar à lista da ordem de instalacao
        if tarefa in tarefa_verificada:
            return
        tarefa_verificada.add(tarefa) # metodo .add() p/adicionar um elemento ao conjunto 'tarefa_verificada' caso a tarefa ja tenha sido verificada, o conjunto nao sera alterado

        if tarefa in mapa_de_dependencias: #  verificar se a 'tarefa' atual esta no dicionario, se sim, existem dependencias associadas a ela
            for dependencia in mapa_de_dependencias[tarefa]: # o loop ira percorrer cada 'dependencia' na lista 'mapa_de_dependencias[tarefa]'
                dep(dependencia) # a funcao 'dep' eh chamada recursivamente para cada 'dependencia' p/que todas sejam adicionadas a lista 'ordem_de_instalacao' corretamente

        ordem_de_instalacao.append(tarefa) # o metodo .append() adiciona um novo elemento no fim da lista
     
    # percorrer todas as tarefas(chaves) do dicionario e chamar a funcao 'dep' pra cada umma
    for tarefa in mapa_de_dependencias.keys(): # o metodo .keys() retorna as chaves do dicionario
        dep(tarefa)
        # caso existam dependencias da tarefa, elas serao adicionadas a lista 'ordem_de_instalacao'

    #chamar a lista 'ordem_de_instalacao' e usar o metodo reverse() p/inverter a ordem da lista, e retornar a lista
    ordem_de_instalacao.reverse() # o metodo .reverse() inverte a ordem da lista, parq que as dependencias fiquem na ordem correta de instalacao
    return ordem_de_instalacao # retorno da lista na ordem correta de instalacao

#lista 'dependencias' e os valores de entrada
dependencias = [
        #"X: A, B, C, D, E",
        #"C: A, B, D",
        #"E: A"
        "Y: A, B, C, D, E",
        "A: B",
        "B: C",
        "C: D",
        "E: A"
]

ordem = imprimir_ordem_istalacao(dependencias) # declaracao da variavel 'ordem' que recebe a funcao 'imprimir_ordem_istalacao(dependencias)'
saida = ", ".join(str(item) for item in ordem) # o metodo join() desempacota os itens da lista e a funcao str() converte os elementos da lista em strings
#print(ordem) # saida com colchetes
print(saida) # saida formatada sem colchetes
