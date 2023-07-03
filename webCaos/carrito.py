class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = request.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito=carrito

    def agregar(self,producto):
        id = str(producto.IDMerca)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "ID":producto.IDMerca,
                "Nombre":producto.NombreMerca,
                "Precio":producto.PrecioVenta,
                "Cantidad":1,
                "Total":producto.PrecioVenta,
            }
            self.actualizar()
        else:
            self.carrito[id]["Cantidad"]+=1
            self.carrito[id]["Total"]+=producto.PrecioVenta
            self.actualizar()

    def resta(self,producto):
        id = str(producto.IDMerca)
        if id in self.carrito.keys():
            self.carrito[id]["Cantidad"]-=1
            self.carrito[id]["Total"]-=producto.PrecioVenta
            if self.carrito[id]["Cantidad"] == 0:
                self.eliminar(producto)
        self.actualizar()

    def actualizar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
        
    def eliminar(self,producto):
        id = str(producto.IDMerca)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.actualizar()

    def vaciar(self):
        self.session["carrito"]={}
        self.session.modified = True