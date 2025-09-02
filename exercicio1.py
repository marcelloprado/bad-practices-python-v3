# 1 - faltam as aspas, e em um cógigo normal, não vamos executar essa linhar
print(Bem-vindo à sua lista de tarefas!)

# 2
tarefas = "uma lista vazia" 

def adicionar_tarefa():
    # 3
    nova_tarefa = (input("Digite a nova tarefa: "))
    # 4
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso.")

def ver_tarefas():
    print("\nSuas tarefas:")
    # 5
    for i in tarefas:
        # 6 - temos 2 erros aqui
        print(f"{i+1}. {tarefas[i]}")

def remover_tarefa():
    ver_tarefas()
    try:
        # 7
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        # 8
        del tarefas[indice]
        print("Tarefa removida com sucesso!")
    except Exception as e:
        # 9
        print("Erro ao remover tarefa:", e)
    
# 10
def Menu():
    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        escolha = int(input("Escolha uma opção: "))

        if escolha = 1: # 11
            adicionar_tarefa()
        elif escolha == 2:
            ver_tarefas()
        elif escolha == 3:
            remover_tarefa()
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada para iniciar o programa
# 12
menu()
