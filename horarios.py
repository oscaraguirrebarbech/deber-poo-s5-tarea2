
class horarios():
    def __init__(self,di,horin,horfi):
        self.dia= di
        self.horainicio= horin
        self.horafinal= horfi
    def __str__(self):
        return 'dia: {}\n horainicio: {}\n horafinal: {}\n'.format(self.dia, self.horainicio,self.horafinal)
    
hor= horarios('sabado', '12:00_AM', '14:00_PM')
print(hor)