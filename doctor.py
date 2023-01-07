class doctor():
    def __init__(self,nom,ced,tel,car,corr):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
        self.cargo=car
        self.correo=corr
        
        
    def __str__(self):
        return 'nombre: {}\n cedula: {}\n telefono: {}\n cargo: {}\n correo: {}'.format(self.nombre, self.cedula,self.telefono, self.cargo, self.correo)
        
        
doc= doctor('angel', '0987654321', '0999999999', 'pediatria', 'angel@mail.com')
print(doc)