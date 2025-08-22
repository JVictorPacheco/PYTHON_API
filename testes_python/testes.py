# maca = int(input('Digite a quantidade de maçãs foram vendidadas'))
# bananas = int(input('Digite a quantidade de maçãs foram vendidadas'))


# if maca > bananas:
#     print('Maçãs vendeu mais que banana')
# elif maca == bananas:
#     print('Maçãs e babanas tiveram a mesma quantidade de vendas')
# else:
#     print('Bananas foram mais vendidas que maçãs')

#------------------------------

# atividadeA = int(input('Informe os dias para atividade A: '))
# atividadeB = int(input('Informe os dias para atividade A: '))
# atividadeC = int(input('Informe os dias para atividade A: '))



# if atividadeA < 0 or atividadeB < 0 or atividadeC < 0:
#     print("Erro: Os dias não podem ser negativos.")
# else:
#     total_tempo = atividadeA + atividadeB + atividadeC
#     print(f"O tempo total do projeto é de {total_tempo} dias.")


class Tarefa:
    lista_tarefas = []
    
    #A forma como a classe será inicializada
    def __init__(self, titulo, status=False):
        self.titulo = titulo
        self.status = status
        Tarefa.lista_tarefas.append(self)
        
    #A forma como ele ira ser apresentando no console
    def __str__(self):
        status = "✅" if self.status else "⏳"
        return f"{self.titulo} {status}"
    
    
tarefas = [
    Tarefa("Estudar Python", True),
    Tarefa("Fazer exercícios", False),
    Tarefa("Revisar código", False)
]


tarefa_estudo = Tarefa("Estudar SQL", True)

print("LISTA DE TAREFAS:")
print(f"{tarefa_estudo}")
#print(f"{Tarefa.lista_tarefas}")

# print("LISTA DE TAREFAS:")
# for tarefa in tarefas:
#     print(f"  {tarefa}")