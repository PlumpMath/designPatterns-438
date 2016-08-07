from abc import ABCMeta, abstractmethod

# Interface que representa pedaços da alma de um bruxo criminoso
class AlmaBruxoCriminoso(metaclass=ABCMeta):
    @abstractmethod
    def obterAcessoAlma(self):
        pass


# Um pedaço de alma pode vir direto do corpo do bruxo, que é a alma real
class AlmaRealBruxoCriminiso(AlmaBruxoCriminoso):
    def obterAcessoAlma(self):
        print("Fragmento de alma destruída\n")


# Um pedaço de alma pode se tornar Horcrux com um feitiço proibido
class Horcrux(AlmaBruxoCriminoso):
    def obterAcessoAlma(self):
        print("Horcrux quebrando...")
        almaReal = AlmaRealBruxoCriminiso()
        almaReal.obterAcessoAlma()


# Exemplo de como destruir dois fragmentos de alma de um bruxo que usou o feitiço Horcrux
almaFalsa = Horcrux()
almaFalsa.obterAcessoAlma()
almaReal = AlmaRealBruxoCriminiso()
almaReal.obterAcessoAlma()