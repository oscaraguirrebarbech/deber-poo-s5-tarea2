
class recetas():
    def __init__(self,nom,lug,med,medic,indic,sint):
        self.nombre=nom
        self.lugar=lug
        self.medico=med
        self.medicamento=medic
        self.indicaciones=indic
        self.sintomas=sint
    def __str__(self):
        return 'nombre: {}\n lugar: {}\n medico: {}\n indicaciones: {}\n sintomas: {}'.format(self.nombre, self.lugar,self.medico, self.indicaciones, self.sintomas)
    
rec= recetas('cesar', 'guayaquil', 'eduardo', 'paracetamol', '1 tableta C8/h', 'gripe')
print(rec)