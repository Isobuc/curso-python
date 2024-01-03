class persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
    
    def dormir(self):
        return f"La persona {self._nombre} esta durmiendo"
    
class estudiante(persona):
    def __init__(self, nombre, edad, sexo, id, calf, materias):
        super().__init__(nombre, edad, sexo)
        self.__id = id
        self.__calf = calf
        self.__materias = materias

    def dormir(self):
        return f"El estudiante {self._nombre} esta durmiendo en clase"

    def estudiar(self):
        return f"El estudiante {self._nombre} esta estudiando para pasar el examen con calificacion mayor a {self.__calf}"
    
class trabajador(persona):
    def __init__(self, nombre, edad, sexo, sueldo, puesto):
        super().__init__(nombre, edad, sexo)
        self.__sueldo = sueldo
        self.__puesto = puesto
    
    def dormir(self):
        return f"El trabajador {self._nombre} esta durmiendo en su puesto de trabajo"
    
    def trabajar(self):
        return f"El trabajador {self._nombre} esta trabajando en el puesto de {self.__puesto} y gana {self.__sueldo} al mes"

#inicializar objetos
persona1 = persona("Javier Mata", 19, "Hombre")
estudiante1 = estudiante("Ramses Daron", 19, "Hombre", 123456, 6.5, "Matematicas")
trabajador1 = trabajador("David Martinez", 23, "Hombre", 15000, "Gerente")

#primer metodo
print(persona1.dormir())
print(estudiante1.dormir())
print(trabajador1.dormir())

#segundo metodo
print(estudiante1.estudiar())
print(trabajador1.trabajar())

