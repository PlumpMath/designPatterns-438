class Singleton(type):
    _instancias = {}
    def __call__ (cls):
        if cls not in cls._instancias:
            print("Isso acaba de ser construído em Hogwarts")
            cls._instancias[cls] = super(Singleton, cls).__call__()
        else:
            print ("Ja existe isso em Hogwarts")
            cls._instancias[cls].__init__()
        return cls._instancias[cls]

class Qpitch(metaclass = Singleton):
    def __init__(self):
        print ("O endereço da quadra de quadribol é " + str(hex(id(self))))
