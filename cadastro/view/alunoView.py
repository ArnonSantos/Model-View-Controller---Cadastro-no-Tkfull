from view.Tkfull import Janela
from controller.alunoController import AlunoController
class AlunoView:

    camera = [['Cadastro de Aluno']]

    cam = [['Matrícula', input],
             ['Nome', input],
             ['E-mail', input],
             ['Gênero', ("Masculino", "Feminino")],
             ['Senha', complex],
             [{'*Encerrar':'assets/img/sair.png'},{'*Cadastrar':'assets/img/aceitar.png'}]
             ]

    def __init__(self):
        self.p = Janela()
        self.p.gerar(self.camera)
        self.p.gerar(self.cam)
        self.p.setEvento(13,self.enviar)
        self.p.start()

    def enviar(self):
        c = AlunoController()
        m = c.Dados(self.p)
        self.p.mensagem(m)


