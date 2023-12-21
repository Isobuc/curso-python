class alumno:
    def __init__(self, nombre, id, calf):
        self.nombre = nombre
        self.id = id
        self.calf = calf
    
    def estudiar(self):
        return f"El estudiante {self.nombre} esta estudiando para pasar el examen con calificacion mayor a {self.calf}"
    
    def ir_a_clase(self):
        return f"El estudiante {self.nombre} con id {self.id} entro a clases a la hora de entrada"
    
    def hacer_tarea(self, cantidad_tarea):
        aumento_calf = cantidad_tarea * .1
        self.calf += aumento_calf
        return f"El estudiante {self.nombre} hizo {cantidad_tarea} tarea(s) y aumento {aumento_calf} de su calificacion dejandolo en {self.calf}"
    
#inicializar objetos
alumno1 = alumno("Javier Mata", 348766, 7.9)
alumno2 = alumno("Ramses Daron", 123456, 7.5)

#primer metodo
print(alumno1.estudiar())
print(alumno2.estudiar())

#segundo metodo
print(alumno1.ir_a_clase())
print(alumno2.ir_a_clase())

#tercer metodo
print(alumno1.hacer_tarea(5))