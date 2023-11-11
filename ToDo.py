from os import system

lista = []


def menu_principal():
    print('''
                  To Do
-------------------------------------------
1 - Cadastrar um tarefa
2 - Marcar tarefa como concluida
3 - Listar todas as tarefas
4 - Pesquisar uma tarefa
5 - Editar uma tarefa
6 - Excluir uma tarefa
7 - Sair
-------------------------------------------''')
    escolha = int(input("Opção: "))
    system('cls')
    return escolha

def cadastrar():
    tarefa = str(input("Qual a tarefa?: "))
    data = str(input("Quando deve ser feito?: "))
    local = str(input("Onde será feito?: "))
    dicionary = {
        'tarefa': tarefa,
        'data': data,
        'local': local,
        'status': 'Pendente'
    }
    lista.append(dicionary)
    system('cls')
    print("Cadastrado com sucesso!!!!")

def listar_tarefas():
    for i in lista:
        print(f'''
Tarefa: {i['tarefa']}
Data: {i['data']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')

def programa():
    while True:
        opção = menu_principal()
        match opção:
            case 1:
                cadastrar()
            case 2:
                system('cls')
                listar_tarefas()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saindo...")
                break
            case _:
                print("Invalido...\nTente novamente")

programa()
