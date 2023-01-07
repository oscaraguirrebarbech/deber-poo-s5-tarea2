
class enfermera():
    def __init__(self,nom,ced,tel,ocu,corr):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
        self.ocupacion=ocu
        self.correo=corr
        
    def __str__(self):
        return 'nombre: {}\n cedula: {}\n telefono: {}\n ocupacion: {}\n correo: {}'.format(self.nombre, self.cedula,self.telefono, self.ocupacion, self.correo)
    
enf= enfermera('laura', '0978562134', '0912435667', 'auxiliar', 'laura@mail.com')
print(enf)