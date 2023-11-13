from os import system

lista = []

def listar_nomes():
    l = 1
    for p in lista:
        print(f'Tarefa {l}: {p['tarefa']}')
        l+=1

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

def menu_editar():
    print('''             MENU DE ESCOLHA
-------------------------------------------
1 - alterar nome
2 - alterar data de inicio
3 - alterar data de termino
4 - alterar local          
-------------------------------------------''')
    escolha = int(input("Opção: "))

def cadastrar():
    tarefa = str(input("Qual a tarefa?: "))
    data = input("Quando deve ser feito?: ")
    final = input("Previsão para concluir: ")
    local = str(input("Onde será feito?: "))
    dicionary = {
        'tarefa': tarefa,
        'data': data,
        'final': final,
        'local': local,
        'status': 'Pendente'
    }
    lista.append(dicionary)
    system('cls')
    print("Cadastrado com sucesso!!!!")

def concluir_tarefa():
    listar_nomes()
    print("")
    alterar = str(input("Qual tarefa deseja concluir?: ")).lower()
    for i in lista:
        if i['tarefa'] == alterar:
            i['status'] = 'concluido'

def listar_tarefas():
    for i in lista:
        print(f'''Tarefa: {i['tarefa']}
Data de inicio: {i['data']}
Data de termino: {i['final']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')

def pesquisar_tarefa():
    listar_nomes()
    print("")
    pesquisar = str(input("Escolha: "))
    system('cls')
    for i in lista:
        if i['tarefa'] == pesquisar:
            print(f'''-------------------------------------------
Tarefa: {i['tarefa']}
Data de inicio: {i['data']}
Data de termino: {i['final']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')
    
def editar_tarefa():
    listar_nomes()
    print("")
    editar = input("Qual tarefa deseja editar?: ")
    system('cls')
    for i in lista:
        if i['tarefa'] == editar:
            print(f'''-------------------------------------------
Tarefa: {i['tarefa']}
Data de inicio: {i['data']}
Data de termino: {i['final']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')
    menu_editar()
        


def programa():
    while True:
        opção = menu_principal()
        match opção:
            case 1:
                cadastrar()
            case 2:
                concluir_tarefa()
            case 3:
                system('cls')
                listar_tarefas()
            case 4:
                pesquisar_tarefa()
            case 5:
                editar_tarefa()
            case 6:
                pass
            case 7:
                print("Saindo...")
                break
            case _:
                print("Invalido...\nTente novamente")

programa()
