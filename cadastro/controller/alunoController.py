from model.alunoModel import AlunoModel
class AlunoController:

    def Dados(self,p):
        Matricula = str(p.getTexto(3))
        Nome = str(p.getTexto(5))
        Email = str(p.getTexto(7))
        Gênero = str(p.getTexto(9))
        Senha = str(p.getTexto(11))
        molde = AlunoModel()
        molde.setMatricula(Matricula)
        molde.setNome(Nome)
        molde.setEmail(Email)
        molde.setGênero(Gênero)
        molde.setSenha(Senha)
        molde.encerrar()
        return molde.encerrar()
