
class cita():
    def __init__(self,fech,paci,horin,horsa,recom):
        self.fecha=fech
        self.paciente=paci
        self.horainicio=horin
        self.horasalida=horsa
        self.recomendacion=recom
        
    def __str__(self):
        return 'fecha: {}\n paciente: {}\n horainicio: {}\n horasalida: {}\n recomendacion: {}'.format(self.fecha, self.paciente,self.horainicio, self.horasalida, self.recomendacion)
    
cit= cita('domingo 8 enero 2023', 'javier', '08:15_AM', '10:15_AM', 'reposo')
print(cit)