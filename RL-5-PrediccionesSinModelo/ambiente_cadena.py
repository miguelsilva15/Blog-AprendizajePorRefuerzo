class Cadena:   
    
    nodos = ["F1", "A", "B", "C", "D", "E", "F2"]
    def __init__(self):
        self.posicion = 3 # posicion inicial
        self.terminado = False
        self.nodo = self.nodos[self.posicion]
    
    def estado_actual(self):
        return self.posicion
        
    def movimiento(self, decision):
        if not self.terminado:
            nueva_posicion = self.posicion + decision    
            recompensa = self.obtener_recompensa(nueva_posicion)
            self.posicion = nueva_posicion
            self.nodo = self.nodos[self.posicion]
            if self.nodo in ['F1', 'F2']:
                self.terminado = True
            return recompensa, self.posicion, self.nodo, self.terminado
        
    def obtener_recompensa(self, nueva_posicion):
        return 1.0 if self.nodos[nueva_posicion] == "F2" else 0.0