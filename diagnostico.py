
class diagnostico():
    def __init__(self,enfe,obs):
        self.enfermedad=enfe
        self.observacion=obs
    
    def __str__(self):
        return 'enfermedad: {}\n observacion: {}\n'.format(self.enfermedad, self.observacion)

diag= diagnostico('gripe','jarabe')
print(diag)