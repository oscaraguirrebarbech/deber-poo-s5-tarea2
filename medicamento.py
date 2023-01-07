
class medicamento():
    def __init__(self,nom,inst,cant,dos,dur,frec):
        self.nombre=nom
        self.instrucciones=inst
        self.cantidad=cant
        self.dosis=dos
        self.duracion=dur
        self.frecuencia=frec
        
    def __str__(self):
        return 'nombre: {}\n instrucciones: {}\n cantidad: {}\n dosis: {}\n duracion: {}\n frecuencia:{}'.format(self.nombre, self.instrucciones, self.cantidad, self.dosis, self.duracion, self.frecuencia)
    
medi= medicamento('analgan','precaucion','1 caja','1 tableta','cada 8 horas','15 dias')
print(medi)