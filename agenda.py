#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input("Selecione uma opção"))
print("Selecionou a ", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
else:
	funcoes.falha()


