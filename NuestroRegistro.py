class registro:
    def __init__(self):
        #status_header = 0 ----> Activo
        #status_header = 1 ----> Borrar
        self.resgister_header = {'status': 0, 'id': 0}
        self.anotacion = ''
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0.0
        self.val4 = 0.0

    def nuevoRegistro(self, anotacion, val1, val2, val3, val4, id):
        self.anotacion = anotacion
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        self.resgister_header["status"] = 0
        self.resgister_header["id"] = id
    
    
        