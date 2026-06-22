import json

class Tarefa:

    def __init__(self,titulo,descricao,id_novo,status="pendente"):
        self.titulo=titulo
        self.descricao=descricao
        self.id_novo=id_novo
        self.__status=status

    def get_status(self):
        return self.__status
    def set_status(self,novo_status):
        self.__status=novo_status

    def exibir(self):
        print(f"titulo:{self.titulo} status:{self.get_status()} descrição:{self.descricao} id:{self.id_novo}")

class Tarefaurgente(Tarefa):

    def __init__(self,titulo,descricao,id_novo,prazo,status="pendente"):
        super().__init__(titulo,descricao,id_novo,status)
        self.prazo=prazo


    def exibir(self):
        print(f"titulo:{self.titulo},status:{self.get_status()},descrição:{self.descricao},prazo:{self.prazo},id:{self.id_novo}")



def cadastrar_tarefa(lista):
    try:
        titulo=input("Titulo:").strip()
        descricao=input("Descrição:").strip()

    except ValueError:
        print("Digite apenas dados compátiveis!")
        return False

    if len(titulo) < 3:
        print("Titulo deve ter no minimo 3 caracteres")
        return False

    tarefa_1=Tarefa(titulo=titulo,descricao=descricao,id_novo=criar_id(lista))

    lista.append(tarefa_1)
    print("Tarefa cadastrada com sucesso:")

    return True

def criar_id(lista):

    if not lista:
        return 1
    armazenar = 0

    for i in lista:

        if i.id_novo > armazenar:
            armazenar = i.id_novo

    return armazenar + 1



def cadastrar_tarefa_urgente(lista):

    try:
        titulo = input("Titulo:").strip()
        descricao = input("Descrição:").strip()
        prazo=input("Prazo:")

    except ValueError:
        print("Digite apenas dados compátiveis!")
        return False

    if len(titulo) < 3:
        print("Titulo deve ter no minimo 3 caracteres")
        return False

    tarefa_2 = Tarefaurgente(titulo=titulo,descricao=descricao,prazo=prazo,id_novo=criar_id(lista))

    lista.append(tarefa_2)


    return True

def listar_todos(lista):

    if not lista:
        print("Lista vazia")
        return False

    for i in lista:
      i.exibir()
    return None


def buscar_tarefa(lista,id_novo_2):

    if not lista:

        print("Lista vazia")
        return False

    for i in lista:

        if i.id_novo == id_novo_2:
            return i

    print("Tarefa não encontrada")

    return None

def carregar_dados():

    lista=[]

    try:
        with open("tarefas.json","r",encoding='utf-8') as arq:
            dados=json.load(arq)

            for i in dados:

                if "prazo" in i:

                    tarefa = Tarefaurgente(i["titulo"], i["descricao"],i["id_novo"], i["prazo"],i["status"])
                    lista.append(tarefa)
                else:

                    tarefa_3=Tarefa(i["titulo"], i["descricao"],i["id_novo"], i["status"])
                    lista.append(tarefa_3)

    except FileNotFoundError:

        return []


    return lista

def salvar_dados(lista):

    dados=[]

    if lista:

        for i in lista:

            if isinstance(i,Tarefaurgente):

                dados.append({"titulo": i.titulo,"status":i.get_status(),"descricao": i.descricao,"prazo": i.prazo,"id_novo": i.id_novo})

            elif isinstance(i,Tarefa):
                dados.append({"titulo": i.titulo,"status":i.get_status(),"descricao": i.descricao,"id_novo":i.id_novo})

        try:

            with open ("tarefas.json",'w',encoding='utf-8') as arq:
                json.dump(dados,arq,ensure_ascii=False,indent=4)

        except ValueError:

             print("Erro ao salvar arquivos")

             return False


        return True

    else:

        print("Lista vazia")
        return False


def concluir_tarefa(lista,id_novo_2):

    encontrado=buscar_tarefa(lista,id_novo_2)

    if encontrado:

        encontrado.set_status("concluida")
        return True

    else:

        print("tarefa não encontrada")
        return False

def menu():

    print("Bem vindo ao seu sistema de tarefas!")
    print("="* 50)
    print("1-Cadastrar tarefa")
    print("2-Concluir tarefa")
    print("3-Listar tarefas")
    print("4-Buscar tarefa")
    print("5-Encerrar")

def mensagem_de_erro():

        print("Digite apenas dados compátiveis")


















