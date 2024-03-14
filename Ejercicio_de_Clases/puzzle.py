class ClaseA:
    def obtener_instancia(self):
        return self  # Devuelve la instancia de la clase A

    def obtener_longitud(self, texto):
        return len(texto)  # Devuelve la longitud del argumento texto


def main():
    instancia_1 = ClaseA  # Asigna la clase A a la variable instancia_a
    metodo_1 = instancia_1.obtener_instancia  # Asigna el método obtener_instancia de la clase A a la variable metodo_z
    
    '''
    Esto es equivalente a escribir que la variable método 1 almacena el método obtener_instancia de la ClaseA
    '''
    
    print(metodo_1(instancia_1))  # Imprime el resultado de llamar al método obtener_instancia con la clase A como argumento
    
    
    print(f"Si escribimos: ClaseA.obtener_instancia(ClaseA) nos aparecerá lo mismo: {ClaseA.obtener_instancia(ClaseA)}")
    
    instancia_2 = instancia_1()  # Crea una instancia de la clase A y la asigna a la variable instancia_2
    
    print(instancia_2 is instancia_1())  # Compara si instancia_aa es igual a una nueva instancia de A
    
    print(ClaseA() is ClaseA()) 
    
    '''
    La expresión ClaseA() is ClaseA() verifica si dos instancias diferentes de la clase ClaseA son exactamente la 
    misma instancia. En otras palabras, comprueba si ambas instancias apuntan a la misma dirección de memoria en Python.

    Si ClaseA() crea una nueva instancia de la clase ClaseA, entonces ClaseA() is ClaseA() evaluará 
    a False, ya que cada llamada a ClaseA() crea una instancia independiente de la clase, incluso si son del mismo tipo.
    '''
    
    metodo_y = instancia_2.obtener_longitud  # Asigna el método obtener_longitud de la instancia instancia_2 a la variable metodo_y
    
    print(metodo_y(()))  # Llama al método obtener_longitud de instancia_2 con una tupla vacía como argumento
    
    print(instancia_1().obtener_longitud((instancia_1,)))  # Crea una nueva instancia de A y llama al método obtener_longitud con una tupla que contiene la clase A
    
    print(ClaseA.obtener_longitud(instancia_2, (instancia_1, metodo_1)))  # Llama al método obtener_longitud de la clase A con instancia_2 y una tupla que contiene la clase A y el método metodo_z
    
    print(instancia_2.obtener_longitud((metodo_1, 1, 'z')))  # Llama al método obtener_longitud de instancia_2 con una tupla que contiene el método metodo_z, el entero 1 y la cadena 'z'

if __name__ == "__main__":
    main()