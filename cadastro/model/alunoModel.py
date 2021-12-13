class AlunoModel:

    def __init__(self):
        self.__Matricula = str
        self.__Nome = str
        self.__Email = str
        self.__Gênero = str
        self.__Senha = str

#================================================================
    def setMatricula(self,Matricula):
        self.__Matricula = Matricula

    def setNome(self,Nome):
        self.__Nome = Nome

    def setEmail(self,Email):
        self.__Email = Email

    def setGênero(self,Gênero):
        self.__Gênero = Gênero
        
    def setSenha(self, Senha):
        self.__Senha = Senha


#================================================================
    def getMatricula(self):
        return self.__Matricula

    def getNome(self):
        return self.__Nome

    def getEmail(self):
        return self.__Email

    def getGênero(self):
        return self.__Gênero

    def getSenha(self):
        return self.__Senha

#================================================================



    def encerrar(self):
        return self.getMatricula() + '\n' + self.getSenha() + '\n' + self.getEmail() + '\n' + self.getGênero()+ '\n' + self.getSenha()
