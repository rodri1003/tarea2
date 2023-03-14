class salirMoto:
    def __init__ (self, nombre):
        self.nombre = nombre

motero1 = salirMoto("miedo")
motero2 = salirMoto("mota")

class uno (salirMoto):
    pass
    def salirMoto():
        return "salir con {} es caida segura".format(motero1.nombre)
    
class dos (salirMoto):
    pass
    def salirMoto():
        return "salir con {} es salir feliz xd".format(motero2.nombre)
    
astronauta1 = uno
astronauta2 = dos
print (astronauta1.salirMoto())
print (astronauta2.salirMoto())