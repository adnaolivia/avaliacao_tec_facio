<h3>estudo do problema:</h3>

- projeto x possui n dependencias a serem instaladas
- cada dependencia possui tambem uma lista de dependencias
	projeto -> dependencias -> dependencias

- determinar a ordem correta de instalação das dependencias de um projeto. para cada dependencia, pode haver uma lista de outras dependencias das quais ela depende
- analisar a estrutura de dependencias econstruir uma ordem de instalacao que respeite todas as dependencias
- percorrer as dependencias (for)
- as dependencias de uma tarefa devem ser instaladas antes dela propria

<b>OBJETIVO</b>
- imprimir a ordem em que as dependencias precisam ser instaladas, levando em consideração as dependencias diretas e indiretas
--------------------------------------------------------------------

<h3>sequencia de passos:</h3>

- criar uma estrutura de dados para armazenar as dependencias e suas respectivas dependencias (dicionario mapa_de_dependencias -> dep_direta: chave ; dep_indireta: valor)
- preencher estrutura de dados com as informacoes fornecidas
	- identificcar as dep. diretas e indiretas e adicionar essas informacoes a estrutura de dados
- criar uma lista vazia p/guardar a ordem de instalacao das dep.
- criar um conjunto vazio p/verificar as dep. ja visitadas
- percorrer as dep. recursivamente: parametros: a atual tarefa, a estrutura, a lista e o conjunto de dep.
	- se a tarefa ja foi verificada, retornar
	- adicionar a tarefa atual ao conjunto de tarefas visitadas
	- verificar se a tarefa atual possui dep. na estrutura de dados. se sim, percorrer as dep. chamando a funcao
	- adicionar tarefa atual na lista
- percorrer todas as chaves da estrutura de dados e chamar a funcao p/cada uma 
- reverter a lista de instalacao
- imprimir a lista :)

--------------------------------------------------------------------

<h3>estruturação do algoritmo:</h3>

- criar um dicionario "mapa_de_dependencias" p/guardar as dependencias de cada projeto
- preencher o dicionario com as dependencias fornecidas
- criar uma lista p/ordem de instalacao das dependencias (ordem_de_instalacao)
- criar um conjunto "projeto_verificado" para não verificar um projeto mais de uma vez
- definir uma funcao 'dep' para percorrer as dependencias de um projeto, e adiciona-las (as dependencias) à lista "ordem_de_instalacao"
- percorrer todos os projetos do "mapa_de_dependencias" e chamar a funcao 'dep' para cada um
- inverter a lista "ordem_de_instalacao" para obter a ordem correta de instalacao
- retornar a lista "ordem_de_instalacao"
- imprimir "ordem_de_instalacao"
