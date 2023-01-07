
class paciente():
    def __init__(self,nom,ced,tel,corr,dire):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
        self.correo=corr
        self.direccion=dire
        
    def __str__(self):
        return 'nombre: {}\n cedula: {}\n telefono: {}\n correo: {}\n direccion: {}'.format(self.nombre, self.cedula,self.telefono, self.correo, self.direccion)
    
pac=paciente('carlos', '0978563421', '099876543', 'carlos@mail.com', 'av.colombia y sucre')
print(pac)