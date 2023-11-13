from os import system

lista = []

def listar_nomes():
    b = 1
    for p in lista:
        print(f"Tarefa {b}: {p['tarefa']}")
        b+=1

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
1 - Alterar nome
2 - Alterar data
3 - Alterar local  
4 - Alterar TUDO        
-------------------------------------------''')
    escolha = int(input("Opção: "))
    return escolha

def cadastrar():
    tarefa = str(input("Descrição da tarefa: "))
    data = input("Data para a realização da tarefa (seg, ter, ...): ")
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

def concluir_tarefa():
    listar_nomes()
    print("")
    alterar = str(input("Qual tarefa deseja concluir?: "))
    for i in lista:
        if i['tarefa'] == alterar:
            i['status'] = 'concluido'

def listar_tarefas():
    for i in lista:
        print(f'''Tarefa: {i['tarefa']}
Data: {i['data']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')

def pesquisar_tarefa():
    listar_nomes()
    print("")
    pesquisar = str(input("Escolha: ")).lower()
    system('cls')
    for i in lista:
        if i['tarefa'] == pesquisar:
            print(f'''-------------------------------------------
Tarefa: {i['tarefa']}
Data: {i['data']}
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
Data: {i['data']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')
            opc = menu_editar()
            match opc:
                case 1:
                    system('cls')
                    nova_descricao = str(input("Nova descrição: "))
                    i['tarefa'] = nova_descricao
                    system('cls')
                    print("Alterado com sucesso!!!")
                case 2:
                    system('cls')
                    nova_data = str(input("Nova data: "))
                    i['data'] = nova_data
                    system('cls')
                    print("Alterado com sucesso!!!")
                case 3:
                    system('cls')
                    novo_local = str(input("Novo local: "))
                    i['local'] = novo_local
                    system('cls')
                    print("Alterado com sucesso!!!")
                case 4:
                    system('cls')
                    nova_descricao = str(input("Nova descrição: "))
                    nova_data = str(input("Nova data: "))
                    novo_local = str(input("Novo local: "))
                    local = lista.index(i)
                    lista[local] = {
                        'tarefa': nova_descricao,
                        'data': nova_data,
                        'local': novo_local,
                        'status': 'Pendente'
                    }
                    system('cls')
                    print("Alterado com sucesso!!!")

def excluir_tarefa():
    listar_nomes()
    tarefa = str(input("Qual tarefa deseja excluir: "))
    for i in lista:
        if i['tarefa'] == tarefa:
            local = lista.index(i)
            lista.pop(local)
            system('cls')
            print("excluido com sucesso!!!")       

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
                excluir_tarefa()
            case 7:
                print("Saindo...")
                break
            case _:
                print("Invalido...\nTente novamente")

programa()