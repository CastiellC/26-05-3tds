class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota


aluno1 = Aluno("Anna", "a TDS", 8.0)
aluno2 = Aluno("Carlos", "b TDS", 7.6)


print(f"Nome: {aluno1.nome}, Turma: {aluno1.turma}, Nota: {aluno1.nota}")
print(f"Nome: {aluno2.nome}, Turma: {aluno2.turma}, Nota: {aluno2.nota}")