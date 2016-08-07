from abc import ABCMeta, abstractmethod

# Essa classe define a interface FilhoTrouxa
class FilhoTrouxa(metaclass = ABCMeta):
    @abstractmethod
    def brincar(self):
        pass

    @abstractmethod
    def estudar(self):
        pass
#Adaptee = Se o filho trouxa for um bruxo de sangue ruim então os métodos chamados serão os do adaptee
class FilhoBruxo(object):
    def voar(self):
        print("Estou voando")
    def enfeitica(self):
        print ("Estou enfeiticando")

# Se FilhoSangueRuim for instanciado ele usará os métodos do adaptee (metodos de filhos bruxos) e não os metodos para humanos normais
class FilhoSangueRuim(FilhoTrouxa, FilhoBruxo):#python permite herança multipla

    def brincar(self):
        self.voar()
    def estudar(self):
        self.enfeitica()

# Se Filho Humano for instanciado ele usa os métodos que ele está sobreescrevendo, sem precisar de um adaptee (demonstrando que isso é possível em python)
class FilhoHumano(FilhoTrouxa):
    def brincar(self):
        print("Estou brincando")
    def estudar(self):
        print("Estou estudando")
