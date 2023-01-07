
class historiaclinica():
    def __init__(self,paci,ingr,sal,diag,obs,recom):
        self.paciente=paci
        self.ingreso=ingr
        self.salida=sal
        self.diagnostico=diag
        self.observacion=obs
        self.recomendacion=recom
        
    def __str__(self):
        return 'paciente: {}\n ingreso: {}\n salida: {}\n diagnostico: {}\n observacion: {}\n recomendacion: {}'.format(self.paciente, self.ingreso,self.salida, self.diagnostico, self.observacion, self.recomendacion)
    
    
hiscl= historiaclinica('cesar', 'viernes', 'lunes', 'reservado', 'estres','reposo')
print(hiscl)