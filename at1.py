class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota
Aluno1 = Aluno("Eliab", "a TDS", 10)       
Aluno2 = Aluno("Anna", "b TDS", 8)
Aluno3 = Aluno("José", "c TDS", 9)

print(Aluno1.nome, Aluno1.turma, Aluno1.nota)
print(Aluno2.nome, Aluno2.turma, Aluno2.nota)
print(Aluno3.nome, Aluno3.turma, Aluno3.nota)