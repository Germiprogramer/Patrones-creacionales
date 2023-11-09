# clase Cliente
class Cliente:
    def __init__(self, usuario, nombre, direccion, telefono, email, contrasenia):
        self.usuario = usuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.contrasenia = contrasenia

    def __str__(self):
        return f"Usuario: {self.usuario}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Email: {self.email}"

    def to_dict(self):
        return {'usuario': self.usuario, 'nombre': self.nombre, 'direccion': self.direccion, 'telefono': self.telefono, 'email': self.email}
